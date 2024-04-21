from rest_framework import serializers
from models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']

class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits = 15, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
