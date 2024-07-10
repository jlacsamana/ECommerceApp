from django.shortcuts import render
from django.http import JsonResponse
from ManageListings.models import Listing
from ManageInventory.models import InventoryItem
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q


# Create your views here.


def test(request):
    return JsonResponse(
        {"message": "Test Successful: Test Successful: Listings Working"}
    )


@csrf_exempt
def route_handler(request):
    """a handler for paramaterless requests"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # load in mandatory data
            newItem = Listing.objects.create(
                item=InventoryItem.objects.get(pk=data["item"]),
                price=data["price"],
                additional_description=data["additional_description"],
            )

            # load in optional fields if provided
            if data.get("on_WooCommerce") != None:
                newItem.manufacturer = data["on_WooCommerce"]

            if data.get("on_Ebay") != None:
                newItem.on_Ebay = data["on_Ebay"]

            if data.get("on_Amazon") != None:
                newItem.on_Amazon = data["on_Amazon"]

            if data.get("on_FBMarketplace") != None:
                newItem.on_FBMarketplace = data["on_FBMarketplace"]
            newItem.save()
            return JsonResponse(
                {"msg": "Item added", "resp": ListingParser(newItem)}, status=200
            )
        except Exception as e:
            return JsonResponse({"msg": "Could Not Add"}, status=500)
    elif request.method == "GET":
        try:
            queryKey = request.GET.get("queryKey", "")
            queryKeyVal = request.GET.get("queryKeyVal1", "")
            queryKeyVal2 = request.GET.get("queryKeyVal2", "")
            queryOffset = request.GET.get("queryAmt", 0)
            queryAmt = request.GET.get("queryAmt", 50)
            match queryKey:
                case "platform":
                    rawResults = []
                    platforms = queryKeyVal.split(",")
                    if "woocommerce" in platforms:
                        rawResults.extend(
                            list(Listing.objects.filter(Q(on_WooCommerce=True)))
                        )
                    if "ebay" in platforms:
                        rawResults.extend(list(Listing.objects.filter(Q(on_Ebay=True))))
                    if "amazon" in platforms:
                        rawResults.extend(
                            list(Listing.objects.filter(Q(on_Amazon=True)))
                        )
                    if "fbmarketplace" in platforms:
                        rawResults.extend(
                            list(Listing.objects.filter(Q(on_FBMarketplace=True)))
                        )
                case "pricefilter":
                    match queryKeyVal:
                        case "gt":
                            rawResults = list(
                                Listing.objects.filter(price__gt=float(queryKeyVal2))
                            )
                        case "lt":
                            rawResults = list(
                                Listing.objects.filter(price__lt=float(queryKeyVal2))
                            )
                        case "gte":
                            rawResults = list(
                                Listing.objects.filter(price__gte=float(queryKeyVal2))
                            )
                        case "lte":
                            rawResults = list(
                                Listing.objects.filter(price__lte=float(queryKeyVal2))
                            )
                        case "exact":
                            rawResults = list(
                                Listing.objects.filter(price__exact=float(queryKeyVal2))
                            )
                        case _:
                            rawResults = Listing.objects.all()
                case "item":
                    rawResults = Listing.objects.filter(
                        item__name__contains=queryKeyVal
                    )
                case _:
                    rawResults = Listing.objects.all()
            subset = rawResults[queryOffset:]
            if queryAmt < len(subset):
                subset = subset[:queryAmt]
            parsedSubset = list(map(ListingParser, subset))
            return JsonResponse(
                {"msg": "Ok - Items fetched", "resp": parsedSubset}, status=200
            )

            return
        except:
            return JsonResponse({"msg": "Could Not Make Query"}, status=500)


@csrf_exempt
def route_handler_with_id(request, id):
    """a handler for requests that take an id as a parameter"""
    if request.method == "PATCH":
        try:
            retrItem = Listing.objects.get(pk=id)
            data = json.loads(request.body)
            # required fields
            retrItem.upc = data["price"]
            retrItem.name = data["additional_description"]

            # optional fields
            if data.get("on_WooCommerce") != None:
                retrItem.on_WooCommerce = data["on_WooCommerce"]

            if data.get("on_Ebay") != None:
                retrItem.on_Ebay = data["on_Ebay"]

            if data.get("on_Amazon") != None:
                retrItem.on_Amazon = data["on_Amazon"]

            if data.get("on_FBMarketplace") != None:
                retrItem.on_FBMarketplace = data["on_FBMarketplace"]

            retrItem.save()
            return JsonResponse(
                {"msg": "OK - Item Edited", "resp": ListingParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)
    elif request.method == "GET":
        try:
            retrItem = Listing.objects.get(pk=id)
            return JsonResponse(
                {"msg": "OK - Fetched", "data": ListingParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)
    elif request.method == "DELETE":
        try:
            retrItem = Listing.objects.get(pk=id)
            retrItem.delete()
            return JsonResponse(
                {"msg": "OK - Deleted", "data": ListingParser(retrItem)},
                status=200,
            )
        except:
            return JsonResponse({"msg": "Not Found"}, status=400)


def ListingParser(listing: Listing):

    return {
        "item": listing.item.id,
        "price": listing.price,
        "additional_description": listing.additional_description,
        "on_WooCommerce": listing.on_WooCommerce,
        "on_Ebay": listing.on_Ebay,
        "on_Amazon": listing.on_Amazon,
        "on_FBMarketplace": listing.on_FBMarketplace,
    }
