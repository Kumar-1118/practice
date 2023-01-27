from django.db import models

# Create your models here.


class ProductModel(models.Model):
   title=models.CharField(max_length=100)
   description=models.TextField()
   price=models.IntegerField()
   unique_code=models.CharField(max_length=100, unique=True)
   size=models.CharField(max_length=100, choices=[('10','10'), ('20','20'),('30','30')])
   quality=models.CharField(max_length=100, choices=[('high','high'),('low','low'),('medium','medium')])
   
   def __str__(self):
       return self.title
   
   class Meta:
       db_table = 'prod'
       
       
class ColourModel(models.Model):
    product=models.ForeignKey(ProductModel, related_name='clr_f', on_delete=models.CASCADE)
    colour=models.CharField(max_length=100,  choices=[('red','red'),('blue','blue'),('green','green'),('black','black')])
    
    class Meta:
        db_table = 'color'
        
    
    # @property
    # def category_name(self):
    #     return self.prod.title


class ImageModel(models.Model):
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media')
    
    
    class Meta:
        db_table = 'image'
      
    # @property
    # def category_name(self):
    #     return self.prod.title
  
        

