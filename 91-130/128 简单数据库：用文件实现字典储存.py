# 简单数据库：用文件实现字典储存

import os
import sqlite3

if __name__ == '__main__':
    
    student = {
    "姓名": "梓潼",
    "年龄": 18,
    "性别": "男",
    "班级": "25级3班"
    }

    # 连接到数据库（如果不存在，会自动创建）
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    # 创建表格（如果不存在）
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        class TEXT
    )
    ''')

    # 插入数据
    cursor.execute('''
    INSERT INTO students (name, age, gender, class)
    VALUES (?, ?, ?, ?)
    ''', (student["姓名"], student["年龄"], student["性别"], student["班级"]))
    conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()