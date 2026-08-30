from typing import Protocol


class LlmProvider(Protocol):
    def generate(self, system_prompt: str, user_message: str) -> str: ...
