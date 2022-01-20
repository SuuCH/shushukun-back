from fastapi import APIRouter

router = APIRouter()


@router.get("/submits")
async def list_src():
    pass


@router.post("/submits")
async def submit_src():
    pass

