from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField( null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=2999.99)
    slug = models.SlugField(unique=True)
    product_image = models.FileField(upload_to='product_image/', default='')
    # category = models.CharField(max_length=200, default='Vegetables')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.title + ' - ' + self.description

    class Meta:
        unique_together = ('title', 'slug')
