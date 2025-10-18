# TrippiTroppi API Documentation

Документация API для backend TrippiTroppi.

## Base URL

```
http://localhost:8000/api/v1
```

## Аутентификация

API использует JWT (JSON Web Tokens) для аутентификации.

### Получение токена

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=password
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Использование токена

Добавьте заголовок Authorization к запросам:

```http
Authorization: Bearer <access_token>
```

---

## Authentication Endpoints

### Register

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "full_name": "John Doe"
}
```

### Login

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=password
```

### Get Current User

```http
GET /auth/me
Authorization: Bearer <token>
```

---

## Users Endpoints

### Get Current User Profile

```http
GET /users/me
Authorization: Bearer <token>
```

### Update Current User

```http
PUT /users/me
Authorization: Bearer <token>
Content-Type: application/json

{
  "full_name": "Updated Name",
  "email": "new@example.com"
}
```

### Get User by ID

```http
GET /users/{user_id}
```

---

## Routes Endpoints

### Generate Route (AI)

```http
POST /routes/generate
Authorization: Bearer <token>
Content-Type: application/json

{
  "city": "Москва",
  "start_date": "2024-06-15T09:00:00",
  "end_date": "2024-06-17T18:00:00",
  "interests": ["museums", "parks", "food"],
  "max_locations_per_day": 5,
  "preferred_start_time": "09:00",
  "preferred_transport": "walking"
}
```

### Get User Routes

```http
GET /routes/?skip=0&limit=100
Authorization: Bearer <token>
```

### Get Route by ID

```http
GET /routes/{route_id}
Authorization: Bearer <token>
```

### Update Route

```http
PUT /routes/{route_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated description",
  "is_public": true
}
```

### Delete Route

```http
DELETE /routes/{route_id}
Authorization: Bearer <token>
```

### Get Public Routes

```http
GET /routes/public/?city=Москва&skip=0&limit=20
```

---

## Locations Endpoints

### Search Locations

```http
POST /locations/search
Content-Type: application/json

{
  "city": "Москва",
  "category": "museum",
  "limit": 20
}
```

### Get Location by ID

```http
GET /locations/{location_id}
```

### Get Nearby Locations

```http
GET /locations/nearby/{latitude}/{longitude}?radius=1000&category=museum&limit=20
```

---

## Recommendations Endpoints

### Get Personalized Recommendations

```http
GET /recommendations/?city=Москва&limit=10
Authorization: Bearer <token>
```

### Get Trending Routes

```http
GET /recommendations/routes/trending?city=Москва&limit=10
```

### Get Similar Routes

```http
GET /recommendations/routes/{route_id}/similar?limit=5
```

---

## Data Models

### User

```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "points": 100,
  "created_at": "2024-06-09T12:00:00",
  "updated_at": "2024-06-09T12:00:00"
}
```

### Route

```json
{
  "id": 1,
  "user_id": 1,
  "title": "Путешествие по Москве",
  "description": "3-дневный маршрут",
  "city": "Москва",
  "start_date": "2024-06-15T09:00:00",
  "end_date": "2024-06-17T18:00:00",
  "is_completed": false,
  "is_public": true,
  "total_duration": 1440,
  "total_distance": 15.5,
  "interests": ["museums", "parks"],
  "locations": [],
  "created_at": "2024-06-09T12:00:00",
  "updated_at": "2024-06-09T12:00:00"
}
```

### Location

```json
{
  "id": 1,
  "name": "Красная площадь",
  "description": "Главная площадь Москвы",
  "city": "Москва",
  "address": "Красная площадь, Москва",
  "latitude": 55.7539,
  "longitude": 37.6208,
  "category": "landmark",
  "subcategories": ["historical", "unesco"],
  "rating": 4.8,
  "reviews_count": 15000,
  "working_hours": {
    "mon": "00:00-23:59",
    "tue": "00:00-23:59"
  },
  "ticket_info": {
    "price": 0,
    "free": true
  },
  "photos": ["url1", "url2"],
  "website": "https://example.com",
  "phone": "+7 123 456 78 90",
  "created_at": "2024-06-09T12:00:00",
  "updated_at": "2024-06-09T12:00:00"
}
```

---

## Error Responses

### 400 Bad Request

```json
{
  "detail": "Invalid request data"
}
```

### 401 Unauthorized

```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden

```json
{
  "detail": "Not enough permissions"
}
```

### 404 Not Found

```json
{
  "detail": "Resource not found"
}
```

### 422 Validation Error

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "invalid email format",
      "type": "value_error.email"
    }
  ]
}
```

---

## Interactive Documentation

После запуска backend, автоматически генерируется интерактивная документация:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

