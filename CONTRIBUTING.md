# Contributing to TrippiTroppi

Спасибо за интерес к проекту TrippiTroppi! Мы приветствуем вклад сообщества.

## Как внести вклад

### Reporting Bugs

Если вы нашли баг, пожалуйста:

1. Проверьте, не был ли баг уже сообщен в [Issues](https://github.com/your-org/trippi-troppi/issues)
2. Создайте новый Issue с подробным описанием:
   - Шаги для воспроизведения
   - Ожидаемое поведение
   - Фактическое поведение
   - Скриншоты (если применимо)
   - Версия ОС, Python, Flutter

### Suggesting Enhancements

Для предложения новых функций:

1. Проверьте [Issues](https://github.com/your-org/trippi-troppi/issues) и [Discussions](https://github.com/your-org/trippi-troppi/discussions)
2. Создайте новый Issue с тегом `enhancement`
3. Опишите предлагаемую функциональность и её пользу

### Pull Requests

#### Процесс

1. Fork репозитория
2. Создайте новую ветку (`git checkout -b feature/AmazingFeature`)
3. Внесите изменения
4. Напишите/обновите тесты
5. Убедитесь, что все тесты проходят
6. Commit изменений (`git commit -m 'Add some AmazingFeature'`)
7. Push в ветку (`git push origin feature/AmazingFeature`)
8. Откройте Pull Request

#### Требования к Pull Request

- [ ] Код соответствует стандартам проекта
- [ ] Добавлены тесты для новой функциональности
- [ ] Все тесты проходят успешно
- [ ] Обновлена документация (если необходимо)
- [ ] Commit messages понятные и описательные
- [ ] PR имеет четкое описание изменений

## Стандарты кода

### Backend (Python)

#### Style Guide

Следуйте [PEP 8](https://pep8.org/):

```python
# Good
def calculate_route_distance(points: List[Point]) -> float:
    """Calculate total distance of route."""
    total = 0.0
    for i in range(len(points) - 1):
        total += haversine_distance(points[i], points[i + 1])
    return total

# Bad
def CalcDist(p):
    t=0
    for i in range(len(p)-1):
        t+=haversine(p[i],p[i+1])
    return t
```

#### Type Hints

Используйте type hints везде:

```python
from typing import List, Optional

def get_user(user_id: int, db: Session) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()
```

#### Docstrings

Используйте Google style docstrings:

```python
def generate_route(
    city: str,
    interests: List[str],
    days: int,
) -> Route:
    """Generate personalized travel route.
    
    Args:
        city: City name
        interests: List of user interests
        days: Number of days
        
    Returns:
        Generated route
        
    Raises:
        ValueError: If city not found
    """
    pass
```

#### Tools

Используйте эти инструменты:

```bash
# Formatting
black app/

# Import sorting
isort app/

# Linting
flake8 app/

# Type checking
mypy app/
```

---

### Frontend (Dart/Flutter)

#### Style Guide

Следуйте [Effective Dart](https://dart.dev/guides/language/effective-dart):

```dart
// Good
class RouteCard extends StatelessWidget {
  final Route route;
  final VoidCallback onTap;
  
  const RouteCard({
    Key? key,
    required this.route,
    required this.onTap,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        child: Text(route.title),
      ),
    );
  }
}
```

#### Widget Structure

```dart
// Разделяйте большие виджеты на подвиджеты
class ComplexScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: _buildAppBar(),
      body: _buildBody(),
      floatingActionButton: _buildFAB(),
    );
  }
  
  Widget _buildAppBar() => AppBar(title: Text('Title'));
  Widget _buildBody() => Container();
  Widget _buildFAB() => FloatingActionButton();
}
```

#### Tools

```bash
# Formatting
flutter format .

# Analysis
flutter analyze

# Testing
flutter test
```

---

## Git Workflow

### Branch Naming

- `feature/description` - новые функции
- `bugfix/description` - исправления багов
- `hotfix/description` - срочные исправления
- `docs/description` - документация
- `refactor/description` - рефакторинг

Примеры:
- `feature/ai-route-generation`
- `bugfix/login-validation`
- `docs/api-documentation`

### Commit Messages

Следуйте [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: Новая функция
- `fix`: Исправление бага
- `docs`: Документация
- `style`: Форматирование, пропущенные точки с запятой
- `refactor`: Рефакторинг
- `test`: Добавление тестов
- `chore`: Обновление build tasks, package manager

**Примеры:**

```bash
feat(auth): add JWT authentication

Implement JWT token generation and validation.
Add login and register endpoints.

Closes #123

---

fix(route): correct distance calculation

The haversine formula was using wrong units.

---

docs(api): update API documentation

Add examples for route generation endpoint.
```

---

## Testing

### Backend Tests

```python
# tests/test_routes.py
import pytest
from fastapi import status

def test_create_route(client, auth_headers):
    """Test route creation."""
    data = {
        "title": "Test Route",
        "city": "Moscow",
        "start_date": "2024-06-15T09:00:00",
        "end_date": "2024-06-17T18:00:00",
        "interests": ["museums", "parks"],
    }
    
    response = client.post(
        "/api/v1/routes/",
        json=data,
        headers=auth_headers,
    )
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == data["title"]
```

Запуск тестов:

```bash
pytest tests/ -v
pytest tests/ --cov=app
```

### Frontend Tests

```dart
// test/widget_test.dart
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('Login screen shows email field', (WidgetTester tester) async {
    await tester.pumpWidget(MyApp());
    
    expect(find.byType(TextField), findsOneWidget);
    expect(find.text('Email'), findsOneWidget);
  });
  
  test('Route model serialization', () {
    final route = Route(id: 1, title: 'Test');
    final json = route.toJson();
    
    expect(json['id'], 1);
    expect(json['title'], 'Test');
  });
}
```

Запуск тестов:

```bash
flutter test
flutter test --coverage
```

---

## Code Review Process

Все Pull Requests проходят code review:

### Что мы проверяем

1. **Функциональность**
   - Решает ли код заявленную проблему?
   - Работает ли как ожидается?

2. **Код качество**
   - Читабельность и поддерживаемость
   - Соответствие стандартам
   - Нет дублирования кода

3. **Тесты**
   - Достаточное покрытие тестами
   - Тесты проходят успешно

4. **Производительность**
   - Нет очевидных проблем с производительностью
   - Оптимальные алгоритмы

5. **Безопасность**
   - Нет уязвимостей
   - Правильная валидация данных

---

## Documentation

### Code Documentation

Документируйте:
- Публичные API
- Сложные алгоритмы
- Неочевидные решения

### Project Documentation

Обновляйте документацию при:
- Добавлении новых API endpoints
- Изменении структуры БД
- Добавлении новых функций

---

## Questions?

- Создайте [Discussion](https://github.com/your-org/trippi-troppi/discussions)
- Свяжитесь с maintainers
- Проверьте [FAQ](docs/FAQ.md)

---

## License

Внося вклад в проект, вы соглашаетесь, что ваш код будет лицензирован под той же лицензией, что и проект.

---

Спасибо за вклад в TrippiTroppi! 🎉

