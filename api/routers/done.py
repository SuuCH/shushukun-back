from fastapi import APIRouter

router = APIRouter()


@router.put("/submits/{submit_id}/done")
async def correct_done():
    return 
