from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    affilation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    qrUrl = models.URLField()
    couponDetail = models.CharField(max_length=200, default="")
    passCode = models.BinaryField(max_length=100, null=True)
    def __str__(self):
        return f"{self.name}({self.email})"

class CheckInLog(models.Model):
    tokenId = models.CharField(max_length=100, unique=True)
    checkedInAt = models.DateTimeField()
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.tokenId}({self.checkedInAt})"