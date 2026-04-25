import re
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Ошибка: укажите файл. Пример: python preprocessor.py test.cpp")
        return

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Ошибка: файл {filename} не найден")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.count("/*") > content.count("*/"):
        print("Ошибка: Обнаружен незакрытый многострочный комментарий (/*)!")
        return

    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    content = re.sub(r'//.*', '', content)
    
    lines = content.splitlines()
    processed_count = 0

    for line in lines:
        trimmed = line.strip()
        
        if trimmed:
            print(trimmed)
            processed_count += 1

    if processed_count > 0:
        print("Ошибок не выявлено.")
    else:
        print("После очистки файл пуст.")

if __name__ == "__main__":
    main()