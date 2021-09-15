from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField('Kategoriya',max_length=50)
    slug = models.SlugField('Havola',max_length=50, unique=True)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField("Nomi",max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='catalog',null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField("Havola",max_length=50, unique=True)
    image = models.ImageField(upload_to='image',null=True)
    info = models.TextField('Qisqa malumot',blank=True)
    desc = models.TextField(blank=True)
    old_price = models.PositiveIntegerField(default=0, null=True)
    price = models.PositiveIntegerField(default=0)
    payment = models.PositiveIntegerField(default=0)
    add_date = models.DateField('Qoshilgan vaqt',auto_now_add=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.title
class Offer(models.Model):
    offer_name = models.CharField(max_length=200)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    visits = models.PositiveIntegerField(default=0)
    orders = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    db_link = models.SlugField(max_length=50)
    def __str__(self):
        return self.offer_name + " - " + self.db_link
class Order(models.Model):
    region = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(verbose_name='Mahsulot soni' , default=0)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(verbose_name="Sotildi", default=False, help_text="Sotilgan bo'lsa belgilang!!!")
    def __str__(self):
        return self.tel
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_photo = models.ImageField(verbose_name="Shaxsiy Surat", upload_to='profile_images/',null=True, blank=True)
    card_number = models.CharField(max_length=16, verbose_name='Karta raqami',null=True, blank=True)
    card_vendor = models.CharField(max_length=100, verbose_name="Karta egasi",null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name="Telefon raqam",null=True, blank=True)
    income = models.PositiveBigIntegerField(verbose_name="Daromad", null=True, blank=True)
    hold = models.PositiveBigIntegerField(verbose_name="Hold", null=True, blank=True)

