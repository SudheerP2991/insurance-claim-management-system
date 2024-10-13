from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Claim
from .serializers import ClaimSerializer

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [AllowAny]  # Bypass JWT for testing purposes

    # Override perform_create to bypass user association if needed
    def perform_create(self, serializer):
        serializer.save()

    # Optional: Override update for custom PATCH/PUT behavior
    def update(self, request, *args, **kwargs):
        # Get the instance of the claim to be updated
        instance = self.get_object()
        
        # Apply partial or full update, based on the request data
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    # Optional: Perform additional logic when updating
    def perform_update(self, serializer):
        # Save the updated instance
        serializer.save()

    # DELETE method is already supported by ModelViewSet, but we can override if needed
    def destroy(self, request, *args, **kwargs):
        # Get the claim instance to delete
        instance = self.get_object()
        self.perform_destroy(instance)
        
        # Return a custom response after deletion
        return Response({"detail": "Claim deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    # Optional: Add any custom behavior to the destroy method if needed
    def perform_destroy(self, instance):
        # Perform the deletion
        instance.delete()
