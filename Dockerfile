# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /scripts

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install watchgod

# Копируем всё приложение
COPY . .

# Открываем порт
EXPOSE 8000

# Команда запуска сервера
CMD ["uvicorn", "scripts.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]