from rest_framework import serializers
from .models import MenuItem,Category
from decimal import Decimal
import bleach




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

# class MenuItemSerializer(serializers.ModelSerializer):
#     stock = serializers.IntegerField(source = 'inventory')
#     price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
#     # category = CategorySerializer()
#     class Meta:
#         model = MenuItem
#         fields = ['title','price','stock','price_after_tax','category']
#         depth = 1

#     def calculate_tax(self,product):
#         """
#         increase price
#         """
#         return product.price*Decimal('1.1')
    
class MenuItemSerializer(serializers.ModelSerializer):
    """
    menu item serializer
    """
    stock = serializers.IntegerField(source='inventory',min_value=0)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only = True)
    category_id =  serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)

    def validate_title(self, value):
        return bleach.clean(value)
    
    def calculate_tax(self, product):
        """
        Increase price by 10%
        """
        return product.price * Decimal('1.1')

    def validate_price(self, value): #define some custom limition for price , it should called validate_field
        if value%2 == 1:
            raise serializers.ValidationError('The price must be divisible by two')
    
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        depth = 1
        extra_kwargs = {
            'stock':{'source':'inventory', 'min_value': 0}
        }


    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title']) #preventing user to insert html forms or script into title 
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)