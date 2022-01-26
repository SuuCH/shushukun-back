from multiprocessing.spawn import import_main_path
from typing import List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.submit as submit_model
import api.schemas.submit as submit_schema

async def create_submit(
  db: AsyncSession, submit_src: submit_schema.SubmitSrc
) ->  submit_model.Submit:
  submit = submit_model.Submit(**submit_src.dict())
  db.add(submit)
  await db.commit()
  await db.refresh(submit)
  return submit

async def get_submits_with_done(db: AsyncSession) -> List[Tuple[int, str, str ,bool]]:
  result: Result = await(
    db.execute(
      select(
        submit_model.Submit.id,
        submit_model.Submit.src,
        submit_model.Submit.error,
        submit_model.Done.id.isnot(None).label("done"),
      ).outerjoin(submit_model.Done)
    )
  )
  return result.all()