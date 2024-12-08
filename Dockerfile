# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем системные зависимости для работы с SQLite
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем весь проект из папки python в контейнер
COPY python /app

# Указываем команду для запуска основного приложения
CMD ["python", "main.py"]
