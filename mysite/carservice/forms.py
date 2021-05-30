from django.forms import ModelForm

from carservice.models import Order, Seller, Address, OrdersArchive, Client, Repairments


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ArchivesForm(ModelForm):
    class Meta:
        model = OrdersArchive
        fields = '__all__'


class ClientsForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class RepairmentsForm(ModelForm):
    class Meta:
        model = Repairments
        fields = '__all__'
