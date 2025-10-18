# TrippiTroppi — Персональный гид по путешествиям

Мобильное приложение с ИИ-агентом для формирования персонализированных туристических маршрутов по городам России.

## 🚀 Технологический стек

- **Frontend**: Flutter
- **Backend**: FastAPI (Python)
- **База данных**: PostgreSQL
- **API интеграции**: Yandex Maps API, OpenTripMap API

## 📁 Структура проекта

```
trippi-troppi/
├── backend/          # FastAPI backend
├── frontend/         # Flutter mobile app
├── docs/            # Документация проекта
└── README.md
```

## 🛠️ Быстрый старт

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
flutter pub get
flutter run
```

## 📖 Документация

Полная документация проекта находится в папке `docs/`:
- [Product Requirements Document (PRD)](docs/PRD.md)

## 🎯 Основные функции MVP

- ИИ-агент для персонального подбора маршрутов
- Фильтры интересов (музеи, парки, еда, выставки)
- Динамическое редактирование маршрута
- Учет ограничений (время работы, билеты, транспорт)
- Автоматическая замена точек маршрута
- Карты и навигация
- Обмен маршрутами
- Геймификация (ачивки, баллы)

## 👥 Команда

- Product Manager: (заполните)
- Backend Developer: (заполните)
- Frontend Developer: (заполните)
- UI/UX Designer: (заполните)

## 📝 Лицензия

(заполните)

