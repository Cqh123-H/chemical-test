# 读取txt文件
def read_txt(filename):
    with open(filename, encoding='utf-8') as f:
        with open('new_04.txt', 'w', encoding='utf-8') as n:
            lines = f.readlines()
            new_l = []
            for line in lines:
                l = line.rstrip('\n')
                l = l.replace('=', '生成')
                l = l.replace('+', '和')
                # l = l.split('=')
                # gen = l[0].split('+')
                # print(gen)
                print(l)
                n.write('{}\n'.format(l))
    f.close()
    # return new_l


if __name__ == '__main__':
    read_txt('./new_02.txt')
