from openai import AsyncOpenAI
from bot.config import settings
from bot.prompt import get_prompt
from bot.logger import get_logger

logger = get_logger(__name__)


async def generate_sql(question: str):
    logger.info(f"Got message: {question}")
    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPENROUTER_API_KEY,
    )

    prompt = f"{get_prompt()} Вопрос: {question}"

    completion = await client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[{"role": "user", "content": prompt}],
        extra_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "VideoAnalyticsBot",
        },
    )
    sql_query = completion.choices[0].message.content.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    logger.info(f"SQL: {sql_query}")

    return sql_query
