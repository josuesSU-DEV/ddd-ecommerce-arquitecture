from rest_framework import serializers
from products.serializers import ProductSerializer
from products.serializers import UserSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cartitem_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"