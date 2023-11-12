from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.title
