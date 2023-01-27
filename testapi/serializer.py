from rest_framework import serializers
from testapi.models import ProductModel, ImageModel, ColourModel



class TestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    price=serializers.IntegerField()
    unique_code=serializers.CharField(max_length=100)
    size=serializers.CharField(max_length=100)
    quality=serializers.CharField(max_length=100)
   
    
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'description',
            'price',
            'unique_code',
            'size',
            'quality',             
        )
        
     
class ImageSerializer(serializers.ModelSerializer):
    # product = ProductModelSerializer()
    # image=serializers.ImageField()
    img=TestSerializer(read_only=True, many=True)
    
    class Meta:
        model=ImageModel
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ColourModel
        fields = '__all__'
    clr_f = TestSerializer(read_only=True, many=True)
    
   
   
# class SavedSerializer(serializers.ModelSerializer):
#     unit_id = serializers.PrimaryKeyRelatedField(
#         source='product',
#         queryset=ProductModel.objects.all()
#     )
#     unit = ProductModelSerializer(read_only=True)

#     class Meta:
#         model = ImageModel
#         fields = [
#             'id',
#             'unit_id',
#             'unit'
#         ]