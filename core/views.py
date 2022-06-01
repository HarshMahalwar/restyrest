from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import student
# Create your views here.


@api_view(['GET'])
def home(request):
    api_ = {
        'create': "To create an student's information",
        'read': "To read the student's information",
        'update': "To update an student's information",
        'delete': "To delete an student's information"
    }
    return Response(api_)


@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def read(request):
    stu = student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update(request, pk):
    stu = student.objects.get(id=pk)
    serializer = StudentSerializer(instance=stu, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    stu = student.objects.get(id=pk)
    stu.delete()
    return Response('Student is deleted')
