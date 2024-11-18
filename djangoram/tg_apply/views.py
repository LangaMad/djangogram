from django.views.generic import TemplateView

from .token import TOKEN
chat_id = '-1002212310184'
# views.py
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from .models import Apply
from .serializers import ApplySerializer


class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Сохраняем данные в базе данных
        self.perform_create(serializer)

        # Получаем данные из сериализатора
        apply_data = serializer.data
        name = apply_data['name']
        email = apply_data['email']
        phone = apply_data['phone']

        # Настройки для Telegram API
        telegram_bot_token = TOKEN
        telegram_chat_id = '-1002212310184'

        # Форматируем сообщение
        message = f"Новая заявка:\nИмя: {name}\nEmail: {email}\nТелефон: {phone}"

        # Отправляем сообщение в Telegram
        url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        data = {
            "chat_id": telegram_chat_id,
            "text": message
        }
        response = requests.post(url, data=data)

        # Проверка успешности отправки
        if response.status_code == 200:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Вывод детальной информации об ошибке
            error_message = response.json().get("description", "Ошибка при отправке заявки в Telegram")
            return Response(
                {"error": error_message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SendMessageView(TemplateView):
    template_name = 'tg_form.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        telegram_bot_token = TOKEN
        telegram_chat_id = '-1002212310184'

        # Форматируем сообщение
        message = f"Новая заявка:\nИмя: {name}\nEmail: {email}\nТелефон: {phone}"

        # Отправляем сообщение в Telegram
        url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        data = {
            "chat_id": telegram_chat_id,
            "text": message
        }
        response = requests.post(url, data=data)










