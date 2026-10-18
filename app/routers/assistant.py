from fastapi import APIRouter, Depends

from app.schemas.assistant import AskRequest, AskResponse
from app.dependencies import get_assistant_service
from app.services.assistant_service import AssistantService

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest, service: AssistantService = Depends(get_assistant_service)):
    return service.ask(request.question)
