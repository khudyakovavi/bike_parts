### Содержание
1. [Установка](#Установка)
2. [Запуск](#Запуск)
3. [API](#API)

### Установка
1. Установка виртуального окружения:
  - `virtualenv .env`
  - `source .env/bin/activate`
  - `pip install -r requirements/local.txt`
2. Задать переменную окружения DJANGO_SETTINGS_MODULE:
  - `source postactivate`
3. Применить миграции
  - `python manage.py migrate`

### Запуск
1. Задать переменную окружения DJANGO_SETTINGS_MODULE:
  - `source postactivate`
2. Запуск сервера:
  - `python manage.py runserver`

### API

API для мобильных устройств, со следующими командами:

1. `GET api/parts/`
  1. Получение списка объявлений с возможностью пагинации. Пример:
    - `GET api/parts/?page=2`
  2. Поиск по названию/марке детали. Примеры:
    - `GET api/parts/?name=wheel`
    - `GET api/parts/?brand=vinca`

2. `POST api/part/`
    - Команда для добавления объявления. Примеры:
    - `POST api/part/ name="Wheel" brand_name="Vinca" phone="87777777"`
    - `POST api/part/ name="Wheel" brand_name="Vinca" price=10 email="test@test.test"`
    - `POST api/part/ name="Wheel" brand_name="Vinca" price=10 phone="+77777777" email="test@test.test"`
    
3. `GET api/brands/`
    - Получение статистики по популярным маркам деталей: марки, детали которых встречаются чаще 5 раз, отсортированные по количеству деталей этой марки.
