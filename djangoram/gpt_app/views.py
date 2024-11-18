from django.shortcuts import render
from openai import OpenAI
from .keys import OPENAI_API_KEY
import requests

client = OpenAI(api_key=OPENAI_API_KEY)
from django.views.generic import TemplateView
# Create your views here.a

class ChatGPTView(TemplateView):
    template_name = 'chat.html'

    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('user_input', '')

        headers = {
           "Content-Type": "application/json",
           "Authorization": f"Bearer {OPENAI_API_KEY}"
       }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 150
        }
        response = requests.post(" https://api.openai.com/v1/chat/completions",
                                 headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            chat_response = data['choices'][0]['message']['content'].strip()
            title = chat_response[:20]
            context = self.get_context_data()
            context['response'] = chat_response
            context['title'] = title
            context['user_input'] = user_input
            return render(request, self.template_name, context)

