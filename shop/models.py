from django.db import models

class AbstractVariant(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.TextField(max_length=1000)

    class meta:
        abstract  = True
    

    def __str__(self):
        return self.name


class Category(AbstractVariant):
    pass



class Type(AbstractVariant):
    pass



class Brand(AbstractVariant):
    pass


class Color(models.Model):
    hex = models.CharField(max_length=10)


    def __str__(self):
        return self.hex
    
class Size(models.Model):
    SIZE_CHOICES = (
        ('xs', 'xs'),
        ('s', 's'),
        ('m', 'm'),
        ('l', 'l'),
        ('xl', 'xl'),
        ('2xl', '2xl'),
        ('3xl', '3xl'),
        ('34', '34'), ('35', '35'), ('36', '36'),
        ('37', '37'), ('38', '38'), ('39', '39'),
        ('40', '40'), ('41', '41'), ('42', '42'),
        ('43', '43'), ('44', '44'), ('45', '45'),
    )

    size = models.CharField(max_length=4, choices=SIZE_CHOICES)

    def __str__(self):
        return self.size

class Product(models.Model):
    name =  models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.TextField(max_length=1000)
    description = models.TextField(max_length=600)
    blend = models.CharField(max_length=255)
    discount = models.PositiveIntegerField(null=True, blank=True)
    

    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    

    def __str__(self):
        category_names = []

        for c in self.category.all():
            category_names.append(c.name)
    
        return f"{', '.join(category_names)} -> {self.type} -> {self.name} ({self.price}$)"