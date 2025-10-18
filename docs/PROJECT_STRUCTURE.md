# TrippiTroppi - Структура проекта

## Полная структура файлов и папок

```
trippi-troppi/
│
├── README.md                           # Основная документация проекта
├── .gitignore                          # Git ignore файл
├── docker-compose.yml                  # Docker Compose конфигурация
├── Makefile                            # Makefile с командами для разработки
│
├── docs/                               # Документация
│   ├── PRD.md                         # Product Requirements Document
│   ├── API.md                         # API документация
│   ├── DATABASE.md                    # Схема базы данных
│   ├── ARCHITECTURE.md                # Архитектура системы
│   ├── SETUP.md                       # Руководство по установке
│   └── PROJECT_STRUCTURE.md           # Структура проекта (этот файл)
│
├── backend/                           # Backend (FastAPI)
│   ├── README.md                      # Backend документация
│   ├── Dockerfile                     # Docker конфигурация
│   ├── requirements.txt               # Python зависимости
│   ├── .env.example                   # Пример переменных окружения
│   ├── alembic.ini                    # Alembic конфигурация
│   ├── pytest.ini                     # Pytest конфигурация
│   │
│   ├── alembic/                       # Миграции базы данных
│   │   ├── env.py                     # Alembic environment
│   │   ├── script.py.mako            # Шаблон миграций
│   │   └── versions/                  # Папка с миграциями
│   │
│   ├── app/                           # Основное приложение
│   │   ├── __init__.py
│   │   ├── main.py                   # Точка входа FastAPI
│   │   │
│   │   ├── api/                      # API endpoints
│   │   │   ├── __init__.py
│   │   │   └── v1/                   # API версия 1
│   │   │       ├── __init__.py
│   │   │       └── routes/           # API маршруты
│   │   │           ├── __init__.py
│   │   │           ├── auth.py       # Аутентификация
│   │   │           ├── users.py      # Пользователи
│   │   │           ├── routes.py     # Туристические маршруты
│   │   │           ├── locations.py  # Локации
│   │   │           └── recommendations.py  # Рекомендации
│   │   │
│   │   ├── core/                     # Ядро приложения
│   │   │   ├── __init__.py
│   │   │   ├── config.py            # Конфигурация
│   │   │   └── security.py          # JWT, безопасность
│   │   │
│   │   ├── db/                       # База данных
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # Base SQLAlchemy class
│   │   │   └── session.py           # Database session
│   │   │
│   │   ├── models/                   # SQLAlchemy ORM модели
│   │   │   ├── __init__.py
│   │   │   ├── user.py              # User model
│   │   │   ├── route.py             # Route, RouteLocation models
│   │   │   ├── location.py          # Location model
│   │   │   └── achievement.py       # Achievement, UserAchievement models
│   │   │
│   │   ├── schemas/                  # Pydantic схемы (DTO)
│   │   │   ├── __init__.py
│   │   │   ├── user.py              # User schemas
│   │   │   ├── route.py             # Route schemas
│   │   │   └── location.py          # Location schemas
│   │   │
│   │   └── services/                 # Бизнес-логика
│   │       ├── __init__.py
│   │       ├── ai_agent.py          # AI агент для маршрутов
│   │       ├── maps_service.py      # Yandex Maps, OpenTripMap
│   │       ├── recommendations.py   # Рекомендации
│   │       └── gamification.py      # Геймификация
│   │
│   └── tests/                        # Тесты
│       ├── __init__.py
│       ├── conftest.py              # Pytest fixtures
│       └── test_auth.py             # Тесты аутентификации
│
└── frontend/                         # Frontend (Flutter)
    ├── README.md                     # Frontend документация
    ├── pubspec.yaml                  # Flutter зависимости
    ├── analysis_options.yaml         # Dart анализатор
    │
    ├── lib/                          # Исходный код
    │   ├── main.dart                # Точка входа
    │   ├── app.dart                 # App widget
    │   │
    │   ├── core/                    # Ядро приложения
    │   │   ├── constants/           # Константы
    │   │   │   ├── api_constants.dart
    │   │   │   ├── app_colors.dart
    │   │   │   └── app_strings.dart
    │   │   ├── theme/              # Темы
    │   │   │   ├── app_theme.dart
    │   │   │   └── text_styles.dart
    │   │   └── utils/              # Утилиты
    │   │       ├── validators.dart
    │   │       └── formatters.dart
    │   │
    │   ├── data/                   # Data layer
    │   │   ├── datasources/        # API clients
    │   │   │   ├── auth_api.dart
    │   │   │   ├── route_api.dart
    │   │   │   └── location_api.dart
    │   │   ├── models/            # Data models
    │   │   │   ├── user_model.dart
    │   │   │   ├── route_model.dart
    │   │   │   └── location_model.dart
    │   │   └── repositories/      # Repository implementations
    │   │       ├── auth_repository_impl.dart
    │   │       ├── route_repository_impl.dart
    │   │       └── location_repository_impl.dart
    │   │
    │   ├── domain/                # Domain layer
    │   │   ├── entities/          # Business entities
    │   │   │   ├── user.dart
    │   │   │   ├── route.dart
    │   │   │   └── location.dart
    │   │   ├── repositories/      # Repository interfaces
    │   │   │   ├── auth_repository.dart
    │   │   │   ├── route_repository.dart
    │   │   │   └── location_repository.dart
    │   │   └── usecases/         # Use cases
    │   │       ├── auth/
    │   │       │   ├── login_usecase.dart
    │   │       │   └── register_usecase.dart
    │   │       ├── route/
    │   │       │   ├── generate_route_usecase.dart
    │   │       │   └── get_routes_usecase.dart
    │   │       └── location/
    │   │           └── search_locations_usecase.dart
    │   │
    │   └── presentation/          # Presentation layer
    │       ├── screens/           # Экраны
    │       │   ├── auth/
    │       │   │   ├── login_screen.dart
    │       │   │   └── register_screen.dart
    │       │   ├── home/
    │       │   │   └── home_screen.dart
    │       │   ├── route/
    │       │   │   ├── route_generator_screen.dart
    │       │   │   ├── route_details_screen.dart
    │       │   │   └── route_list_screen.dart
    │       │   ├── map/
    │       │   │   └── map_screen.dart
    │       │   ├── profile/
    │       │   │   └── profile_screen.dart
    │       │   └── achievements/
    │       │       └── achievements_screen.dart
    │       │
    │       ├── widgets/           # Переиспользуемые виджеты
    │       │   ├── common/
    │       │   │   ├── custom_button.dart
    │       │   │   ├── custom_text_field.dart
    │       │   │   └── loading_indicator.dart
    │       │   ├── route/
    │       │   │   ├── route_card.dart
    │       │   │   └── location_card.dart
    │       │   └── map/
    │       │       └── custom_marker.dart
    │       │
    │       └── state/            # State management
    │           ├── auth/
    │           │   ├── auth_provider.dart
    │           │   └── auth_state.dart
    │           ├── route/
    │           │   ├── route_provider.dart
    │           │   └── route_state.dart
    │           └── location/
    │               ├── location_provider.dart
    │               └── location_state.dart
    │
    ├── assets/                   # Ресурсы
    │   ├── images/              # Изображения
    │   ├── icons/               # Иконки
    │   └── fonts/               # Шрифты
    │
    ├── test/                    # Тесты
    │   ├── widget_test.dart
    │   └── unit_test.dart
    │
    ├── android/                 # Android конфигурация
    ├── ios/                     # iOS конфигурация
    └── web/                     # Web конфигурация (опционально)
```

