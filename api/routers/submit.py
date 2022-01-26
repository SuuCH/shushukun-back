from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.submit as submit_schema
import api.cruds.submit as submit_crud
from api.db import get_db

router = APIRouter()


@router.get("/submits", response_model=List[submit_schema.Submit])
async def list_src():
    return [submit_schema.Submit(id=1)]

@router.post("/submits", response_model=submit_schema.SubmitSrcResponse)
async def create_submit(submit_src_body: submit_schema.SubmitSrc, db: AsyncSession = Depends(get_db)):
    return await submit_crud.create_submit(db, submit_src_body)

