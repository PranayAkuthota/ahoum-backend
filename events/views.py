from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer

from accounts.permissions import (
    IsFacilitator
)


from .models import (
    Event,
    Enrollment
)

from .serializers import (
    EventSerializer,
    EnrollmentSerializer
)

from accounts.permissions import (
    IsFacilitator,
    IsSeeker
)

from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, filters

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class EventCreateView(
    generics.CreateAPIView
):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated,
        IsFacilitator
    ]

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )
class EventListView(
    generics.ListAPIView
):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Event.objects.all()
class EventDetailView(
    generics.RetrieveAPIView
):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Event.objects.all()
class EventUpdateView(
    generics.UpdateAPIView
):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated,
        IsFacilitator
    ]

    queryset = Event.objects.all()
class EventDeleteView(
    generics.DestroyAPIView
):

    permission_classes = [
        IsAuthenticated,
        IsFacilitator
    ]

    queryset = Event.objects.all()
from rest_framework.views import APIView


class EnrollEventView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsSeeker
    ]

    def post(
        self,
        request,
        pk
    ):

        event = Event.objects.get(pk=pk)

        enrollment, created = (
            Enrollment.objects.get_or_create(
                event=event,
                seeker=request.user,
                defaults={
                    "status": "ENROLLED"
                }
            )
        )

        if not created:
            return Response(
                {
                    "detail":
                    "Already enrolled"
                },
                status=400
            )

        return Response(
            EnrollmentSerializer(
                enrollment
            ).data,
            status=201
        )
class MyEnrollmentsView(
    generics.ListAPIView
):

    serializer_class = (
        EnrollmentSerializer
    )

    permission_classes = [
        IsAuthenticated,
        IsSeeker
    ]

    def get_queryset(self):

        return Enrollment.objects.filter(
            seeker=self.request.user
        )
class CancelEnrollmentView(
    APIView
):

    permission_classes = [
        IsAuthenticated,
        IsSeeker
    ]

    def post(
        self,
        request,
        pk
    ):

        enrollment = Enrollment.objects.get(
            event_id=pk,
            seeker=request.user
        )

        enrollment.status = (
            "CANCELLED"
        )

        enrollment.save()

        return Response(
            {
                "message":
                "Enrollment cancelled"
            }
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Enrollment


class CancelEnrollmentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        enrollment = Enrollment.objects.get(
            event_id=pk,
            seeker=request.user
        )

        enrollment.status = "CANCELLED"
        enrollment.save()

        return Response({
            "message": "Enrollment cancelled"
        })
from rest_framework import generics

from .models import Enrollment
from .serializers import EnrollmentSerializer


class MyEnrollmentsView(
    generics.ListAPIView
):

    serializer_class = EnrollmentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return Enrollment.objects.filter(
            seeker=self.request.user
        )
class EventListView(
    generics.ListAPIView
):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        queryset = Event.objects.all().order_by("id")

        language = self.request.query_params.get(
            "language"
        )

        location = self.request.query_params.get(
            "location"
        )

        if language:
            queryset = queryset.filter(
                language=language
            )

        if location:
            queryset = queryset.filter(
                location=location
            )

        return queryset
class EventListView(generics.ListAPIView):

    serializer_class = EventSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Event.objects.all().order_by("id")

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        "title",
        "description",
        "language",
        "location"
    ]
filter_backends = [
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]

ordering_fields = [
    "starts_at",
    "capacity",
    "created_at",
]

ordering = [
    "-created_at"
]