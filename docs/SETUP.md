# TrippiTroppi - Руководство по установке

## Предварительные требования

### Backend
- Python 3.11 или выше
- PostgreSQL 15 или выше
- Redis (опционально, для кэширования)
- pip или poetry

### Frontend
- Flutter SDK 3.16 или выше
- Dart SDK 3.2 или выше
- Android Studio (для Android разработки)
- Xcode (для iOS разработки, только macOS)

### Общее
- Git
- Docker и Docker Compose (опционально, для контейнеризации)

---

## Установка Backend

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-org/trippi-troppi.git
cd trippi-troppi
```

### 2. Настройка Python окружения

```bash
cd backend

# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# На Linux/Mac:
source venv/bin/activate
# На Windows:
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

### 3. Настройка базы данных

#### Установка PostgreSQL

**macOS:**
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install postgresql-15
sudo systemctl start postgresql
```

**Windows:**
Скачайте и установите с [официального сайта](https://www.postgresql.org/download/windows/)

#### Создание базы данных

```bash
# Войдите в PostgreSQL
psql postgres

# Создайте пользователя и базу данных
CREATE USER trippitroppi_user WITH PASSWORD 'your_password';
CREATE DATABASE trippitroppi OWNER trippitroppi_user;
GRANT ALL PRIVILEGES ON DATABASE trippitroppi TO trippitroppi_user;
\q
```

### 4. Конфигурация окружения

Скопируйте файл с примером переменных окружения:

```bash
cp .env.example .env
```

Отредактируйте `.env` файл:

```env
# Database
DATABASE_URL=postgresql://trippitroppi_user:your_password@localhost:5432/trippitroppi

# API Keys
YANDEX_MAPS_API_KEY=your_yandex_api_key
OPENTRIPMAP_API_KEY=your_opentripmap_api_key
OPENAI_API_KEY=your_openai_api_key

# Security
SECRET_KEY=your-secret-key-generate-random
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Получение API ключей

**Yandex Maps API:**
1. Зарегистрируйтесь на https://developer.tech.yandex.ru/
2. Создайте новый проект
3. Получите API ключ для Maps API

**OpenTripMap API:**
1. Зарегистрируйтесь на https://opentripmap.io/register
2. Получите бесплатный API ключ

**OpenAI API:**
1. Зарегистрируйтесь на https://platform.openai.com/
2. Создайте API ключ в настройках

### 5. Применение миграций

```bash
# Применить миграции базы данных
alembic upgrade head
```

### 6. Запуск backend сервера

```bash
# Development режим с auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Или используйте Makefile
make backend
```

Backend будет доступен на: http://localhost:8000

API документация (Swagger): http://localhost:8000/docs

---

## Установка Frontend

### 1. Установка Flutter

**macOS:**
```bash
# Используя Homebrew
brew install --cask flutter

# Или скачайте с официального сайта
# https://docs.flutter.dev/get-started/install/macos
```

**Linux:**
```bash
# Скачайте Flutter SDK
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.16.0-stable.tar.xz

# Распакуйте
tar xf flutter_linux_3.16.0-stable.tar.xz

# Добавьте в PATH
export PATH="$PATH:`pwd`/flutter/bin"
```

**Windows:**
Скачайте и установите с [официального сайта](https://docs.flutter.dev/get-started/install/windows)

### 2. Проверка Flutter

```bash
flutter doctor
```

Убедитесь, что все проверки пройдены успешно. Установите недостающие компоненты.

### 3. Настройка проекта

```bash
cd frontend

# Получение зависимостей
flutter pub get
```

### 4. Конфигурация

Создайте файл конфигурации `lib/core/config.dart`:

```dart
class Config {
  static const String apiBaseUrl = 'http://localhost:8000/api/v1';
  static const String yandexMapsApiKey = 'your_yandex_maps_key';
}
```

### 5. Запуск приложения

```bash
# Показать доступные устройства
flutter devices

# Запустить на конкретном устройстве
flutter run -d <device_id>

# Или просто
flutter run

# Или используйте Makefile
make frontend
```

---

## Использование Docker (Альтернативный способ)

### 1. Установка Docker

Установите Docker и Docker Compose с [официального сайта](https://docs.docker.com/get-docker/)

### 2. Запуск с Docker Compose

```bash
# Из корневой директории проекта
docker-compose up -d

# Или используйте Makefile
make docker-up
```

Это запустит:
- PostgreSQL на порту 5432
- Redis на порту 6379
- Backend API на порту 8000

### 3. Просмотр логов

```bash
docker-compose logs -f

# Или
make docker-logs
```

### 4. Остановка контейнеров

```bash
docker-compose down

# Или
make docker-down
```

---

## Создание тестовых данных

После запуска backend можете создать тестовые данные:

```bash
cd backend
source venv/bin/activate
python scripts/seed_data.py
```

---

## Проверка установки

### Backend

```bash
# Проверка health endpoint
curl http://localhost:8000/health

# Ожидаемый ответ
{"status":"healthy"}
```

### Frontend

Приложение должно запуститься на эмуляторе или устройстве без ошибок.

---

## Разработка

### Backend

```bash
# Запуск с auto-reload
make backend

# Запуск тестов
make test

# Линтинг
make lint

# Создание миграции
make db-migrate message="your migration message"

# Применение миграций
make db-upgrade
```

### Frontend

```bash
# Запуск в debug режиме
flutter run

# Запуск тестов
flutter test

# Анализ кода
flutter analyze

# Форматирование
flutter format .
```

---

## Troubleshooting

### Backend не запускается

1. Проверьте, что PostgreSQL запущен:
```bash
pg_isready -h localhost -p 5432
```

2. Проверьте DATABASE_URL в .env файле

3. Проверьте логи:
```bash
tail -f logs/app.log
```

### Frontend не запускается

1. Очистите кеш Flutter:
```bash
flutter clean
flutter pub get
```

2. Проверьте flutter doctor:
```bash
flutter doctor -v
```

3. Убедитесь, что эмулятор/устройство запущено:
```bash
flutter devices
```

### Проблемы с миграциями

```bash
# Откатить все миграции
alembic downgrade base

# Применить заново
alembic upgrade head
```

---

## Дополнительные ресурсы

- [FastAPI документация](https://fastapi.tiangolo.com/)
- [Flutter документация](https://docs.flutter.dev/)
- [PostgreSQL документация](https://www.postgresql.org/docs/)
- [SQLAlchemy документация](https://docs.sqlalchemy.org/)

---

## Поддержка

Если у вас возникли проблемы:

1. Проверьте [Issues](https://github.com/your-org/trippi-troppi/issues)
2. Создайте новый Issue
3. Свяжитесь с командой: support@trippitroppi.com

