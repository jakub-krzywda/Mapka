from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
