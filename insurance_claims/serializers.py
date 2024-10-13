from rest_framework import serializers
from .models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['id', 'claimant', 'policy_number', 'description', 'status', 'submission_date', 'file']
        read_only_fields = ['id', 'status', 'submission_date']
