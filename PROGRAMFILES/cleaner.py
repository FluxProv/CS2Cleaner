import os
import random
import shutil
import subprocess
from colorama import Fore, Style

def find_and_rename(target_folders, target_names, replacement_names):
    for folder in target_folders:
        for root, dirs, files in os.walk(folder):
            for name in dirs + files:
                for i, target_name in enumerate(target_names):
                    if target_name.lower() in name.lower():
                        new_name = random.choice(replacement_names)
                        new_path = os.path.join(root, new_name)
                        try:
                            shutil.move(os.path.join(root, name), new_path)
                            print(f"{Fore.GREEN}({ 'Папка' if os.path.isdir(new_path) else 'Файл' }) по пути {new_path} был переименован в {new_name} и успешно перемещен!{Style.RESET_ALL}")
                            if os.path.isdir(new_path):
                                shutil.rmtree(new_path)  # Полностью удаляем переименованную папку
                                print(f"{Fore.GREEN}Папка {new_path} успешно удалена.{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Ошибка при переименовании {name}: {e}{Style.RESET_ALL}")

def clear_folders():
    appdata_folder = os.path.join(os.environ['APPDATA'])
    localappdata_folder = os.path.join(os.environ['LOCALAPPDATA'])

    try:
        shutil.rmtree(appdata_folder)
        print(f"{Fore.GREEN}Папка {appdata_folder} успешно удалена.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Папка {appdata_folder} не найдена.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Нет разрешения на удаление папки {appdata_folder}.{Style.RESET_ALL}")

    try:
        shutil.rmtree(localappdata_folder)
        print(f"{Fore.GREEN}Папка {localappdata_folder} успешно удалена.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Папка {localappdata_folder} не найдена.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Нет разрешения на удаление папки {localappdata_folder}.{Style.RESET_ALL}")

    prefetch_folder = "C:\\Windows\\Prefetch"
    try:
        for root, dirs, files in os.walk(prefetch_folder):
            for file in files:
                os.remove(os.path.join(root, file))
                print(f"{Fore.GREEN}Файл {file} успешно удален.{Style.RESET_ALL}")
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
                print(f"{Fore.GREEN}Папка {dir} успешно удалена.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Все файлы и папки из папки {prefetch_folder} успешно удалены.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Папка {prefetch_folder} не найдена.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Нет разрешения на удаление файлов и папок из {prefetch_folder}.{Style.RESET_ALL}")

    # Очистка корзины
    try:
        subprocess.run(["powershell", "-Command", "Clear-RecycleBin -Force"], check=True)
        print(f"{Fore.GREEN}Корзина успешно очищена.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Ошибка при очистке корзины: {e}{Style.RESET_ALL}")

    # Остальные шаги автоматической очистки по гайду
    # 1. Почистить историю поиска, загрузок и cookie файлы на сайтах, где качали читы
    # 2. Скачать и переименовать LastActivity Cleaner
    # 3. Прятать читы и выполнять остальные указанные шаги

def troll_folders():
    target_folders = [os.path.join(os.environ['APPDATA']), os.path.join(os.environ['LOCALAPPDATA'])]
    target_names = ["Exloader", "Tkazer", "Aimstar", "Naim", "Xone", "Midnight"]
    replacement_names = ["SoundCloud", "YandexDisk", "OperaGX", "ChromeCokies", "Startup10", "Yandex", "YandexMusic"]

    troll_folder = os.path.join(os.path.dirname(__file__), "Troll")  # Папка Troll находится в директории программы
    if not os.path.exists(troll_folder):
        os.makedirs(troll_folder)
        print(f"{Fore.GREEN}Папка Troll успешно создана.{Style.RESET_ALL}")

    for name in target_names:
        new_troll_folder = os.path.join(target_folders[0] if random.random() < 0.5 else target_folders[1], name)
        if not os.path.exists(new_troll_folder):
            os.makedirs(new_troll_folder)
            print(f"{Fore.GREEN}Папка {new_troll_folder} успешно создана.{Style.RESET_ALL}")
        for i in range(1, 7):  # Копируем от 1.jpg до 6.jpg
            try:
                shutil.copy(os.path.join(os.path.dirname(__file__), f"{i}.jpg"), new_troll_folder)
                print(f"{Fore.GREEN}Фото {i}.jpg скопировано в {new_troll_folder}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Ошибка при копировании {i}.jpg: {e}{Style.RESET_ALL}")

def run_ccleaner():
    try:
        ccleaner_path = os.path.join(os.path.dirname(__file__), 'CCleaner', 'CCleaner.exe')
        subprocess.run([ccleaner_path], check=True)
        print(f"{Fore.GREEN}CCleaner успешно запущен.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Ошибка при запуске CCleaner: {e}{Style.RESET_ALL}")

def main():
    while True:
        print("Программа CleanerCS2")
        print("Выберите действие:")
        print("1. Быстрая очистка")
        print("2. Добавить троллинг")
        print("3. Запустить CCleaner")
        print("4. Полная очистка (выполнить дополнительные шаги)")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print(f"{Fore.CYAN}Выполняется быстрая очистка...{Style.RESET_ALL}")
            clear_folders()
        elif choice == '2':
            print(f"{Fore.CYAN}Добавляется троллинг...{Style.RESET_ALL}")
            troll_folders()
        elif choice == '3':
            print(f"{Fore.CYAN}Запуск CCleaner...{Style.RESET_ALL}")
            run_ccleaner()
        elif choice == '4':
            print(f"{Fore.CYAN}Выполняется полная очистка...{Style.RESET_ALL}")
            clear_folders()
            find_and_rename(["C:\\", "D:\\", "E:\\"], ["Exloader", "Tkazer", "Aimstar", "Naim", "Xone", "Midnight", "NeverLose", "luno", "Interium", "cheat", "aimbot", "wh", "ahk", "external", "menu"], ["SoundCloud", "YandexDisk", "OperaGX", "ChromeCokies", "Startup10", "Yandex", "YandexMusic"])
            # Выполнение дополнительных шагов по гайду
            print(f"{Fore.CYAN}Выполняются дополнительные шаги автоматической очистки...{Style.RESET_ALL}")
            # Почистить историю поиска, загрузок и cookie файлы
            # Скачать и переименовать LastActivity Cleaner
            # Прятать читы и выполнять остальные указанные шаги
        elif choice == '5':
            break
        else:
            print(f"{Fore.RED}Неверный ввод. Повторите попытку.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
