from django.urls import path

from .views import (
    EventCreateView,
    EventListView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
    EnrollEventView,
MyEnrollmentsView,
CancelEnrollmentView
)

urlpatterns = [

    path(
        "",
        EventListView.as_view()
    ),

    path(
        "create/",
        EventCreateView.as_view()
    ),

    path(
        "<int:pk>/",
        EventDetailView.as_view()
    ),

    path(
        "<int:pk>/update/",
        EventUpdateView.as_view()
    ),

    path(
        "<int:pk>/delete/",
        EventDeleteView.as_view()
    ),
    path(
    "<int:pk>/enroll/",
    EnrollEventView.as_view()
),

path(
    "<int:pk>/cancel/",
    CancelEnrollmentView.as_view()
),

path(
    "my-enrollments/",
    MyEnrollmentsView.as_view()
),
path(
    "<int:pk>/cancel/",
    CancelEnrollmentView.as_view()
),

]
