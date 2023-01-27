from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from testapi.serializer import TestSerializer

from testapi.models import ProductModel, ImageModel, ColourModel
from testapi.serializer import *
from django.http import Http404
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from .serializer import ImageSerializer, ColorSerializer, TestSerializer



# class ProdView(APIView):
#     def get(self,request):
#         x=ProductModel.objects.all()
#         serializer=TestSerializer(x,many=True)
#         return Response(serializer.data)
    
    # def get_object(self, pk):
    #     try:
    #         details=ProductModel.objects.get(pk=pk)
    #         return details
    #     except:
    #         return Http404
        
    # def patch(self, request, pk):
    #     qs=self.get_object(pk)
    #     serializer=TestSerializer(qs,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)


class ListProduct(ListAPIView):
    serializer_class=TestSerializer    
    queryset=ProductModel.objects.all()
    
class ProdProduct(RetrieveUpdateAPIView):
     serializer_class=TestSerializer
     queryset=ProductModel.objects.all()



class ListImage(ListAPIView):
    serializer_class=ImageSerializer
    queryset=ImageModel.objects.all()

    
class ImageProd(RetrieveUpdateAPIView):
    serializer_class=ImageSerializer
    queryset=ImageModel.objects.all()


class ListColor(ListAPIView):
    serializer_class=ColorSerializer    
    queryset=ColourModel.objects.all()
    
class ColorProd(RetrieveUpdateAPIView):
     serializer_class=ColorSerializer
     queryset=ColourModel.objects.all()
     
     

    
    


    

