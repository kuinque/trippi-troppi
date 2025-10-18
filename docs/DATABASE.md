# Database Schema

Схема базы данных PostgreSQL для TrippiTroppi.

## Entity Relationship Diagram

```
┌─────────────────┐
│     Users       │
├─────────────────┤
│ id (PK)         │
│ email           │
│ username        │
│ hashed_password │
│ full_name       │
│ is_active       │
│ is_superuser    │
│ points          │
│ created_at      │
│ updated_at      │
└─────────────────┘
        │
        │ 1:N
        ▼
┌─────────────────┐        ┌──────────────────┐
│     Routes      │──N:N───│ RouteLocations   │
├─────────────────┤        ├──────────────────┤
│ id (PK)         │        │ id (PK)          │
│ user_id (FK)    │        │ route_id (FK)    │
│ title           │        │ location_id (FK) │
│ description     │        │ order            │
│ city            │        │ visit_time       │
│ start_date      │        │ duration         │
│ end_date        │        │ notes            │
│ is_completed    │        │ is_visited       │
│ is_public       │        │ created_at       │
│ total_duration  │        └──────────────────┘
│ total_distance  │                │
│ interests       │                │
│ created_at      │                │ N:1
│ updated_at      │                ▼
└─────────────────┘        ┌──────────────────┐
        │                  │    Locations     │
        │                  ├──────────────────┤
        │ 1:N              │ id (PK)          │
        │                  │ name             │
        ▼                  │ description      │
┌─────────────────────┐    │ city             │
│ UserAchievements    │    │ address          │
├─────────────────────┤    │ latitude         │
│ id (PK)             │    │ longitude        │
│ user_id (FK)        │    │ category         │
│ achievement_id (FK) │    │ subcategories    │
│ is_unlocked         │    │ rating           │
│ unlocked_at         │    │ reviews_count    │
│ progress            │    │ working_hours    │
│ created_at          │    │ ticket_info      │
│ updated_at          │    │ external_id      │
└─────────────────────┘    │ external_source  │
        │                  │ photos           │
        │ N:1              │ website          │
        ▼                  │ phone            │
┌─────────────────┐        │ created_at       │
│  Achievements   │        │ updated_at       │
├─────────────────┤        └──────────────────┘
│ id (PK)         │
│ code            │
│ name            │
│ description     │
│ icon            │
│ points          │
│ condition_type  │
│ condition_value │
│ created_at      │
└─────────────────┘
```

## Tables

### users

Пользователи приложения.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | User ID |
| email | VARCHAR | UNIQUE, NOT NULL | Email address |
| username | VARCHAR | UNIQUE, NOT NULL | Username |
| hashed_password | VARCHAR | NOT NULL | Hashed password |
| full_name | VARCHAR | NULLABLE | Full name |
| is_active | BOOLEAN | DEFAULT TRUE | Account active |
| is_superuser | BOOLEAN | DEFAULT FALSE | Superuser flag |
| points | INTEGER | DEFAULT 0 | Gamification points |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Update timestamp |

**Indexes:**
- `idx_users_email` on `email`
- `idx_users_username` on `username`

---

### routes

Туристические маршруты.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Route ID |
| user_id | INTEGER | FOREIGN KEY(users.id), NOT NULL | Owner user ID |
| title | VARCHAR | NOT NULL | Route title |
| description | TEXT | NULLABLE | Description |
| city | VARCHAR | NOT NULL | City name |
| start_date | TIMESTAMP | NOT NULL | Trip start date |
| end_date | TIMESTAMP | NOT NULL | Trip end date |
| is_completed | BOOLEAN | DEFAULT FALSE | Completion status |
| is_public | BOOLEAN | DEFAULT FALSE | Public visibility |
| total_duration | INTEGER | NULLABLE | Total duration (minutes) |
| total_distance | FLOAT | NULLABLE | Total distance (km) |
| interests | JSON | NULLABLE | Interest categories |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Update timestamp |

**Indexes:**
- `idx_routes_user_id` on `user_id`
- `idx_routes_city` on `city`
- `idx_routes_is_public` on `is_public`

---

### locations

Туристические локации и достопримечательности.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Location ID |
| name | VARCHAR | NOT NULL | Location name |
| description | TEXT | NULLABLE | Description |
| city | VARCHAR | NOT NULL | City name |
| address | VARCHAR | NULLABLE | Address |
| latitude | FLOAT | NOT NULL | Latitude |
| longitude | FLOAT | NOT NULL | Longitude |
| category | VARCHAR | NOT NULL | Category |
| subcategories | JSON | NULLABLE | Subcategories |
| rating | FLOAT | NULLABLE | Rating (0-5) |
| reviews_count | INTEGER | DEFAULT 0 | Number of reviews |
| working_hours | JSON | NULLABLE | Working hours |
| ticket_info | JSON | NULLABLE | Ticket information |
| external_id | VARCHAR | NULLABLE | External API ID |
| external_source | VARCHAR | NULLABLE | External source |
| photos | JSON | NULLABLE | Photo URLs |
| website | VARCHAR | NULLABLE | Website URL |
| phone | VARCHAR | NULLABLE | Phone number |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Update timestamp |

