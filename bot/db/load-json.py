# flake8: noqa: E501
import asyncio
import json
from sqlalchemy import text
from datetime import datetime
from bot.db.database import async_session


def parse_datetime(dt_str: str) -> datetime:
    return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))


async def load_data_from_json_to_db(str_path: str = "bot/videos.json"):
    with open(str_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    async with async_session() as session:
        async with session.begin():
            for video in data["videos"]:
                await session.execute(
                    text(
                        """
                    INSERT INTO videos 
                    (id, video_created_at, views_count, likes_count, reports_count, 
                     comments_count, creator_id, created_at, updated_at)
                    VALUES 
                    (:id, :video_created_at, :views_count, :likes_count, :reports_count,
                     :comments_count, :creator_id, :created_at, :updated_at)
                    """
                    ),
                    {
                        "id": video["id"],
                        "video_created_at": parse_datetime(video["video_created_at"]),
                        "views_count": video["views_count"],
                        "likes_count": video["likes_count"],
                        "reports_count": video["reports_count"],
                        "comments_count": video["comments_count"],
                        "creator_id": video["creator_id"],
                        "created_at": parse_datetime(video["created_at"]),
                        "updated_at": parse_datetime(video["updated_at"]),
                    },
                )
                for s in video.get("snapshots", []):
                    await session.execute(
                        text(
                            """
                        INSERT INTO video_snapshots
                        (id, video_id, views_count, likes_count, reports_count, comments_count,
                         delta_views_count, delta_likes_count, delta_reports_count, 
                         delta_comments_count, created_at, updated_at)
                        VALUES 
                        (:id, :video_id, :views_count, :likes_count, :reports_count, 
                         :comments_count, :delta_views_count, :delta_likes_count, :delta_reports_count,
                         :delta_comments_count, :created_at, :updated_at)
                        """
                        ),
                        {
                            "id": s["id"],
                            "video_id": s["video_id"],
                            "views_count": s["views_count"],
                            "likes_count": s["likes_count"],
                            "reports_count": s["reports_count"],
                            "comments_count": s["comments_count"],
                            "delta_views_count": s["delta_views_count"],
                            "delta_likes_count": s["delta_likes_count"],
                            "delta_reports_count": s["delta_reports_count"],
                            "delta_comments_count": s["delta_comments_count"],
                            "created_at": parse_datetime(s["created_at"]),
                            "updated_at": parse_datetime(s["updated_at"]),
                        },
                    )


if __name__ == "__main__":
    asyncio.run(load_data_from_json_to_db())
