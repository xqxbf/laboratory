# 动态重新加载模块

import importlib
import sys
import time

def load_plugin(plugin_name):
    """
    动态重新加载名为 plugin_name 的模块。
    如果模块尚未加载，则首次加载；否则重新加载。
    :return: 加载的模块对象，加载失败返回 None
    """
    module_name = plugin_name
    try:
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
        return sys.modules[module_name]
    except Exception as e:
        print(f"加载插件 {module_name} 失败: {e}")
        return None

def monitor_and_reload(plugin_name):
    """
    监控插件目录，当插件文件变化时，动态重新加载插件模块。
    :param plugin_name: 插件模块名称
    """
    import os
    
    plugin = load_plugin(plugin_name)
    if not plugin:
        print(f"插件 {plugin_name} 初始加载失败，退出监控")
        return
    
    plugin_path = plugin.__file__
    last_mtime = os.path.getmtime(plugin_path)
    
    print(f"开始监控插件 {plugin_name}，文件路径: {plugin_path}")
    
    try:
        while True:
            try:
                current_mtime = os.path.getmtime(plugin_path)
                if current_mtime != last_mtime:
                    print(f"检测到插件 {plugin_name} 变化，重新加载...")
                    new_plugin = load_plugin(plugin_name)
                    if new_plugin:
                        plugin = new_plugin
                        plugin_path = plugin.__file__
                        last_mtime = current_mtime
                        print(f"插件 {plugin_name} 重新加载成功")
            except FileNotFoundError:
                print(f"插件 {plugin_name} 文件不存在，等待...")
                time.sleep(2)  # 延长等待时间
            except Exception as e:
                print(f"监控插件 {plugin_name} 时出错: {e}")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n停止监控插件 {plugin_name}")

if __name__ == "__main__":
    plugin_name = 'test'
    plugin = load_plugin(plugin_name)
    
    if plugin:
        if hasattr(plugin, 'test'):
            plugin.test()
        else:
            print(f"插件 {plugin_name} 中没有 test 方法")
        
        monitor_and_reload(plugin_name)
    else:
        print(f"插件 {plugin_name} 加载失败")