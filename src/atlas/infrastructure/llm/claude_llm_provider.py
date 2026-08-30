import anthropic


class ClaudeLlmProvider:
    def __init__(self, api_key: str, model: str = "claude-sonnet-5") -> None:
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def generate(self, system_prompt: str, user_message: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=16000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        if response.stop_reason == "refusal":
            raise RuntimeError("The model declined to answer this question.")

        return next(block.text for block in response.content if block.type == "text")
