from django.db import models




class PropertyTypeModel(models.Model):
    property_type=models.CharField(max_length=254)

    def __str__(self):
        return f"{self.property_type}"



class BallincolligPropertyModel(models.Model):
    """ model for Ballincolig Properties"""
    area = models.CharField(max_length=254)
    full_address = models.TextField()
    price = models.IntegerField(default=200000)
    property_type = models.ForeignKey(PropertyTypeModel, on_delete=models.CASCADE)
    sold_date = models.CharField(max_length=254)
    longitude = models.CharField(max_length=254)
    latitude = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.full_address}"


class BallincolligPropertyListModel(models.Model):

    area = models.CharField(max_length=254)
    full_address = models.TextField()
    price = models.IntegerField(default=200000)
    property_type = models.ForeignKey(PropertyTypeModel, on_delete=models.CASCADE)
    sold_date = models.CharField(max_length=254)
    longitude = models.CharField(max_length=254)
    latitude = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.full_address}"
