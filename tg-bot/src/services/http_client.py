import httpx


class DjangoHttpClient:
    def __init__(self, base_url, timeout=None):
        self.base_url = base_url
        self.timeout = timeout

    async def update_token_status(self, chat_id, username, token: str):
        url = f"{self.base_url}/api/core/update-status/"
        data = {"chat_id": chat_id, "username": username, "token": token}

        async with httpx.AsyncClient() as client:
            response = await client.put(url, data=data, timeout=self.timeout)

        return response
