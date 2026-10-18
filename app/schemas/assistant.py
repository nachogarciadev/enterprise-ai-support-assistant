from pydantic import BaseModel, Field, ConfigDict


class AskRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    question: str = Field(
        min_length=3, strict=True, description="The question to ask the assistant"
    )


class AskResponse(BaseModel):
    answer: str
    sources: list[str]
    mode: str
