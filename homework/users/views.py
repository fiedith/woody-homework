from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

# User requirement: create, delete
class UserView(APIView):
     # create user
    @swagger_auto_schema(request_body=UserSerializer, operation_id="Create user")
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # if not valid
        return JsonResponse(serializer.errors, status=404)

    # delete user
    @swagger_auto_schema(operation_id="Delete user")
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse(
            {"message": "deleted"},
            status=204
        )