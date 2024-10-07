from rest_framework import generics,status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import MenuItem,Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MenuItemSerializer,CategorySerializer
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


# class MenuItemView(generics.ListCreateAPIView):
#     """
#     include listapiview and createapiview 
#     """
#     queryset = MenuItem.objects.select_related('category').all()
#     serializer_class = MenuItemSerializer

#     def get_serializer_context(self):
#         # Add 'request' to the serializer context
#         context = super().get_serializer_context()
#         context['request'] = self.request
#         return context


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 

class MenuItemView(APIView):
    def get(self, request):
        """
        Handle GET request to list all menu items
        """
        menu_items = MenuItem.objects.all()
        category_name = request.query_params.get('category')
        price = request.query_params.get('price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage',default = 2)
        page = request.query_params.get('page', default = 1)
        print(f'ordering........................{request}')
        
        if category_name:
            menu_items = menu_items.filter(category__title = category_name)
        if price:
            menu_items = menu_items.filter(price__lte = price)
        if search:
            menu_items = menu_items.filter(title__icontains = search)
        if ordering:
            ordering_fields = ordering.split(",")
            menu_items = menu_items.order_by(*ordering_fields)
        
        paginator = Paginator(menu_items,per_page=perpage)
        try:
            menu_items = paginator.page(number=page)
        except EmptyPage:
            menu_items = []

        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle post request to list all menu items
        """
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            datas = serializer.validated_data #to see datas before save them
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'POST'])
# def menu_item_view(request):
#     if request.method == 'GET':
#         # Handle GET request to list all menu items
#         menu_items = MenuItem.objects.all()
#         serializer = MenuItemSerializer(menu_items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         # Handle POST request to create a new menu item
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    """
    update (put), delete and retrieve single one
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer