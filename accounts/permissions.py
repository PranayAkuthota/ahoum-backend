from rest_framework.permissions import BasePermission
from .models import UserProfile
from rest_framework.permissions import BasePermission

class IsFacilitator(BasePermission):
    def has_permission(self, request, view):
        try:
            profile = UserProfile.objects.get(
                user=request.user
            )
            return profile.role == "FACILITATOR"
        except UserProfile.DoesNotExist:
            return False


class IsSeeker(BasePermission):
    def has_permission(self, request, view):
        try:
            profile = UserProfile.objects.get(
                user=request.user
            )
            return profile.role == "SEEKER"
        except UserProfile.DoesNotExist:
            return False
class IsSeeker(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):
        return (
            request.user.userprofile.role
            == "SEEKER"
        )