def create_file_f1():
    with open('F1.txt', 'w', encoding='utf-8') as f1:
        line="a"
        while line != "":
            line = input("Введите строку (или пустую строку для завершения ввода): ")
            f1.write(line + '\n')


def copy_lines_to_f2(n1, n2):
    with open('F1.txt', 'r', encoding='utf-8') as f1, open('F2.txt', 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        for i in range(n1 - 1, n2):
                line = lines[i]
                if line.startswith('A'):
                    f2.write(line)


def count_words_in_f2():
    with open('F2.txt', 'r', encoding='utf-8') as f2:
        first_line = f2.readline()
        word_count = len(first_line.split())
        return word_count



create_file_f1()


n1 = int(input("Введите номер первой строки (N1): "))
n2 = int(input("Введите номер последней строки (N2): "))

copy_lines_to_f2(n1, n2)

word_count = count_words_in_f2()
print(f"Количество слов в первой строке файла F2: {word_count}")


