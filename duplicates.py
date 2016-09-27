import hashlib
import os
import sys

files = {}
if len(sys.argv) == 1:
    print('Вы не указали адресс папки')
    sys.exit(1)
os.chdir(sys.argv[1])


def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def check_copies():
    for i in os.walk(os.getcwd(), topdown=True, onerror=None, followlinks=False):
        os.chdir(i[0])
        for k in i[2]:
            Hash = get_hash_md5(k)
            if not (Hash in files):
                files[Hash] = [i[0]+'/'+k]
            else:
                files[Hash].append(i[0]+'/'+k)

if __name__ == '__main__:
check_copies()
    for i in files:
        if len(files[i]) > 1:
            print("Для файла", files[i][0], "найдены слудующие копии:")
            for k in files[i][1:]:
                print(k)
