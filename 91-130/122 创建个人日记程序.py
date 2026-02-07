# 创建个人日记程序

from typing import List
import os
import time
import datetime
import sqlite3
import getpass
import hashlib

class DiaryManager:

    def __init__(self, diary_dir: str = "diaries"):
        """
        初始化日记目录
        
        :param diary_dir: 存储日记文件的目录，默认值为 "diaries"
        """
        self.diary_dir = diary_dir
        os.makedirs(self.diary_dir, exist_ok=True)
    
    def write_diary(self, username: str, content: List[str]):
        """
        写入用户的日记
        
        :param username: 用户名
        :param content: 日记内容，为字符串列表，每个元素为一行
        :return: None
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        filename = f"{username}_{timestamp}.txt"
        filepath = os.path.join(self.diary_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(content)
        
        print(f"日记已保存至：{filepath}")
    
    def create_diary(self, username: str):
        """
        创建用户的个人日记文件
        
        :param username: 用户名
        :return: None
        """
        diary_path = os.path.join(self.diary_dir, f"{username}.txt")
        with open(diary_path, "w", encoding="utf-8") as f:
            f.write(f"个人日记文件 - {username}\n")
        print(f"已创建用户 {username} 的个人日记文件")

    def read_diary(self, username: str):
        """
        读取用户的个人日记文件
        
        :param username: 用户名
        :return: None
        """
        diary_path = os.path.join(self.diary_dir, f"{username}.txt")
        if not os.path.exists(diary_path):
            print(f"用户 {username} 的日记文件不存在")
            return
        
        with open(diary_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"用户 {username} 的日记内容：")
            print(content)



class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = hashlib.md5(hashlib.md5(password.encode()).hexdigest().encode()).hexdigest()
        self.diary_manager = DiaryManager()
        self.is_logged_in = False
    
    def login(self, conn, cursor):
        """
        用户登录
        
        :param conn: 数据库连接
        :param cursor: 数据库游标
        :return: str: 登录成功的用户名，失败返回空字符串
        """
        print("用户登录")
        username = input("请输入用户名：")
        password = getpass.getpass("请输入密码：")
        
        # 从数据库查询用户信息
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        
        if result and hashlib.md5(hashlib.md5(password.encode()).hexdigest().encode()).hexdigest() == result[0]:
            print("登录成功")
            self.is_logged_in = True
            self.username = username
            return username
        else:
            print("登录失败：用户名或密码错误")
            return ""
        
    def register(self, conn, cursor):
        """
        用户注册
        
        :param conn: 数据库连接
        :param cursor: 数据库游标
        :return: None
        """
        print("用户注册")
        username = input("请输入用户名：")
        password = getpass.getpass("请输入密码：")
        confirm_password = getpass.getpass("请确认密码：")
        
        if password != confirm_password:
            print("两次密码输入不一致")
            return
        
        # 检查用户名是否已存在
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("用户名已存在")
            return
        
        self.username = username
        self.password = hashlib.md5(hashlib.md5(password.encode()).hexdigest().encode()).hexdigest()
        self.diary_manager.create_diary(username)
        self.save_username_password(conn, cursor)
        print("注册成功，请牢记您的密码，遗失后将无法找回")

    def save_username_password(self, conn, cursor):
        """
        将用户名和加密后的密码保存到 SQLite 数据库
        """
        cursor.execute("""
            INSERT OR REPLACE INTO users (username, password)
            VALUES (?, ?)
        """, (self.username, self.password))
        conn.commit()
        print("用户信息已保存到数据库")



if __name__ == "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')
    print("初始化程序中...")

    # 1. 确保日记目录存在
    print("检查数据库目录是否存在...", end='')
    diary_dir = "diaries"
    os.makedirs(diary_dir, exist_ok=True)
    print("True")
    
    # 2. 定义数据库路径
    db_path = os.path.join(diary_dir, "users.db")
    
    # 3. 检查数据库文件是否存在
    print("检查数据库是否存在...", end='')
    db_exists = os.path.exists(db_path)
    if db_exists:
        print("True")
    else:
        print("False\n自动创建中...")
        time.sleep(1)
        print("已创建数据库文件")    
    
    # 4. 创建数据库连接（如果文件不存在，SQLite会自动创建）
    print("创建数据库连接...", end='')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("True")
    
    # 5. 检查用户表是否存在
    print("检查用户表是否存在...", end='')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone() is not None
    if table_exists:
        print("True")
    else:
        print("False")  
        # 6. 创建用户表（如果不存在）
        print("创建用户表...", end='')
        if not table_exists:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()
            print("已创建用户表")
    
    # 7. 确认数据库状态
    if db_exists:
        # 8. 初始化管理员账号
        cursor.execute("SELECT username FROM users WHERE username = ?", ("admin",))
        admin_exists = cursor.fetchone() is not None
        if not admin_exists:
            admin_password = hashlib.md5("administrator".encode()).hexdigest()
            admin_password_hash = hashlib.md5(admin_password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", admin_password_hash))
            conn.commit()  
        else:
            admin_password = hashlib.md5("administrator".encode()).hexdigest()
            admin_password_hash = hashlib.md5(admin_password.encode()).hexdigest()
            cursor.execute("UPDATE users SET password = ? WHERE username = ?", (admin_password_hash, "admin"))
            conn.commit()  

    print("初始化完成")

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # User 登录系统
    user = User("", "")
    logged_in_username = ""
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=====================================")
        print("           个人日记系统")
        print("=====================================")
        
        if user.is_logged_in:
            print(f"当前登录用户：{logged_in_username}")
            print("1. 写日记")
            print("2. 读日记")
            print("3. 查看所有日记")
            print("4. 退出登录")
        else:
            print("1. 登录")
            print("2. 注册")
            print("3. 退出程序")
        
        option = input("请选择操作：")
        
        if user.is_logged_in:
            # 已登录状态
            if option == "1":
                # 写日记
                print("\n写日记")
                print("请输入日记内容（按Ctrl+C结束输入）：")
                content = []
                try:
                    while True:
                        line = input()
                        content.append(line + "\n")
                except KeyboardInterrupt:
                    pass
                
                if content:
                    user.diary_manager.write_diary(logged_in_username, content)
                else:
                    print("日记内容不能为空")
                input("按回车继续...")
                
            elif option == "2":
                # 读日记
                print("\n读日记")
                user.diary_manager.read_diary(logged_in_username)
                input("按回车继续...")
                
            elif option == "3":
                # 查看所有日记
                print("\n查看所有日记")
                diary_files = []
                for file in os.listdir("diaries"):
                    if file.startswith(logged_in_username) and file.endswith(".txt") and "_" in file:
                        diary_files.append(file)
                
                if diary_files:
                    print(f"{logged_in_username} 的所有日记：")
                    for i, file in enumerate(diary_files, 1):
                        print(f"{i}. {file}")
                    
                    # 选择查看某个日记
                    try:
                        choice = int(input("请输入要查看的日记编号："))
                        if 1 <= choice <= len(diary_files):
                            file_path = os.path.join("diaries", diary_files[choice-1])
                            print(f"\n日记内容 ({diary_files[choice-1]}):")
                            with open(file_path, "r", encoding="utf-8") as f:
                                print(f.read())
                        else:
                            print("无效的编号")
                    except ValueError:
                        print("请输入有效的数字")
                else:
                    print("没有找到日记文件")
                input("按回车继续...")
                
            elif option == "4":
                # 退出登录
                print("退出登录成功")
                user.is_logged_in = False
                logged_in_username = ""
                time.sleep(1)
                
            else:
                print("无效选择")
                input("按回车继续...")
                
        else:
            # 未登录状态
            if option == "1":
                # 登录
                os.system('cls' if os.name == 'nt' else 'clear')
                logged_in_username = user.login(conn, cursor)
                if logged_in_username:
                    input("按回车继续...")
                else:
                    input("按回车继续...")
                    
            elif option == "2":
                # 注册
                os.system('cls' if os.name == 'nt' else 'clear')
                user.register(conn, cursor)
                input("按回车继续...")
                
            elif option == "3":
                # 退出程序
                print("退出程序")
                conn.close()
                exit()
                
            else:
                print("无效选择")
                input("按回车继续...")
    
    # 关闭数据库连接
    conn.close()