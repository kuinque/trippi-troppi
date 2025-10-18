# TrippiTroppi Frontend

Flutter мобильное приложение для TrippiTroppi.

## 🚀 Установка и запуск

### Требования

- Flutter SDK 3.16+
- Dart 3.2+
- Android Studio / Xcode (для эмуляторов)

### Установка зависимостей

```bash
flutter pub get
```

### Запуск приложения

```bash
# На Android эмуляторе
flutter run

# На iOS симуляторе
flutter run -d ios

# На физическом устройстве
flutter run -d <device-id>
```

### Сборка

```bash
# Android APK
flutter build apk

# Android App Bundle
flutter build appbundle

# iOS
flutter build ios
```

## 📁 Структура проекта

```
frontend/
├── lib/
│   ├── main.dart                  # Точка входа
│   ├── app.dart                   # App widget
│   ├── core/                      # Константы, утилиты, темы
│   │   ├── constants/
│   │   ├── theme/
│   │   └── utils/
│   ├── data/                      # Данные
│   │   ├── datasources/          # API клиенты
│   │   ├── models/               # Data models
│   │   └── repositories/         # Repository implementations
│   ├── domain/                    # Бизнес-логика
│   │   ├── entities/             # Domain entities
│   │   ├── repositories/         # Repository interfaces
│   │   └── usecases/             # Use cases
│   └── presentation/              # UI
│       ├── screens/              # Экраны
│       ├── widgets/              # Переиспользуемые виджеты
│       └── state/                # State management (Provider/Bloc)
├── assets/                        # Ресурсы
│   ├── images/
│   ├── icons/
│   └── fonts/
├── test/                          # Тесты
└── pubspec.yaml                   # Dependencies
```

## 🎨 Архитектура

Проект использует **Clean Architecture** с разделением на слои:

### Data Layer
- API клиенты для взаимодействия с backend
- Модели данных (JSON serialization)
- Реализация репозиториев

### Domain Layer
- Entities (бизнес-объекты)
- Repository интерфейсы
- Use cases (бизнес-логика)

### Presentation Layer
- UI компоненты (screens, widgets)
- State management (Provider/Riverpod/Bloc)
- Навигация

## 📦 Основные зависимости

```yaml
dependencies:
  flutter:
    sdk: flutter
  
  # State Management
  provider: ^6.1.1
  # or
  flutter_bloc: ^8.1.3
  
  # Networking
  http: ^1.1.0
  dio: ^5.4.0
  
  # Routing
  go_router: ^12.1.1
  
  # Local Storage
  shared_preferences: ^2.2.2
  hive: ^2.2.3
  
  # Maps
  yandex_mapkit: ^4.0.0
  
  # UI
  flutter_svg: ^2.0.9
  cached_network_image: ^3.3.0
  
  # Utils
  intl: ^0.18.1
  equatable: ^2.0.5
```

## 🗺️ Основные экраны

1. **Onboarding** - Приветствие и введение
2. **Auth** - Вход/Регистрация
3. **Home** - Главный экран с рекомендациями
4. **Route Generator** - Создание маршрута с AI
5. **Route Details** - Детали маршрута
6. **Map** - Карта с маршрутом
7. **Profile** - Профиль пользователя
8. **Achievements** - Ачивки и геймификация
9. **Social** - Обмен маршрутами

## 🎯 TODO

- [ ] Настроить Flutter проект
- [ ] Реализовать API клиент
- [ ] Создать базовые экраны
- [ ] Интегрировать Yandex Maps
- [ ] Реализовать state management
- [ ] Добавить темы (светлая/темная)
- [ ] Локализация (RU/EN)
- [ ] Unit и widget тесты

