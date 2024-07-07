from django.db import models
from django.contrib.auth.models import User

class profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userimage = models.ImageField(upload_to='photos/%Y/%m%d/')

def __str__(self):
    return self.User.username


class masseges(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]



    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'