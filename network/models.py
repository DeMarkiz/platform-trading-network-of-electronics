from django.db import models


class NetworkNode(models.Model):
    TYPE_CHOICES = [
        ('factory', 'Завод'),
        ('retail', 'Розничная сеть'),
        ('entrepreneur', 'ИП'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_level(self):
        level = 0
        current = self
        while current.supplier:
            level += 1
            current = current.supplier
        return level


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()
    supplier = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.model})"