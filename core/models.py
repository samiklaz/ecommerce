from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('Glocery', 'Glocery'),
    ('Beverages', 'Beverages'),
    ('Other Categories', 'Other Categories'),
)

QUANTITY = (
    ('Cups', 'Cups'),
    ('Bags', 'Bags'),
    ('Bottle', 'Bottle'),
    ('Rubber', 'Rubber'),
    ('undefined', 'undefined'),
)


def upload_location(instance, filename):
    file_path = 'product/{title}-{filename}'.format(
         title=str(instance.title), filename=filename)
    return file_path


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    price = models.BigIntegerField()
    discount_price = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default='Glocery', max_length=30)
    quantity_type = models.CharField(max_length=10, choices=QUANTITY, default='Cups')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:details", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={'slug': self.slug})


@receiver(post_delete, sender=Item)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=Item)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username