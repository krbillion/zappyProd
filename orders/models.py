from django.db import models
from carts.models import CartItem
from django.contrib.auth import get_user_model
# from mainapp.models import Profile
# Create your models here.
User = get_user_model()


STATUS_CHOICES = (
    ("Started","Started"),
    ("Abandoned","Abandoned"),
    ("Finished","Finished"),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    final_total = models.DecimalField(default=100.00, max_digits=1000, decimal_places=2)
    location = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id
