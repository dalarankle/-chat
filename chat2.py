
# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


# 整理對話紀錄
def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_picture_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_picture_count = 0
    person = None
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':     
            for i in s[2:]:
                if i == '貼圖':
                    allen_sticker_count += 1
                elif i == '圖片':
                    allen_picture_count += 1
                else:
                    allen_word_count += len(i)
        elif name == 'Viki':
            for i in s[2:]:
                if i == '貼圖':
                    viki_sticker_count += 1
                elif i == '圖片':
                    viki_picture_count += 1
                else:
                    viki_word_count += len(i)

    print('Allen字數', allen_word_count, '個字；使用了', allen_sticker_count, '個貼圖；傳送了', allen_picture_count, '個圖片')
    print('Viki字數', viki_word_count, '個字；使用了', viki_sticker_count, '個貼圖；傳送了', viki_picture_count, '個圖片')


# 存入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


# main function
def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    # write_file('line-output.txt', lines)
            

main()