**Indexes:**
- `idx_locations_city` on `city`
- `idx_locations_category` on `category`
- `idx_locations_external_id` on `external_id`
- `idx_locations_coordinates` on `(latitude, longitude)` (for geospatial queries)

---

### route_locations

Many-to-many связь между маршрутами и локациями.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | ID |
| route_id | INTEGER | FOREIGN KEY(routes.id), NOT NULL | Route ID |
| location_id | INTEGER | FOREIGN KEY(locations.id), NOT NULL | Location ID |
| order | INTEGER | NOT NULL | Order in route |
| visit_time | TIMESTAMP | NULLABLE | Planned visit time |
| duration | INTEGER | NULLABLE | Duration (minutes) |
| notes | TEXT | NULLABLE | User notes |
| is_visited | BOOLEAN | DEFAULT FALSE | Visited status |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |

**Indexes:**
- `idx_route_locations_route_id` on `route_id`
- `idx_route_locations_location_id` on `location_id`

---

### achievements

Ачивки для геймификации.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Achievement ID |
| code | VARCHAR | UNIQUE, NOT NULL | Unique code |
| name | VARCHAR | NOT NULL | Achievement name |
| description | TEXT | NULLABLE | Description |
| icon | VARCHAR | NULLABLE | Icon URL |
| points | INTEGER | DEFAULT 0 | Points reward |
| condition_type | VARCHAR | NOT NULL | Condition type |
| condition_value | INTEGER | NOT NULL | Condition value |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |

**Indexes:**
- `idx_achievements_code` on `code`

**Condition Types:**
- `routes_created` - Количество созданных маршрутов
- `routes_completed` - Количество завершенных маршрутов
- `locations_visited` - Количество посещенных локаций
- `cities_visited` - Количество посещенных городов
- `routes_shared` - Количество поделенных маршрутов
- `days_streak` - Дни подряд использования

---

### user_achievements

Связь пользователей и ачивок с прогрессом.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | ID |
| user_id | INTEGER | FOREIGN KEY(users.id), NOT NULL | User ID |
| achievement_id | INTEGER | FOREIGN KEY(achievements.id), NOT NULL | Achievement ID |
| is_unlocked | BOOLEAN | DEFAULT FALSE | Unlocked status |
| unlocked_at | TIMESTAMP | NULLABLE | Unlock timestamp |
| progress | INTEGER | DEFAULT 0 | Current progress |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Update timestamp |

**Indexes:**
- `idx_user_achievements_user_id` on `user_id`
- `idx_user_achievements_achievement_id` on `achievement_id`

---

## Sample Queries

### Get user's routes with locations

```sql
SELECT r.*, 
       json_agg(
         json_build_object(
           'order', rl.order,
           'location', l.*
         ) ORDER BY rl.order
       ) as locations
FROM routes r
LEFT JOIN route_locations rl ON r.id = rl.route_id
LEFT JOIN locations l ON rl.location_id = l.id
WHERE r.user_id = 1
GROUP BY r.id;
```

### Find nearby locations

```sql
SELECT *,
  (
    6371 * acos(
      cos(radians(55.7558)) * cos(radians(latitude)) *
      cos(radians(longitude) - radians(37.6173)) +
      sin(radians(55.7558)) * sin(radians(latitude))
    )
  ) AS distance
FROM locations
WHERE city = 'Москва'
HAVING distance < 5
ORDER BY distance
LIMIT 20;
```

### Get user achievements with progress

```sql
SELECT a.*, ua.is_unlocked, ua.progress, ua.unlocked_at
FROM achievements a
LEFT JOIN user_achievements ua ON a.id = ua.achievement_id AND ua.user_id = 1
ORDER BY a.points DESC;
```

### Get trending public routes

```sql
SELECT r.*, u.username, COUNT(rl.id) as locations_count
FROM routes r
JOIN users u ON r.user_id = u.id
LEFT JOIN route_locations rl ON r.id = rl.route_id
WHERE r.is_public = true
  AND r.created_at > NOW() - INTERVAL '30 days'
GROUP BY r.id, u.username
ORDER BY r.created_at DESC
LIMIT 10;
```

