from typing import Optional
from asgiref.sync import sync_to_async


@sync_to_async
def get_token(text: str) -> Optional[str]:
    try:
        _, token = text.split()
    except ValueError:
        return

    return token
