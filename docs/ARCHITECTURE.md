# TrippiTroppi - Архитектура системы

## Обзор

TrippiTroppi — это мобильное приложение для создания персонализированных туристических маршрутов с использованием искусственного интеллекта.

## Технологический стек

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15+
- **Cache**: Redis
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **AI/ML**: OpenAI API, LangChain

### Frontend
- **Framework**: Flutter 3.16+
- **State Management**: Provider / Riverpod / Bloc
- **Networking**: Dio / HTTP
- **Maps**: Yandex MapKit
- **Storage**: Hive / SharedPreferences

### External APIs
- **Yandex Maps API** - Карты, геокодинг, маршруты
- **OpenTripMap API** - Достопримечательности и локации
- **OpenAI API** - AI для генерации маршрутов

### DevOps
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions (планируется)

---

## Архитектура Backend

### Структура слоев

```
┌─────────────────────────────────────────────┐
│           API Layer (FastAPI)               │
│  - REST endpoints                           │
│  - Request/Response validation              │
│  - Authentication middleware                │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│         Business Logic Layer                │
│  - Services (AI Agent, Maps, etc.)          │
│  - Use Cases                                │
│  - Business Rules                           │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│          Data Access Layer                  │
│  - SQLAlchemy Models                        │
│  - Repositories                             │
│  - Database Session Management              │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│              Database                       │
│  - PostgreSQL                               │
│  - Redis (cache)                            │
└─────────────────────────────────────────────┘
```

### Ключевые компоненты

#### 1. API Routes (`app/api/v1/routes/`)
- **auth.py** - Аутентификация (регистрация, логин)
- **users.py** - Управление пользователями
- **routes.py** - CRUD для маршрутов
- **locations.py** - Поиск и управление локациями
- **recommendations.py** - Рекомендации и популярные маршруты

#### 2. Services (`app/services/`)
- **ai_agent.py** - AI агент для генерации маршрутов
- **maps_service.py** - Интеграция с Yandex Maps и OpenTripMap
- **recommendations.py** - Система рекомендаций
- **gamification.py** - Геймификация (ачивки, баллы)

#### 3. Models (`app/models/`)
- **user.py** - Модель пользователя
- **route.py** - Модель маршрута и связей с локациями
- **location.py** - Модель локации
- **achievement.py** - Модели ачивок

#### 4. Schemas (`app/schemas/`)
Pydantic схемы для валидации данных API

#### 5. Core (`app/core/`)
- **config.py** - Конфигурация приложения
- **security.py** - JWT, хеширование паролей

---

## Архитектура Frontend (Flutter)

### Clean Architecture

```
┌─────────────────────────────────────────────┐
│          Presentation Layer                 │
│  - Screens                                  │
│  - Widgets                                  │
│  - State Management (Provider/Bloc)         │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│            Domain Layer                     │
│  - Entities                                 │
│  - Use Cases                                │
│  - Repository Interfaces                    │
└─────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│             Data Layer                      │
│  - API Clients                              │
│  - Models (DTOs)                            │
│  - Repository Implementations               │
│  - Local Storage                            │
└─────────────────────────────────────────────┘
```

### Основные экраны

1. **Onboarding** - Приветствие
2. **Auth** - Вход/Регистрация
3. **Home** - Главный экран с рекомендациями
4. **Route Generator** - AI генератор маршрутов
5. **Route Details** - Детали маршрута
6. **Map View** - Карта с маршрутом и навигацией
7. **Profile** - Профиль пользователя
8. **Achievements** - Ачивки и геймификация
9. **Social/Share** - Обмен маршрутами

---

## Data Flow

### Создание маршрута с AI

