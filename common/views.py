from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from rest_framework import viewsets, generics
from .serializers import UserSerializer
from .models import User
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #filter_backends = [DjangoFilterBackend]
    #filter_backends = ['broker_id']

class IDList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        b_id = self.request.query_params.get('b_id')
        if username is not None and b_id is not None:
            queryset = queryset.filter(username=username, broker_id=b_id)
        return queryset

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})