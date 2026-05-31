from rest_framework import serializers
from .models import Event
from rest_framework import serializers
from .models import Event, Enrollment

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event

        fields = [
            "id",
            "title",
            "description",
            "language",
            "location",
            "starts_at",
            "ends_at",
            "capacity",
            "created_by",
            "created_at",
            "updated_at"
        ]

        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at"
        ]
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"

        read_only_fields = [
            "created_by",
            "created_at",
            "updated_at",
        ]

class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = [
            "seeker",
            "event",
            "created_at",
            "updated_at",
        ]