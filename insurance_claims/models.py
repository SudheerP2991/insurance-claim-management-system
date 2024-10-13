print("Claim model loaded")  # Add this at the top of models.py to check if the file is being executed.

from django.db import models
from django.contrib.auth.models import User

class Claim(models.Model):
    CLAIM_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    claimant = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who submitted the claim
    policy_number = models.CharField(max_length=50)  # Policy number
    description = models.TextField()  # Description of the claim
    status = models.CharField(max_length=10, choices=CLAIM_STATUS_CHOICES, default='Pending')  # Claim status
    submission_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the claim is submitted
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  # File field for uploading related documents

    def __str__(self):
        return f"Claim {self.policy_number} by {self.claimant.username} - {self.status}"

