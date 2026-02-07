# 文本加密储存：将加密的文本储存到文件冲

import hashlib

if __name__ == '__main__':

    text = input("please input test which you want to encrypt: ")

    # 对文本进行加密
    encrypted_text = hashlib.sha256(hashlib.sha256(text.encode()).hexdigest().encode()).hexdigest()

    # 将加密后的文本储存到文件中
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)