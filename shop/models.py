from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)
    ordering = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)
    
    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)
    description = models.TextField(blank=True, null=True)
    featured_item = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
    
    def __str__(self):
        return self.title