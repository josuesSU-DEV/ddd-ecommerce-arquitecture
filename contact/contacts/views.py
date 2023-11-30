from rest_framework import generics
from rest_framework.response import Response

class EnviarMensajeAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        # Lógica para enviar mensaje
        # ...

        return Response({"mensaje": "Mensaje enviado con éxito"})