```
┌──────────┐      ┌──────────┐      ┌──────────────┐
│  User    │─────▶│  Flutter │─────▶│  Backend API │
│  Input   │      │   App    │      │   /routes/   │
└──────────┘      └──────────┘      │   generate   │
                                     └──────────────┘
                                            │
                                            ▼
                                     ┌──────────────┐
                                     │  AI Service  │
                                     │  (OpenAI)    │
                                     └──────────────┘
                                            │
                                            ▼
                                     ┌──────────────┐
                                     │ Maps Service │
                                     │  (Yandex/    │
                                     │  OpenTrip)   │
                                     └──────────────┘
                                            │
                                            ▼
                                     ┌──────────────┐
                                     │  Optimize    │
                                     │  Route Logic │
                                     └──────────────┘
                                            │
                                            ▼
                                     ┌──────────────┐
                                     │   Database   │
                                     │ (PostgreSQL) │
                                     └──────────────┘
                                            │
                                            ▼
                                     ┌──────────────┐
                                     │   Response   │
                                     │   to Client  │
                                     └──────────────┘
```

### Аутентификация Flow

```
1. User sends credentials
2. Backend validates and creates JWT token
3. Flutter app stores token (secure storage)
4. All subsequent requests include JWT in Authorization header
5. Backend validates token on each request
```

---

## База данных

### Основные таблицы

- **users** - Пользователи
- **routes** - Маршруты
- **locations** - Локации и достопримечательности
- **route_locations** - Связь маршрутов и локаций (многие-ко-многим)
- **achievements** - Ачивки
- **user_achievements** - Прогресс пользователей по ачивкам

См. [DATABASE.md](./DATABASE.md) для детальной схемы.

---

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Регистрация
- `POST /api/v1/auth/login` - Вход
- `GET /api/v1/auth/me` - Текущий пользователь

### Routes
- `POST /api/v1/routes/generate` - Генерация маршрута (AI)
- `GET /api/v1/routes/` - Список маршрутов
- `GET /api/v1/routes/{id}` - Получить маршрут
- `PUT /api/v1/routes/{id}` - Обновить маршрут
- `DELETE /api/v1/routes/{id}` - Удалить маршрут
- `GET /api/v1/routes/public/` - Публичные маршруты

### Locations
- `POST /api/v1/locations/search` - Поиск локаций
- `GET /api/v1/locations/{id}` - Информация о локации
- `GET /api/v1/locations/nearby/{lat}/{lon}` - Локации поблизости

### Recommendations
- `GET /api/v1/recommendations/` - Персональные рекомендации
- `GET /api/v1/recommendations/routes/trending` - Популярные маршруты
- `GET /api/v1/recommendations/routes/{id}/similar` - Похожие маршруты

См. [API.md](./API.md) для полной документации API.

---

## Безопасность

### Аутентификация
- JWT токены с истечением срока действия
- Bcrypt для хеширования паролей
- HTTPS для production

### Авторизация
- Проверка владельца ресурса
- Public/Private маршруты
- Rate limiting (планируется)

### Валидация
- Pydantic для валидации входных данных
- SQL injection защита через ORM
- CORS middleware

---

## Масштабирование

### Горизонтальное масштабирование
- Stateless backend (можно запустить несколько инстансов)
- Redis для shared cache между инстансами
- Load balancer (nginx)

### Оптимизация
- Database indexing
- Query optimization
- Caching (Redis)
- CDN для статики

### Monitoring (планируется)
- Logging (структурированное)
- Metrics (Prometheus)
- Error tracking (Sentry)
- Performance monitoring

---

## Deployment

### Development
```bash
docker-compose up
```

### Production (планируется)
- Kubernetes / Docker Swarm
- CI/CD pipeline (GitHub Actions)
- Blue-Green deployment
- Automatic backups

---

## Roadmap

### Phase 1: MVP ✓
- [x] Базовая архитектура backend
- [x] Базовая архитектура frontend
- [x] Документация
- [ ] Реализация AI агента
- [ ] Интеграция с картами
- [ ] Базовый UI

### Phase 2: Enhancement
- [ ] Геймификация
- [ ] Социальные функции
- [ ] Push-уведомления
- [ ] Оффлайн режим

### Phase 3: Scale
- [ ] Интеграция с бронированием
- [ ] Партнерские программы
- [ ] Расширение на другие страны
- [ ] Web версия

---

## Контакты

- Product Manager: (заполните)
- Tech Lead: (заполните)
- Backend Team: (заполните)
- Frontend Team: (заполните)

