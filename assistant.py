from anthropic import Anthropic


class Assistant:
    """Manages the conversation with Claude, keeping turn history."""

    def __init__(self, config):
        self.client = Anthropic(api_key=config.anthropic_api_key)
        self.model = config.model
        self.max_tokens = config.max_tokens
        self.system_prompt = config.system_prompt
        self.history = []

    def reply(self, user_text: str) -> str:
        self.history.append({"role": "user", "content": user_text})
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.history,
        )
        text = "".join(
            block.text for block in response.content if block.type == "text"
        )
        self.history.append({"role": "assistant", "content": text})
        return text

    def reset(self) -> None:
        self.history = []
