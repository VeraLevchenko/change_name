import os

if __name__ == '__main__':
    directory = "E:\Отрицательные\под индивидуальное домовладение"
    filelist = os.listdir(directory)

# -------------------------Меняем текст----------------------------------
    for i in range(0, len(filelist)):
        old_filename =f"{filelist[i]}"
        print("old_filename", old_filename)
        new_filename = f"{i}_{old_filename}"
        print("new_filename", new_filename)
        try:
            os.rename(f'{directory}\{old_filename}', f'{directory}\{new_filename}')
        except FileNotFoundError:
            print("Файл не найден")
        except PermissionError:
            print("Нет доступа для переименования файла")

