try:
    with open("Git\\text_git.txt", "r") as file:
        readlines = file.readlines()
        print(readlines)
except FileNotFoundError:
    print("Файл не найден или его не возможно открыть")
except:
    print("Ошибка")
finally:
    print(file.closed)
