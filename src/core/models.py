from django.db import models
from django.contrib.auth.models import User


class TelegramToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, unique=True)
    is_active = models.BooleanField(default=False)
    chat_id = models.CharField(max_length=256, blank=True, null=True)
    tg_username = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def activate_token(self, chat_id, tg_username):
        self.is_active = True
        self.chat_id = chat_id
        self.tg_username = tg_username
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.token}"


class MessageHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sended_at}"
