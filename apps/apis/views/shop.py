from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.shop.models import Category, Product, Store, Stock
from apps.apis.serializers.shop import CategorySerializer, ProductSerializer
from apps.apis.serializers.shop import StoreSerializer, StockSerializer

class categoryListAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        c_serializer = CategorySerializer(category, many = True)
        return Response(c_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        c_serializer = CategorySerializer(data = request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(c_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(c_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class categoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        c_serializer = CategorySerializer(category)
        return Response(c_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        c_serializer = CategorySerializer(category, data = request.data)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(c_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(c_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.filter(id=pk).first()
        category.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)

class productListAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        p_serializer = ProductSerializer(product, many = True)
        return Response(p_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        p_serializer = ProductSerializer(data = request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(p_serializer.data, status = status.HTTP_201.CREATED)
        else:
            return Response(p_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class productDetailAPIView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(id = pk).first()
        p_serializer = ProductSerializer(product)
        return Response(p_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        product = Product.objects.filter(id = pk).first()
        p_serializer = ProductSerializer(product, data = request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(p_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(p_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.filter(id = pk).first()
        product.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)

class storeListAPIView(APIView):
    def get(self, request):
        store = Store.objects.all()
        s_serializer = StoreSerializer(store, many = True)
        return Response(s_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        s_serializer = StoreSerializer(request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(s_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class storeDetailAPIView(APIView):
    def get(self, request, pk):
        store = Store.objects.filter(id = pk).first()
        s_serializer = StoreSerializer(store)
        return Response(s_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        store = Store.objects.filter(id = pk).first()
        s_serializer = StoreSerializer(store, data = request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(s_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = Store.objects.filter(id = pk).first()
        store.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)

class stockListAPIView(APIView):
    def get(self, request):
        stock = Stock.objects.all()
        s_serializer = StockSerializer(stock, many = True)
        return Response(s_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        s_serializer = StockSerializer(request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(s_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class stockDetailAPIView(APIView):
    def get(self, request, pk):
        stock = Stock.objects.filter(id = pk).first()
        s_serializer = StockSerializer(stock)
        return Response(s_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        stock = Stock.objects.filter(id = pk).first()
        s_serializer = StockSerializer(stock, data = request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(s_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stock = Stock.objects.filter(id = pk).first()
        stock.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)