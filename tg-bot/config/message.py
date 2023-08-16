import json


class Messages:
    def __init__(self, file_path: str = "config/messages.json"):
        self.file_path = file_path
        self.messages = self._load_messages()

    def _load_messages(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def __getattr__(self, key):
        if key in self.messages:
            return self.messages[key]
        raise AttributeError(f"'Messages' object has no attribute '{key}'")


msg: Messages = Messages()
