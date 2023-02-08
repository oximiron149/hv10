def read_last(lines, file):
    if lines > 0:
        with open(file, encoding="utf 8") as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('число строк должно быть положительным')

#read_last(-3, "artickle.txt")
def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_lenth = len(max(words, key=len))
        sought_words = []
        for i in words:
            if len(i) == max_lenth:
                sought_words.append(i)
        return sought_words
print(longest_words('artickle.txt'))