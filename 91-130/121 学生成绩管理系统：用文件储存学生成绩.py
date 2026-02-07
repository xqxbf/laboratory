# 学生成绩管理系统：用文件储存学生成绩

import sqlite3
from typing import List, Dict, Optional
import os

class StudentGradeManager:
    def __init__(self, db_path: str = "grades.db"):
        """初始化数据库连接并创建表（若不存在）"""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_table()

    def _init_table(self):
        """创建学生成绩表"""
        sql = """
        CREATE TABLE IF NOT EXISTS student_grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            chinese REAL,
            math REAL,
            english REAL,
            physics REAL,
            chemistry REAL,
            biology REAL,
            total REAL,
            average REAL
        );
        """
        self.conn.execute(sql)
        self.conn.commit()

    def add_or_update_student(self, student_id: str, name: str, **scores) -> bool:
        """添加或更新学生成绩
        
        :param student_id: 学号
        :param name: 姓名
        :param scores: 各科成绩（键为科目名，值为成绩）
        :return: 是否成功
        """
        total = sum(scores.values())
        average = total / len(scores) if scores else 0
        sql = """
        INSERT INTO student_grades(student_id, name, chinese, math, english, physics, chemistry, biology, total, average)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
            name=excluded.name,
            chinese=excluded.chinese,
            math=excluded.math,
            english=excluded.english,
            physics=excluded.physics,
            chemistry=excluded.chemistry,
            biology=excluded.biology,
            total=excluded.total,
            average=excluded.average;
        """
        try:
            self.conn.execute(sql, (
                student_id, name,
                scores.get("chinese"), scores.get("math"), scores.get("english"),
                scores.get("physics"), scores.get("chemistry"), scores.get("biology"),
                total, average
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print("添加/更新失败:", e)
            return False

    def get_student(self, student_id: str) -> Optional[Dict]:
        """根据学号查询学生成绩
        
        :param student_id: 学号
        :return: 学生成绩字典（若不存在则返回None）
        """
        sql = "SELECT * FROM student_grades WHERE student_id = ?"
        cursor = self.conn.execute(sql, (student_id,))
        row = cursor.fetchone()
        if not row:
            return None
        keys = ["id", "student_id", "name", "chinese", "math", "english", "physics", "chemistry", "biology", "total", "average"]
        return dict(zip(keys, row))

    def list_all_students(self) -> List[Dict]:
        """列出所有学生成绩
        
        :return: 学生成绩列表（按总分降序排列）
        """
        sql = "SELECT * FROM student_grades ORDER BY total DESC"
        cursor = self.conn.execute(sql)
        keys = ["id", "student_id", "name", "chinese", "math", "english", "physics", "chemistry", "biology", "total", "average"]
        return [dict(zip(keys, row)) for row in cursor.fetchall()]

    def delete_student(self, student_id: str) -> bool:
        """删除学生记录
        
        :param student_id: 学号
        :return: 是否成功
        """ 
        sql = "DELETE FROM student_grades WHERE student_id = ?"
        try:
            cursor = self.conn.execute(sql, (student_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("删除失败:", e)
            return False

    def get_ranking(self, student_id: str) -> Optional[int]:
        """获取学生总分排名
        
        :param student_id: 学号
        :return: 排名（若不存在则返回None）
        """
        sql = """
        SELECT student_id, RANK() OVER (ORDER BY total DESC) AS rank
        FROM student_grades
        """
        cursor = self.conn.execute(sql)
        for row in cursor.fetchall():
            if row[0] == student_id:
                return row[1]
        return None

    def close(self):
        """关闭数据库连接
        
        :return: None
        """
        try:
            self.conn.close()
        except Exception as e:
            print("关闭数据库连接失败:", e)

def clean_screen_with_title():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')
        # 添加问候语
    print("=====================================")
    print("欢迎使用学生成绩管理系统！")
    print("=====================================")

# 主程序
if __name__ == "__main__":
    
    manager = StudentGradeManager()
    
    while True:

        clean_screen_with_title()

        # 显示选项菜单
        print("\n请选择操作：")
        print("1. 添加/更新学生成绩")
        print("2. 查询学生成绩")
        print("3. 列出所有学生成绩")
        print("4. 删除学生记录")
        print("5. 获取学生排名")
        print("0. 退出系统")
        
        choice = input("请输入选项编号：").strip()

        clean_screen_with_title()
        
        if choice == "0":
            # 退出系统
            manager.close()
            clean_screen_with_title()
            print("感谢使用学生成绩管理系统，再见！")
            break
        
        elif choice == "1":
            # 添加/更新学生成绩
            student_id = input("请输入学号：").strip()
            name = input("请输入姓名：").strip()
            
            # 输入各科成绩
            scores = {}
            subjects = ["chinese", "math", "english", "physics", "chemistry", "biology"]
            subject_names = {"chinese": "语文", "math": "数学", "english": "英语", "physics": "物理", "chemistry": "化学", "biology": "生物"}
            
            for subj in subjects:
                score_input = input(f"请输入{subject_names[subj]}成绩（按回车跳过）：").strip()
                if score_input:
                    try:
                        scores[subj] = float(score_input)
                    except ValueError:
                        print(f"{subject_names[subj]}成绩输入无效，已跳过")
            
            if student_id and name:
                success = manager.add_or_update_student(student_id, name, **scores)

                if success:
                    print("添加/更新成功！")
                else:
                    print("添加/更新失败！")
            else:
                print("学号和姓名不能为空！")
        
        elif choice == "2":
            # 查询学生成绩
            student_id = input("请输入要查询的学号：").strip()
            student = manager.get_student(student_id)

            if student:
                print("\n学生信息：")
                print(f"学号：{student['student_id']}")
                print(f"姓名：{student['name']}")
                print(f"语文：{student['chinese']}")
                print(f"数学：{student['math']}")
                print(f"英语：{student['english']}")
                print(f"物理：{student['physics']}")
                print(f"化学：{student['chemistry']}")
                print(f"生物：{student['biology']}")
                print(f"总分：{student['total']}")
                print(f"平均分：{student['average']}")
            else:
                print("未找到该学生信息！")
        
        elif choice == "3":
            # 列出所有学生成绩
            students = manager.list_all_students()

            if students:
                print("\n所有学生成绩（按总分降序）：")
                print("=====================================")
                print(f"{'学号':<10} {'姓名':<10} {'总分':<10} {'平均分':<10}")
                print("=====================================")
                for student in students:
                    print(f"{student['student_id']:<10} {student['name']:<10} {student['total']:<10.1f} {student['average']:<10.1f}")
                print("=====================================")
            else:
                print("暂无学生信息！")
        
        elif choice == "4":
            # 删除学生记录
            student_id = input("请输入要删除的学号：").strip()
            success = manager.delete_student(student_id)

            if success:
                print("删除成功！")
            else:
                print("删除失败，未找到该学生！")
        
        elif choice == "5":
            # 获取学生排名
            student_id = input("请输入要查询排名的学号：").strip()
            ranking = manager.get_ranking(student_id)

            if ranking:
                print(f"该学生的排名是：第 {ranking} 名")
            else:
                print("未找到该学生信息！")
        
        else:
            print("无效的选项，请重新输入！")

        input("按任意键继续...")
    
    manager.close()
