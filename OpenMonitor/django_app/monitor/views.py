from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class PingView(APIView):
    def get(self, request):
        return Response({"message": "pong"})

class OpenProjectStatusView(APIView):
    def get(self, request):
        try:
            resp = requests.get("https://community.openproject.com/api/v3/projects", timeout=5)
            status = resp.status_code
        except requests.RequestException:
            status = "error"
        return Response({"openproject_status": status})
