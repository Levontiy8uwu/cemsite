# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменные окружения для Python (для логирования и вывода в консоль)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию контейнера
WORKDIR /betsite

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . /betsite/