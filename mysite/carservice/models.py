from django.db import models
from django.urls import reverse


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.street


class RentalBase(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    logo = models.ImageField(upload_to='logo', null=True, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    rental_base = models.ForeignKey(RentalBase, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    car_mark = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    num_of_seats = models.IntegerField()
    cost_per_day = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('car_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.car_model


class Client(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Seller(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    salary = models.FloatField(default=3000)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    days = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse('order_details', kwargs={'pk': self.pk})

    def __str__(self):
        return "Client: {}, Seller: {}, Car: {}".format(self.client, self.seller, self.car.car_model)


class OrdersArchive(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=False)
    car_score = models.IntegerField(default=0)
    order_score = models.IntegerField(default=0)
    approved = models.BooleanField(default=True)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return "Order: {}, Car score: {}, Order score: {}".format(self.order.id, self.car_score, self.order_score)


class Repairments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    engine = models.BooleanField(default=False)
    tire = models.BooleanField(default=False)
    door = models.BooleanField(default=False)
    window = models.BooleanField(default=False)
    varnish = models.BooleanField(default=False)
    oil = models.BooleanField(default=False)
    total_price = models.FloatField(null=True)

    def __str__(self):
        return self.car.car_model
