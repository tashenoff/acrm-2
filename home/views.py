from django.shortcuts import render
from main.models import Main
from home.serializers import HomeListSerializer
from main.models import Main
from customer.models import Customer
from rest_framework import generics


# def home(request):
#     return render(request, 'home/index.html')

def home(request):
    Customer_list = Customer.objects.all()
    context = {'clintList': Customer_list}
    return render(request, 'home/index.html', context)


class RecordCreateView(generics.CreateAPIView):
    serializer_class = HomeListSerializer
    queryset = Main.objects.all()


class RecordListView(generics.ListAPIView):
    serializer_class = HomeListSerializer
    queryset = Main.objects.all()


class RecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeListSerializer
    queryset = Main.objects.all()
