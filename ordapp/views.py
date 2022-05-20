from rest_framework.generics import CreateAPIView

from ordapp.bot import send_message
from ordapp.models import Order
from ordapp.serializers import OrderSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        '''
        Переопределим метод post.
        '''
        send_message(request.data)
        return self.create(request, *args, **kwargs)
