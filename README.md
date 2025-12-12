# Video Analytics Telegram Bot

#### Telegram-бот для аналитики видео, который отвечает на вопросы на русском языке, формируя SQL-запросы и извлекая данные из базы данных PostgreSQL.

## Требования
- Python 3.13+
- PostgreSQL 17
- Poetry
- Docker and Docker Compose (optional)

## Установка
1. Клонируем репозиторий
```python
git clone https://github.com/AKamysheva/Telegram_bot.git
```
2. Create an .env file
```python
BOT_TOKEN=mybottoken
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
HOST_DB=db
PORT_DB=5432
OPENROUTER_API_KEY=myapikey
```
3. Запуск в Docker
```python
docker build -t bot .
docker compose up -d
```

## Дополнительно

Для загрузки данных в базу требуется файл `videos.json` с исходными данными.  
Этот файл **не включён** в репозиторий по причинам конфиденциальности.  
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