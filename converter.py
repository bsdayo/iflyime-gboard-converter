# -*- coding: utf-8 -*-

import sys
from xpinyin import Pinyin

INPUT_FILEPATH = sys.argv[1] if len(sys.argv) >= 2 else 'user_dict.txt'
OUTPUT_FILEPATH = sys.argv[2] if len(sys.argv) >= 3 else 'dictionary.txt'

p = Pinyin()

if __name__ == '__main__':
    try:
        input_f = open(INPUT_FILEPATH, encoding='utf-8')
        output_f = open(OUTPUT_FILEPATH, 'w', encoding='utf-8')

        output_f.write("# Gboard Dictionary version:1\n")

        for line in input_f.readlines():
            if line.startswith('#') or line == '\n':
                continue

            phrase = line.split(' ')[0]
            pinyin = p.get_pinyin(phrase, '')

            output_f.write(f"{pinyin}\t{phrase}\tzh-CN\n")

        input_f.close()
        output_f.close()

    except FileNotFoundError:
        print(f"文件不存在！")
        sys.exit(0)
