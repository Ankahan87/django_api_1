from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Review
from .serializers import ProductDetailsSerializer, ProductListSerializer, ReviewSerializer


@api_view(['GET'])
def products_list_view(request):
    all_prod = Product.objects.all()
    ser = ProductListSerializer(all_prod, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            prod = Product.objects.filter(id=product_id)
            rev = Review.objects.filter(product=product_id)
            ser_rev = ReviewSerializer(rev, many=True)
            ser_prod = ProductDetailsSerializer(prod)
            return Response(ser_prod.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
