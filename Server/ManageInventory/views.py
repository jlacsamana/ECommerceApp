from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ManageInventory.models import InventoryItem
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def test(request):
    return JsonResponse({"message": "Test Successful: Inventory Working"})


def route_handler(request):
    """a handler for paramaterless requests"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # load in mandatory data
            newItem = InventoryItem.objects.create(
                upc=data["upc"],
                name=data["name"],
                description=data["description"],
                is_second_hand=data["is_second_hand"],
            )
            # load in optional fields if provided
            if data.get("manufacturer") != None:
                newItem.manufacturer = data["manufacturer"]

            if data.get("product_series") != None:
                newItem.product_series = data["product_series"]

            if data.get("quantity") != None:
                newItem.quantity = data["quantity"]
            newItem.save()
            return JsonResponse(
                {"msg": "Item added", "resp": InventoryItemParser(newItem)}, status=200
            )
        except:
            return JsonResponse({"msg": "Could Not Add"}, status=500)
    elif request.method == "GET":
        try:
            queryKey = request.GET.get("queryKey", "")
            queryKeyVal = request.GET.get("queryKeyVal", "")
            queryOffset = request.GET.get("queryAmt", 0)
            queryAmt = request.GET.get("queryAmt", 50)
            match queryKey:
                case "name":
                    rawResults = InventoryItem.objects.filter(
                        name__contains=queryKeyVal
                    )
                case "manufacturer":
                    rawResults = InventoryItem.objects.filter(
                        manufacturer__contains=queryKeyVal
                    )
                case "series":
                    rawResults = InventoryItem.objects.filter(
                        product_series__contains=queryKeyVal
                    )
                case _:
                    rawResults = InventoryItem.objects.all()
            subset = rawResults[queryOffset:]
            if queryAmt < len(subset):
                subset = subset[:queryAmt]
            parsedSubset = list(map(InventoryItemParser, subset))
            return JsonResponse(
                {"msg": "Ok - Items fetched", "resp": parsedSubset}, status=200
            )

            return
        except:
            return JsonResponse({"msg": "Could Not Make Query"}, status=500)


def route_handler_with_id(request, id):
    """a handler for requests that take an id as a parameter"""
    if request.method == "PATCH":
        try:
            retrItem = InventoryItem.objects.get(pk=id)
            data = json.loads(request.body)
            # required fields
            retrItem.upc = data["upc"]
            retrItem.name = data["name"]
            retrItem.description = data["description"]
            retrItem.is_second_hand = data["is_second_hand"]

            # optional fields
            if data.get("manufacturer") != None:
                retrItem.manufacturer = data["manufacturer"]

            if data.get("product_series") != None:
                retrItem.product_series = data["product_series"]

            if data.get("quantity") != None:
                retrItem.quantity = data["quantity"]

            retrItem.save()
            return JsonResponse(
                {"msg": "OK - Item Edited", "resp": InventoryItemParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)
    elif request.method == "GET":
        try:
            retrItem = InventoryItem.objects.get(pk=id)
            return JsonResponse(
                {"msg": "OK - Fetched", "data": InventoryItemParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)
    elif request.method == "DELETE":
        try:
            retrItem = InventoryItem.objects.get(pk=id)
            retrItem.delete()
            return JsonResponse(
                {"msg": "OK - Deleted", "data": InventoryItemParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)


def InventoryItemParser(item: InventoryItem):

    return {
        "id": item.id,
        "upc": item.upc,
        "name": item.name,
        "description": item.description,
        "manufacturer": item.manufacturer,
        "product_series": item.product_series,
        "is_second_hand": item.is_second_hand,
        "quantity": item.quantity,
    }
