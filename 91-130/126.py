import re
from collections import defaultdict, Counter
from datetime import datetime
import json
import argparse

class LogAnalyzer:
    """
    通用日志分析器
    支持按正则提取、统计、聚合、时间窗口分析
    """

    def __init__(self, log_path, encoding='utf-8'):
        self.log_path = log_path
        self.encoding = encoding
        self.lines = []
        self._load()

    def _load(self):
        """读取日志到内存"""
        with open(self.log_path, 'r', encoding=self.encoding, errors='ignore') as f:
            self.lines = f.readlines()

    def extract(self, pattern, group_names=None):
        """
        按正则提取日志
        :param pattern: 正则表达式，支持命名分组 (?P<name>...)
        :param group_names: 若给出，则只返回这些分组
        :return: 提取结果列表，每项为 dict
        """
        regex = re.compile(pattern)
        results = []
        for line in self.lines:
            m = regex.search(line)
            if m:
                if group_names:
                    results.append({k: m.group(k) for k in group_names if k in m.groupdict()})
                else:
                    results.append(m.groupdict())
        return results

    def count(self, key_func):
        """
        按 key_func 统计出现次数
        :param key_func: 接收单行日志，返回统计键
        :return: Counter
        """
        counter = Counter()
        for line in self.lines:
            k = key_func(line)
            if k is not None:
                counter[k] += 1
        return counter

    def time_window(self, time_pattern, time_fmt, window_seconds=300):
        """
        按时间窗口聚合日志条数
        :param time_pattern: 提取时间字符串的正则（必须含命名分组 time）
        :param time_fmt: 时间字符串格式，如 '%Y-%m-%d %H:%M:%S'
        :param window_seconds: 窗口秒数
        :return: dict，key 为窗口起始时间戳，value 为计数
        """
        regex = re.compile(time_pattern)
        buckets = defaultdict(int)
        for line in self.lines:
            m = regex.search(line)
            if not m:
                continue
            time_str = m.group('time')
            try:
                dt = datetime.strptime(time_str, time_fmt)
                ts = int(dt.timestamp())
                bucket = ts // window_seconds * window_seconds
                buckets[bucket] += 1
            except Exception:
                continue
        return dict(buckets)

    def top(self, key_func, top_n=10):
        """
        获取出现频率最高的 top_n 项
        :param key_func: 同 count
        :return: list[tuple(key, count)]
        """
        return self.count(key_func).most_common(top_n)

    def save_json(self, data, out_path, ensure_ascii=False, indent=2):
        """将分析结果保存为 JSON"""
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent)

    def report(self, pattern=None, time_pattern=None, time_fmt=None, window=300, top_n=10):
        """
        一键生成常用报告
        """
        report = {}
        if pattern:
            report['extract'] = self.extract(pattern)
        if time_pattern and time_fmt:
            report['time_window'] = self.time_window(time_pattern, time_fmt, window)
        report['total_lines'] = len(self.lines)
        return report


def main():
    parser = argparse.ArgumentParser(description='日志分析器：分析日志文件提取信息')
    parser.add_argument('-l', '--log', help='日志文件路径')
    parser.add_argument('-p', '--pattern', help='提取正则（含命名分组）')
    parser.add_argument('-t', '--time_pattern', help='时间提取正则，需含(?P<time>...)')
    parser.add_argument('-f', '--time_fmt', help='时间格式，如 "%%Y-%%m-%%d %%H:%%M:%%S"')
    parser.add_argument('-w', '--window', type=int, default=300, help='时间窗口秒数，默认300')
    parser.add_argument('-o', '--output', help='输出JSON路径')
    args = parser.parse_args()

    if not args.log:
        parser.print_help()
        return

    analyzer = LogAnalyzer(args.log)
    rep = analyzer.report(
        pattern=args.pattern,
        time_pattern=args.time_pattern,
        time_fmt=args.time_fmt,
        window=args.window
    )
    
    if args.output:
        analyzer.save_json(rep, args.output)
        print(f'报告已保存至 {args.output}')
    else:
        print(json.dumps(rep, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
