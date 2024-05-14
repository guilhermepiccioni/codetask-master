from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=250, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
