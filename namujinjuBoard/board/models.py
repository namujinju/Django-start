from django.db import models


class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_nickname = models.CharField(max_length=10)
    u_age = models.IntegerField(default=0)
    # u_gender = models.Choices()

    def __str__(self):
        return self.u_name
