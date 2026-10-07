from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def test_api():
    return {
        "message": "FastAPI is working!",
        "status": "success"
    }