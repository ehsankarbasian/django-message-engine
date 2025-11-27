from django.shortcuts import HttpResponse
from django.views.generic.base import View

from message_engine.message_facade import MessageFacade


class SendMessageView(View):
    
    def get(self, request):
        
        if not request.user.is_anonymous:
            MessageFacade.send_verify_message(user=request.user, context=None)
            return HttpResponse('OK')

        return HttpResponse('request.user is Ananymous')
