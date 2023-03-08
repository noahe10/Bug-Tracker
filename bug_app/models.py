from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    def __str__ (self):
        return self.title

    class Meta:
        ordering = ['-complete']