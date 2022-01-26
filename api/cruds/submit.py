from sqlalchemy.ext.asyncio import AsyncSession

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