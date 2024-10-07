from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView




# Create your views here.
# @csrf_exempt
# def books(request):
#     if request.method == "GET":
#         books = Book.objects.all().values()
#         return JsonResponse({"books": list(books)})
#     elif request.method == "POST":
#         title = request.POST.get("title")
#         author = request.POST.get("author")
#         price = request.POST.get("price")

#         book = Book(title=title, author=author, price=price)

#         try:
#             book.save()

#         except IntegrityError:
#             return JsonResponse(
#                 {"error": "true", "message": "required field missing"}, status=400
#             )

#         return JsonResponse(model_to_dict(book), status=201)



@api_view(['POST',"GET"])
def books(request):
    return Response('list of the books: ',status  = status.HTTP_200_OK)


# write class base view via def :
class BookList(APIView):
    """
    write api view apiview of drf
    """
    def get(self,request): # if method was get 
        print(request)
        author = request.GET.get('author')
        if author:
            return Response({'message':f'list of objects by {author}'},status.HTTP_200_OK)
        return Response({'message':'list of objects'},status.HTTP_200_OK)
    
    def post(self,request):
        print(request)
        print(request.data)
        author = request.data.get('author')
        print(author)
        return Response({'message':'book created'},status.HTTP_201_CREATED)