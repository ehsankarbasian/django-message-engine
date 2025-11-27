from django.urls import path

from .views import SendVerifyMessageView, SendWelcomeMessageView


urlpatterns = [
    path("send_message/verify", SendVerifyMessageView.as_view()),
    path("send_message/welcome", SendWelcomeMessageView.as_view()),
]
