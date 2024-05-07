from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  
    tokens = models.IntegerField(default=4000)

    def __str__(self):
        return self.username
        return self.tokens

class Chat(models.Model):
    # user = models.ForeignKey(user, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
        return self.message
        return self.timestamp