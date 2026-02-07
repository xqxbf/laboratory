# 模拟数据库操作异常处理

import sqlite3
import contextlib

@contextlib.contextmanager
def db_connection(db_name="test.db"):
    """
    数据库连接上下文管理器
    :param db_name: 数据库文件名，默认 test.db
    :return: 数据库连接和游标
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        yield conn, cursor
    finally:    
        cursor.close()
        conn.close()

def db_error(e):
    """
    数据库错误处理函数
    :param e: 数据库错误对象
    :return: None
    """
    if e == sqlite3.IntegrityError:
        print("数据库完整性错误，可能是主键冲突或唯一约束违规")
    elif e == sqlite3.OperationalError:
        print("数据库操作错误，可能是表不存在或其他操作问题")
    elif e == sqlite3.ProgrammingError:
        print("数据库编程错误，可能是SQL语句错误或参数绑定问题")
    elif e == sqlite3.DatabaseError:
        print("数据库错误，可能是数据库文件损坏或其他问题")
    elif e == sqlite3.InterfaceError:
        print("数据库接口错误，可能是参数传递错误或其他接口问题")
    elif e == sqlite3.InternalError:
        print("数据库内部错误，可能是数据库引擎问题")
    else:
        print(f"未知数据库错误：{e}")

def __main__():
    """
    主函数，执行数据库操作
    :return: None
    """
    try:
        with db_connection() as (conn, cursor):
            """
            创建 users 表（如果不存在）
            :return: None
            """
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
            )
            conn.commit()
            cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
            conn.commit()
            cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
            conn.commit()
            """
            尝试查找信息
            :return: None
            """
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        db_error(e)

__main__()



