from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Log
from .serializers import LogSerializer

class LogAPIView(APIView):
    def get(self, request):
        logs = Log.objects.all()
        source_ip = request.query_params.get('source_ip')
        level = request.query_params.get('level')
        timestamp = request.query_params.get('timestamp')

        if source_ip:
            logs = logs.filter(source_ip=source_ip)
        if level:
            logs = logs.filter(level=level)
        if timestamp:
            logs = logs.filter(timestamp=timestamp)

        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the SIEM API. Use /api/logs/ to POST and GET logs.")
