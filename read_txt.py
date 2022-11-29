# 读取txt文件
def read_txt(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)
        new_l = []
        for line in lines:
            l = line.rstrip('\n').split()
            print(l)
            new_l.append(line)
        print(new_l)
    f.close()
    # return new_l


if __name__ == '__main__':
    read_txt('./merge_new7.txt')
