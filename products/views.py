from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from .models import Product

from .serializers import ProductSerializer



# Retrieve all products or filter them by category and price range

@api_view(['GET'])

def product_list(request):

  category = request.query_params.get('category')

  min_price = request.query_params.get('min_price')

  max_price = request.query_params.get('max_price')



  products = Product.objects.all()



  if category:

    products = products.filter(category=category)

  if min_price:

    products = products.filter(price__gte=min_price)

  if max_price:

    products = products.filter(price__lte=max_price)



  serializer = ProductSerializer(products, many=True)

  return Response(serializer.data)



# Create a new product

@api_view(['POST'])

def product_create(request):

  serializer = ProductSerializer(data=request.data)

  if serializer.is_valid():

    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Retrieve, update, or delete a product by ID

@api_view(['GET', 'PUT', 'DELETE'])

def product_detail(request, pk):

  try:

    product = Product.objects.get(pk=pk)

  except Product.DoesNotExist:

    return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)



  if request.method == 'GET':

    serializer = ProductSerializer(product)

    return Response(serializer.data)



  elif request.method == 'PUT':

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



  elif request.method == 'DELETE':

    product.delete()

    return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


