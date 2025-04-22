from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.links import Link
from app.schemas.link import LinkCreate


async def create_link(
        new_link: LinkCreate,
        session: AsyncSession,
) -> Link:
    new_link_data = new_link.dict()
    db_link = Link(**new_link_data)

    session.add(db_link)
    return db_link


async def get_base_url_by_id(
        shorten_url_id: int,
        session: AsyncSession
):
    result = await session.execute(
        select(Link).where(Link.id == shorten_url_id)
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link
