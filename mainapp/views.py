from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import(
    User,Todo,UserSerializer, TodoSerializer
)

from rest_framework.response import Response


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
    def list(self, request, *arg, **kwarg):
        todoes=Todo.objects.filter(user=request.user)
        return Response(TodoSerializer(instance=todoes,many=True).data)
