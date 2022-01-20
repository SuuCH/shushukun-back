from typing import Optional

from pydantic import BaseModel, Field



class SubmitBase(BaseModel):
    src: Optional[str] = Field(None, example="#include <stdio.h>")
    error: Optional[str] = Field(None, example="分かりません")

class SubmitSrc(SubmitBase):
  password: Optional[str] = Field(None, example="aiueo")

class SubmitSrcRsponse(SubmitSrc):
  id: int
  done: bool = Field(False, description="採点完了フラグ")

  class Config:
    orm_mode = True