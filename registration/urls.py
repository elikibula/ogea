from django.urls import path
from registration.views import ParticipantRegistrationView, dashboard, register_participant

app_name = 'registration'

urlpatterns = [
    path('registration/', ParticipantRegistrationView.as_view(), name='registration'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register_participant, name='register'),
]