---

## Описание основных компонентов

### Backend

#### Core (`backend/app/core/`)
Содержит базовую конфигурацию и утилиты:
- **config.py** - управление переменными окружения и настройками
- **security.py** - JWT токены, хеширование паролей

#### Models (`backend/app/models/`)
SQLAlchemy ORM модели для работы с базой данных:
- **user.py** - модель пользователя
- **route.py** - модель маршрута и связей с локациями
- **location.py** - модель туристической локации
- **achievement.py** - модели для геймификации

#### Schemas (`backend/app/schemas/`)
Pydantic схемы для валидации и сериализации данных:
- Валидация входных данных API
- Сериализация ответов
- Type safety

#### Services (`backend/app/services/`)
Бизнес-логика приложения:
- **ai_agent.py** - AI для генерации маршрутов
- **maps_service.py** - интеграция с внешними API карт
- **recommendations.py** - алгоритмы рекомендаций
- **gamification.py** - система ачивок и баллов

#### API Routes (`backend/app/api/v1/routes/`)
REST API endpoints:
- **auth.py** - регистрация, логин, JWT
- **users.py** - управление профилем
- **routes.py** - CRUD маршрутов
- **locations.py** - поиск локаций
- **recommendations.py** - рекомендации

---

### Frontend

#### Core (`frontend/lib/core/`)
Базовые компоненты:
- **constants/** - константы приложения
- **theme/** - темы и стили
- **utils/** - вспомогательные функции

#### Data Layer (`frontend/lib/data/`)
Работа с данными:
- **datasources/** - API клиенты, HTTP запросы
- **models/** - модели данных с JSON сериализацией
- **repositories/** - реализация репозиториев

#### Domain Layer (`frontend/lib/domain/`)
Бизнес-логика:
- **entities/** - бизнес-объекты (чистые от деталей реализации)
- **repositories/** - интерфейсы репозиториев
- **usecases/** - use cases для каждого действия

#### Presentation Layer (`frontend/lib/presentation/`)
UI и взаимодействие:
- **screens/** - экраны приложения
- **widgets/** - переиспользуемые UI компоненты
- **state/** - state management (Provider/Bloc)

---

## Соглашения о коде

### Backend (Python)

#### Именование файлов
- Используйте `snake_case` для файлов и модулей
- Например: `user_model.py`, `auth_service.py`

#### Именование классов
- Используйте `PascalCase` для классов
- Например: `UserModel`, `AuthService`

#### Именование функций
- Используйте `snake_case` для функций
- Например: `get_user()`, `create_route()`

#### Структура API endpoints
```python
@router.get("/{resource_id}")  # GET для получения
@router.post("/")              # POST для создания
@router.put("/{resource_id}")  # PUT для обновления
@router.delete("/{resource_id}") # DELETE для удаления
```

---

### Frontend (Dart/Flutter)

#### Именование файлов
- Используйте `snake_case` для файлов
- Например: `login_screen.dart`, `route_card.dart`

#### Именование классов
- Используйте `PascalCase` для классов
- Например: `LoginScreen`, `RouteCard`

#### Именование переменных
- Используйте `camelCase` для переменных
- Например: `userName`, `routeId`

#### Структура виджетов
```dart
class MyWidget extends StatelessWidget {
  const MyWidget({Key? key}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
```

---

## Зависимости между компонентами

### Backend Flow

```
API Routes → Services → Models/Repositories → Database
     ↓
  Schemas (validation)
```

### Frontend Flow

```
Screens → State Management → Use Cases → Repositories → API Clients
    ↓
 Widgets
```

---

## Дополнительные файлы

### Configuration Files
- **backend/.env** - переменные окружения (не в git)
- **backend/alembic.ini** - конфигурация миграций
- **backend/pytest.ini** - конфигурация тестов
- **frontend/pubspec.yaml** - Flutter зависимости

### CI/CD (планируется)
- **.github/workflows/** - GitHub Actions
- **Jenkinsfile** - Jenkins pipeline
- **k8s/** - Kubernetes манифесты

---

## Ресурсы

- [Backend README](../backend/README.md)
- [Frontend README](../frontend/README.md)
- [API Documentation](./API.md)
- [Database Schema](./DATABASE.md)
- [Architecture](./ARCHITECTURE.md)
- [Setup Guide](./SETUP.md)

