@echo off
chcp 65001 > nul
cls

REM Проверяем наличие установленного Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не обнаружен. Установите Python и повторите попытку.
    exit /b 1
)

REM Устанавливаем необходимые библиотеки Python
echo Библиотеки проверяются...
pip show colorama >nul 2>&1
if %errorlevel% neq 0 (
    echo Устанавливается библиотека colorama...
    pip install colorama
)

pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Устанавливается библиотека pyinstaller...
    pip install pyinstaller
)

echo Установка завершена.

REM Запрашиваем путь установки от пользователя
set /p installPath=Введите путь для установки программы: 

REM Создаем директорию установки, если ее не существует
if not exist "%installPath%" mkdir "%installPath%"

REM Копируем файлы программы в указанную директорию
echo Копирование файлов в %installPath%...
xcopy /s /y "путь_к_вашим_файлам" "%installPath%"

echo Программа успешно установлена в %installPath%
pause
