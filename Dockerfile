# Базовий образ Python 3.12
FROM python:3.12

# Змінні середовища
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Робоча директорія в контейнері
WORKDIR /app
COPY . /app/


# Встановлюємо системні залежності, необхідні для компіляції
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libtiff5-dev \
    tk-dev \
    tcl-dev \
    build-essential \
    libssl-dev \
    libbz2-dev \
    libsqlite3-dev \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо requirements.txt і встановлюємо Python-залежності
COPY requirements.txt .
# Remove backports.zoneinfo from requirements if Python >= 3.9

RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проєкт
COPY . .

# Відкриття порту
EXPOSE 8001

# Запуск Django-серверу
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]