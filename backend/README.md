# TrippiTroppi Backend

FastAPI backend для приложения TrippiTroppi.

## 🚀 Установка и запуск

### Требования

- Python 3.11+
- PostgreSQL 15+
- Redis (опционально, для кэширования)

### Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Настройка окружения

1. Скопируйте `.env.example` в `.env`:
```bash
cp .env.example .env
```

2. Заполните необходимые переменные окружения в `.env`

### Создание базы данных

```bash
# Запустите PostgreSQL и создайте базу данных
createdb trippitroppi

# Примените миграции
alembic upgrade head
```

### Запуск сервера

```bash
# Development mode
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

API будет доступен по адресу: `http://localhost:8000`

Документация API (Swagger): `http://localhost:8000/docs`

ReDoc документация: `http://localhost:8000/redoc`

## 📁 Структура проекта

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Точка входа приложения
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── routes/         # API endpoints
│   │           ├── auth.py     # Аутентификация
│   │           ├── users.py    # Пользователи
│   │           ├── routes.py   # Маршруты
│   │           ├── locations.py # Локации
│   │           └── recommendations.py # Рекомендации
│   ├── core/
│   │   ├── config.py           # Конфигурация приложения
│   │   └── security.py         # JWT, хеширование паролей
│   ├── db/
│   │   ├── base.py             # Base model для SQLAlchemy
│   │   └── session.py          # Database session
│   ├── models/                 # SQLAlchemy ORM модели
│   │   ├── user.py
│   │   ├── route.py
│   │   ├── location.py
│   │   └── achievement.py
│   ├── schemas/                # Pydantic схемы (DTO)
│   │   ├── user.py
│   │   ├── route.py
│   │   └── location.py
│   └── services/               # Бизнес-логика
│       ├── ai_agent.py         # AI агент для маршрутов
│       ├── maps_service.py     # Интеграция с картами
│       ├── recommendations.py  # Рекомендации
│       └── gamification.py     # Геймификация
├── alembic/                    # Миграции базы данных
├── tests/                      # Тесты
├── requirements.txt
├── .env.example
└── README.md
```

## 🔑 API Endpoints

### Аутентификация
- `POST /api/v1/auth/register` - Регистрация
- `POST /api/v1/auth/login` - Вход
- `POST /api/v1/auth/refresh` - Обновление токена

### Пользователи
- `GET /api/v1/users/me` - Текущий пользователь
- `PUT /api/v1/users/me` - Обновить профиль
- `GET /api/v1/users/{id}` - Получить пользователя

### Маршруты
- `POST /api/v1/routes/generate` - Сгенерировать маршрут (AI)
- `GET /api/v1/routes` - Список маршрутов
- `GET /api/v1/routes/{id}` - Получить маршрут
- `PUT /api/v1/routes/{id}` - Обновить маршрут
- `DELETE /api/v1/routes/{id}` - Удалить маршрут

### Локации
- `GET /api/v1/locations/search` - Поиск локаций
- `GET /api/v1/locations/{id}` - Информация о локации

### Рекомендации
- `GET /api/v1/recommendations` - Получить рекомендации

## 🧪 Тестирование

```bash
pytest tests/
```

## 📦 Миграции базы данных

```bash
# Создать миграцию
alembic revision --autogenerate -m "description"

# Применить миграции
alembic upgrade head

# Откатить миграцию
alembic downgrade -1
```

## 🔧 Разработка

### Code Style

Проект использует:
- `black` для форматирования
- `isort` для сортировки импортов
- `flake8` для линтинга

```bash
black app/
isort app/
flake8 app/
```

