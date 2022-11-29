import re
from zhon.hanzi import punctuation


def delete_chinese(text):
    text = re.sub('[\u4e00-\u9fa5]', '', text)
    text = re.sub('[{}]'.format(punctuation), "", text)
    return text


def read_txt(filename):
    with open(filename, encoding='utf-8') as f:
        with open('new.txt', 'w', encoding='utf-8') as n:
            lines = f.readlines()
            # print(lines)
            new_l = []
            for line in lines:
                l = line.rstrip('\n')
                # print(line)
                # print(l)
                text = re.sub('[\u4e00-\u9fa5]', '', l)
                # text = re.sub('[{}]'.format(punctuation), "", text)
                text = re.sub('[：]', '', text)
                text = re.sub('[，”“、。；【】！？——]', '', text)
                text = re.sub('[①②③④⑤⑥]', '', text)
                n.write('{}\n'.format(text))
                # print(text)
                # new_l.append(text)
            # print(new_l)
        n.close()

    f.close()


if __name__ == '__main__':
    read_txt('./merge_new7.txt')
