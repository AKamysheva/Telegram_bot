from openai import OpenAI
from bot.config import settings
from bot.prompt import get_prompt


async def generate_sql(question: str):
    print("Got message:", question)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPENROUTER_API_KEY,
    )

    prompt = f"{get_prompt()} Вопрос: {question}"

    completion = client.chat.completions.create(
        model="mistralai/devstral-2512:free",
        messages=[{"role": "user", "content": prompt}],
        extra_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "VideoAnalyticsBot",
        },
    )
    sql_query = completion.choices[0].message.content.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    print(sql_query)

    return sql_query
