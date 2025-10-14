from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('category_name', max_length=50)
    img = models.ImageField('category_img', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_id')
    name = models.CharField('product_name', max_length=50)
    img = models.ImageField('product_img', upload_to='images')
    price = models.PositiveIntegerField('product_price')

    def __str__(self):
        return self.name
        

class Cart(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_id')