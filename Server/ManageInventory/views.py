from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def test(request):
    return JsonResponse({'message': 'Test Successful: Inventory Working'})

@api_view(['GET'])
def get_inventory_items(request):
    ''''''

@api_view(['GET'])
def get_inventory_item(request, id):
    ''''''

@api_view(['POST'])
def post_new_inventory_item(request):
    ''''''

@api_view(['PATCH'])
def edit_inventory_item(request):
    ''''''

@api_view(['DELETE'])
def delete_inventory_item(request, id):
    ''''''
