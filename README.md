# Platform Trading Network of Electronics

Платформа для управления иерархической сетью по продаже электроники: заводы, розничные магазины и ИП.
## 🚀 Описание
Это Django-приложение предоставляет REST API для отображения и управления структурой сети поставок электроники.  
Каждый узел сети (например, завод, магазин, ИП) может иметь родительский узел и множество дочерних, формируя дерево.

**Основной стек:**
- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL
- django-filter

## 📁 Структура
```
platform-trading-network-of-electronics/
├── network/            # Приложение для работы с узлами сети
│   ├── models.py       # Модели NetworkNode, Product
│   ├── serializers.py  # DRF-сериализаторы
│   ├── views.py        # ViewSet'ы для API
│   ├── urls.py         # Роутинг для API
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Установка
1. **Клонируй репозиторий:**
```bash
git clone git@github.com:DeMarkiz/platform-trading-network-of-electronics.git
cd platform-trading-network-of-electronics
```

2. **Создай и активируй виртуальное окружение:**
```bash
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows
```

3. **Установи зависимости:**
```bash
pip install -r requirements.txt
```

4. **Настрой `.env` и базу данных PostgreSQL.**

5. **Примени миграции:**
```bash
python manage.py migrate
```

6. **Запусти сервер:**
```bash
python manage.py runserver
```

## 📦 API
### Примеры эндпоинтов:
| Метод | URL | Описание |
|-------|-----|----------|
| GET   | /api/nodes/            | Список всех узлов сети |
| POST  | /api/nodes/            | Создание нового узла |
| GET   | /api/nodes/{id}/       | Информация об узле |
| GET   | /api/nodes/{id}/children/ | Список дочерних узлов |
| GET   | /api/nodes/{id}/products/ | Товары, связанные с узлом |

Фильтрация, сортировка и вложенные маршруты настроены через `django-filter` и `DRF`.

## 🛠️ Возможности
- Поддержка древовидной структуры сети.
- CRUD-операции через API.
- Привязка товаров к узлам.
- Фильтрация по типам, названиям, родителям и др.

## 📌 План на будущее
- Авторизация и разграничение прав доступа.
- Импорт/экспорт данных.
- Визуализация дерева сети на фронте.

## 🧑‍💻 Автор
[DeMarkiz](https://github.com/DeMarkiz)

## 📝 Лицензия
Проект распространяется под лицензией MIT.
