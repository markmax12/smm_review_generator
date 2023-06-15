import openai

class OpenAI:
    MODEL = "gpt-3.5-turbo"
    msg = "Напиши отызв на этот товар."

    def __init__(self, api_key: str) -> None:
        openai.api_key = api_key

    def send_request(self, title: str) -> str:
        print(f"{self.msg}, {title}")
        response = openai.ChatCompletion.create(
            model=self.MODEL,
            messages=[
                {"role": "user", "content": f"{title}. {self.msg}"}
            ],
        )
        return response