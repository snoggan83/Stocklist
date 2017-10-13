from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stocklist
from .serializers import StocklistSerializer
from .models import Stocklist, Stock

# Lists all stocklists or creates a new one
class StockListFull(APIView):

    def get(self, request):
        stocklists = Stocklist.objects.all()
        serializer = StocklistSerializer(stocklists, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def index(request):
    all_stocklists = Stocklist.objects.all()
    context = {"all_stocklists": all_stocklists}
    return render(request, "stocklist/index.html", context)

def detail(request, stocklist_id):
    stocklist = get_object_or_404(Stocklist, pk=stocklist_id)
    return render(request, "stocklist/detail.html", {"stocklist": stocklist})

def portfolio(request, stocklist_id):
    stocklist = get_object_or_404(Stocklist, pk=stocklist_id)
    try:
        selected_stock = stocklist.stock_set.get(pk=request.POST["stock"])
    except (KeyError, Stock.DoesNotExist):
        return render(request, "stocklist/detail.html", {"stocklist": stocklist, "error_message": "Not a valid stock"})
    else:
        selected_stock.in_portfolio = True
        selected_stock.save()
        return render(request, "stocklist/detail.html", {"stocklist": stocklist})