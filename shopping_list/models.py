from django.db import models
from django.contrib.auth.models import User
from tools.utilities import get_current_user

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=50, null=False, blank=False)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_who_created_shop", default=get_current_user)
    current = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.shop_name


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, blank=False)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_created_category", default=get_current_user)
    current = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(blank=True, null=True)
    default_quantity = models.IntegerField(null=False, blank=False, default=1)
    default_unit = models.CharField(max_length=30, null=False, blank=False, default="package")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category", default=0)
    default_source = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="buy_here_if_possible", default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_created_product", default=get_current_user)
    notes = models.TextField(null=True, blank=True)
    current = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.product_name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name

    def __str2__(self):
        return self.default_source


class List_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_of_list_item")
    date_created = models.DateTimeField(auto_now=True)
    bought = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    date_bought = models.DateTimeField(default=None, blank=True, null=True)
    default_source = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="where_to_buy", default=0)
    actual_source = models.ForeignKey(Shop, on_delete=models.CASCADE, default=None, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_put_item_on_list")
    shopper = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_bought_item", default=None, null=True, blank=True)
    quantity_required = models.IntegerField(default=1)
    quantity_bought = models.IntegerField(default=0)
    creator_notes = models.TextField(null=True, blank=True)
    buyer_notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['date_created']
        verbose_name = "list item"
        verbose_name_plural = "list items"

    def save(self, *args, **kwargs):
        if not self.creator:
            self.creator = get_current_user()
            print(self.creator)
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.product.product_name} | ordered by {self.creator}"

    def __category__(self):
        return self.product.category

    def __default_source__(self):
        return self.product.default_source



    
