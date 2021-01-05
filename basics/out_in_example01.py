import re
# Example_01

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]', ' ', text)
    text = text.lower()
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    print(word_cnt)

    # 词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    print(sorted_word_cnt)
    return sorted_word_cnt

with open('out_in_exp.txt', 'r') as i:
    text = i.read()

word_and_freq = parse(text)
print(type(word_and_freq))
with open('out.txt', 'w') as o:
    for word, freq in word_and_freq:
        o.write('{} {}\n'.format(word, freq))