from app.schemas.assistant import AskResponse


class AssistantService:
    def ask(self, question: str) -> AskResponse:
        return AskResponse(
            answer=f"Todavía no hay documentación para: '{question}'",
            sources=[],
            mode="mock",
        )
