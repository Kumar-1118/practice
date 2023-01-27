from django.contrib import admin
from .models import ProductModel, ColourModel, ImageModel

# Register your models here.


admin.site.register(ProductModel)
admin.site.register(ColourModel)
admin.site.register(ImageModel)