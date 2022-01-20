from typing import List
from fastapi import APIRouter

import api.schemas.submit as submit_schema

router = APIRouter()


@router.get("/submits", response_model=List[submit_schema.Submit])
async def list_src():
    return [submit_schema.Submit(id=1)]

@router.post("/submits", response_model=submit_schema.SubmitSrcRsponse)
async def submit_src(submit_src_body: submit_schema.SubmitSrc):
    return submit_schema.SubmitSrcRsponse(id=1,password="aiueo" **submit_src_body.dic())

