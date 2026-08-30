from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_prompt: str = Field(alias="userPrompt")


class ChatResponse(BaseModel):
    answer: str
