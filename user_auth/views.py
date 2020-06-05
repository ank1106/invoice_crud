from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer


class AuthAPI(APIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
	        user = authenticate(username=ser.data["username"], 
	                    password=ser.data["password"])
	        if user:
	        	return JsonResponse({"status":"OK","token":getAuthToken(user)}, status=200)         
        	return JsonResponse({"error":"invalid username or password"})
        return JsonResponse(ser.errors, status=400)


def getAuthToken(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)
