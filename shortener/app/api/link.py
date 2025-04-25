from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.link import create_link, get_base_url_by_id
from app.schemas.link import LinkCreate, LinkDB

router = APIRouter()


@router.post(
    '/',
    response_model=LinkDB,
    response_model_exclude_none=True,
)
async def create_new_url(
        base_url: LinkCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_url = await create_link(base_url.base_url, session)
    return new_url


@router.get(
    '/{shorten_url_id}',
    status_code=status.HTTP_307_TEMPORARY_REDIRECT
)
async def get_base_url(
        shorten_url_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    db_link = await get_base_url_by_id(shorten_url_id, session)
    return RedirectResponse(url=db_link.base_url)
