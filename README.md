# Video Analytics Telegram Bot

#### Telegram-бот для аналитики видео, который отвечает на вопросы на русском языке, формируя SQL-запросы и извлекая данные из базы данных PostgreSQL.

## Требования
- Python 3.13+
- PostgreSQL 17
- Poetry
- Docker and Docker Compose (optional)

## Установка
1. Клонируем репозиторий и устанавливаем зависимости
```python
git clone https://github.com/AKamysheva/Telegram_bot.git
poetry install
```
2. Создайте .env файл в папке bot
```python
BOT_TOKEN=mybottoken
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
HOST_DB=db
PORT_DB=5432
OPENROUTER_API_KEY=myapikey
```
3. Создайте бота через @BotFather и получите токен, добавьте его в файл `.env`
4. Запуск в Docker
```python
docker build -t bot .
docker compose up -d

# выполняем инициализацию данных
docker compose run bot poetry run python -m bot.db.init_db 
docker compose run bot poetry run python -m bot.db.load-json
```

## Дополнительно

Для загрузки данных в базу требуется файл `videos.json` с исходными данными.  
Этот файл **не включён** в репозиторий по причинам конфиденциальности.
Файл должен быть размещён в директории bot/ перед запуском скрипта загрузки данных.
Структура файла должна соответствовать примеру:

```json
{
  "videos": [
    {
      "id": "uuid",
      "video_created_at": "2025-11-26T11:00:08.983295+00:00",
      "views_count": 0,
      "likes_count": 0,
      "reports_count": 0,
      "comments_count": 0,
      "creator_id": "creator_uuid",
      "created_at": "2025-11-26T11:00:08.983295+00:00",
      "updated_at": "2025-12-01T10:00:00.236609+00:00",
      "snapshots": [
        {
          "id": "uuid",
          "video_id": "uuid",
          "views_count": 0,
          "likes_count": 0,
          "reports_count": 0,
          "comments_count": 0,
          "delta_views_count": 0,
          "delta_likes_count": 0,
          "delta_reports_count": 0,
          "delta_comments_count": 0,
          "created_at": "2025-11-26T11:00:09.053200+00:00",
          "updated_at": "2025-11-26T11:00:09.053200+00:00"
        }
      ]
    }
  ]
}
```
Для корректной работы загрузите этот файл в папку bot/ перед запуском загрузчика данных.

## Подход к обработке запросов:
1. Пользователь отправляет вопрос на русском языке в Telegram.
2. Текст вопроса передаётся в LLM (Mistral Devstral через OpenRouter) вместе с описанием схемы БД и примерами запросов.
3. Модель возвращает один SQL-запрос без пояснений.
4. SQL-запрос выполняется напрямую в PostgreSQL через SQLAlchemy.
5. Результат запроса (одно число) возвращается пользователю.
