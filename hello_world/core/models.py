from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MEMBERSHIP_CHOICES = [
        ("free", "Free"),
        ("premium", "Premium"),
        ("pro", "Pro"),
    ]
    membership = models.CharField(max_length=16, choices=MEMBERSHIP_CHOICES, default="free")

    def __str__(self):
        return f"{self.user.username} ({self.get_membership_display()})"
