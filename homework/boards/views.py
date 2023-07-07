from django.contrib.auth import get_user_model
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Board
from .serializers import BoardSerializer

# posts list
class BoardListCreateView(APIView):
    # retrieve all posts
    @swagger_auto_schema(operation_id="Get posts")
    def get(self, request):
        # take all board objects
        boards = Board.objects.all()
        # put all boards into serializer, specify many=True
        serializer = BoardSerializer(boards, many=True)
        return JsonResponse(serializer.data)

    # create post
    @swagger_auto_schema(request_body=BoardSerializer, operation_id="Create post")
    def post(self, request):
        serializer = BoardSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=201)
        # if invalid
        return JsonResponse(serializer.errors, status=404)


# individual posts
class BoardDetailView(APIView):
    @swagger_auto_schema(operation_id="Get specific post")
    def get(self, request, pk):
        try:
            # get corresponding post using board pk
            board = Board.objects.get(pk=pk)
            serializer = BoardSerializer(board)
            return JsonResponse(serializer.data)
        # error if board does not exist
        except Board.DoesNotExist:
            return JsonResponse({"message": "post not found"}, status=404)

    # delete specific post
    @swagger_auto_schema(operation_id="Delete specific post")
    def delete(self, request, pk):
        try:
            # get corresponding post using board pk
            board = Board.objects.get(pk=pk)
            board.delete()
            # status 204 = successful delete
            return JsonResponse({"message": "deleted"}, status=204)
        # error if board does not exist
        except Board.DoesNotExist:
            return JsonResponse({"message": "post not found"}, status=404)


# class BoardListCreateView(generics.ListCreateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(
#         operation_id="Create board",
#         request_body=BoardSerializer,
#         responses={201: BoardSerializer()}
#     )
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # Set the author field to the user instance
#         serializer.validated_data['author'] = request.user
#
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
# class BoardDetailView(generics.RetrieveDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(
#         operation_id="Retrieve board",
#         responses={200: BoardSerializer()}
#     )
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
#
#     @swagger_auto_schema(
#         operation_id="Delete board",
#         responses={204: None}
#     )
#     def delete(self, request, *args, **kwargs):
#         return super().delete(request, *args, **kwargs)
#
#     def perform_destroy(self, instance):
#         if instance.author != self.request.user:
#             raise PermissionDenied("You don't have permission to delete this board.")
#         return super().perform_destroy(instance)