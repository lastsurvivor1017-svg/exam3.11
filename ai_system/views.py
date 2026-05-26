from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import simple_chatbot_response


class ChatBotView(APIView):
    def post(self, request):
        message = request.data.get("message")
        response = simple_chatbot_response(message)
        
        return Response({
            "message": message,
            "response": response
        })
    

def ai(request):
    return render(request, 'ai/ai.html')