from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

from .forms import OrderForm, EmployeeForm, AddressForm, ArchivesForm, ClientsForm, RepairmentsForm
from .models import Order, Car, Client, Address, Repairments, RentalBase, Seller, OrdersArchive


class StartView(TemplateView):
    template_name = 'start.html'

    def get_context_data(self, **kwargs):
        ctx = super(StartView, self).get_context_data(**kwargs)

        cars = Car.objects.filter(is_available=True)
        ctx['cars'] = cars

        return ctx


class NewOrderView(CreateView):
    model = Order
    fields = [
        'seller', 'days'
    ]

    template_name = 'new_order.html'

    def get_car(self):
        car_pk = self.kwargs['car_pk']
        car = Car.objects.get(pk=car_pk)

        return car

    def get_client(self):
        client = Client.objects.last()
        return client

    def get_context_data(self, **kwargs):
        ctx = super(NewOrderView, self).get_context_data(**kwargs)
        ctx['car'] = self.get_car()

        return ctx

    def form_valid(self, form):
        new_order = form.save(commit=False)
        new_order.car = self.get_car()
        new_order.client = self.get_client()
        new_order.save()

        return super(NewOrderView, self).form_valid(form)

    def get_success_url(self):
        car = self.get_car()
        car_details_page_url = car.get_absolute_url()
        car.is_available = False
        car.save()

        return '{}?booking-success=1'.format(car_details_page_url)


class CarDetailsView(DetailView):
    template_name = 'car_details.html'
    model = Car

    def get_context_data(self, **kwargs):
        ctx = super(CarDetailsView, self).get_context_data(**kwargs)
        ctx['booking_success'] = 'booking-success' in self.request.GET

        return ctx


class NewAddressView(CreateView):
    model = Address
    fields = [
        'country', 'city', 'street', 'postal_code'
    ]
    template_name = 'new_address.html'

    def form_valid(self, form):
        new_address = form.save(commit=False)
        new_address.save()

        return super(NewAddressView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_client')


class NewClientView(CreateView):
    model = Client
    fields = [
        'name', 'surname', 'phone'
    ]
    template_name = 'new_client.html'

    def get_address(self):
        address = Address.objects.last()
        return address

    def form_valid(self, form):
        new_client = form.save(commit=False)
        new_client.address = self.get_address()
        new_client.save()

        return super(NewClientView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class RepairView(CreateView):
    model = Repairments
    fields = [
        'car', 'engine', 'tire', 'door', 'window', 'varnish', 'oil', 'total_price'
    ]
    template_name = 'repair.html'

    def form_valid(self, form):
        new_repair = form.save(commit=False)
        new_repair.save()

        return super(RepairView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class NewCarView(CreateView):
    model = Car
    fields = [
        'rental_base', 'image', 'car_mark', 'car_model', 'car_color', 'num_of_seats', 'cost_per_day'
    ]
    template_name = 'new_car.html'

    def form_valid(self, form):
        new_car = form.save(commit=False)
        new_car.save()

        return super(NewCarView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class NewRentalBaseAddressView(CreateView):
    model = Address
    fields = [
        'country', 'city', 'street', 'postal_code'
    ]
    template_name = 'new_rental_base_address.html'

    def form_valid(self, form):
        new_address = form.save(commit=False)
        new_address.save()

        return super(NewRentalBaseAddressView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_rental_base')


class NewRentalBaseView(CreateView):
    model = RentalBase
    fields = [
        'name', 'phone', 'number_of_employees', 'logo'
    ]
    template_name = 'new_rental_base.html'

    def get_address(self):
        address = Address.objects.last()
        return address

    def form_valid(self, form):
        new_rental_base = form.save(commit=False)
        new_rental_base.address = self.get_address()

        new_rental_base.save()

        return super(NewRentalBaseView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class NewEmployeeAddressView(CreateView):
    model = Address
    fields = [
        'country', 'city', 'street', 'postal_code'
    ]
    template_name = 'new_employee_address.html'

    def form_valid(self, form):
        new_address = form.save(commit=False)
        new_address.save()

        return super(NewEmployeeAddressView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_employee')


class NewEmployeeView(CreateView):
    model = Seller
    fields = [
        'name', 'surname', 'phone', 'salary'
    ]
    template_name = 'new_employee.html'

    def get_address(self):
        address = Address.objects.last()
        return address

    def form_valid(self, form):
        new_employee = form.save(commit=False)
        new_employee.address = self.get_address()
        new_employee.save()

        return super(NewEmployeeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class RateOrderView(CreateView):
    model = OrdersArchive
    fields = [
        'car_score', 'order_score'
    ]
    template_name = 'rate_order.html'

    def get_order(self):
        order = Order.objects.last()
        return order

    def form_valid(self, form):
        new_ordersarchive = form.save(commit=False)
        new_ordersarchive.order = self.get_order()
        new_ordersarchive.save()

        return super(RateOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class OrdersView(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        ctx = super(OrdersView, self).get_context_data(**kwargs)

        orders = Order.objects.all()
        ctx['orders'] = orders

        return ctx


def order_edit(request, id):
    instance = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/orders')
    return render(request, 'edit_form.html', {'form': form})


def order_delete(request, id):
    try:
        order_select = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return redirect('/carservice/orders')
    order_select.car.is_available = True
    order_select.car.save()
    order_select.delete()
    return redirect('/carservice/orders')


class EmployeesView(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        ctx = super(EmployeesView, self).get_context_data(**kwargs)

        employees = Seller.objects.all()
        ctx['employees'] = employees

        return ctx


def employee_edit(request, id):
    instance = get_object_or_404(Seller, id=id)
    form = EmployeeForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/employees')
    return render(request, 'edit_form.html', {'form': form})


def employee_delete(request, id):
    try:
        employee_select = Seller.objects.get(id=id)
    except Seller.DoesNotExist:
        return redirect('/carservice/employees')
    employee_select.delete()
    return redirect('/carservice/employees')


class AddressesView(TemplateView):
    template_name = 'addresses.html'

    def get_context_data(self, **kwargs):
        ctx = super(AddressesView, self).get_context_data(**kwargs)

        addresses = Address.objects.all()
        ctx['addresses'] = addresses

        return ctx


def address_edit(request, id):
    instance = get_object_or_404(Address, id=id)
    form = AddressForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/addresses')
    return render(request, 'edit_form.html', {'form': form})


def address_delete(request, id):
    try:
        address_select = Address.objects.get(id=id)
    except Address.DoesNotExist:
        return redirect('/carservice/addresses')
    address_select.delete()
    return redirect('/carservice/addresses')


class ArchivesView(TemplateView):
    template_name = 'archives.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArchivesView, self).get_context_data(**kwargs)
        archives = OrdersArchive.objects.all()
        ctx['archives'] = archives

        return ctx


def archive_edit(request, id):
    instance = get_object_or_404(OrdersArchive, id=id)
    form = ArchivesForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/archives')
    return render(request, 'edit_form.html', {'form': form})


def archive_delete(request, id):
    try:
        archive_select = OrdersArchive.objects.get(id=id)
    except OrdersArchive.DoesNotExist:
        return redirect('/carservice/archives')
    archive_select.delete()
    return redirect('/carservice/archives')


class ClientsView(TemplateView):
    template_name = 'clients.html'

    def get_context_data(self, **kwargs):
        ctx = super(ClientsView, self).get_context_data(**kwargs)
        clients = Client.objects.all()
        ctx['clients'] = clients

        return ctx


def client_edit(request, id):
    instance = get_object_or_404(Client, id=id)
    form = ClientsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/clients')
    return render(request, 'edit_form.html', {'form': form})


def client_delete(request, id):
    try:
        client_select = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return redirect('/carservice/clients')
    client_select.delete()
    return redirect('/carservice/clients')


class RentalBaseInfoView(TemplateView):
    template_name = 'rental_base_info.html'

    def get_context_data(self, **kwargs):
        ctx = super(RentalBaseInfoView, self).get_context_data(**kwargs)
        rentalbases = RentalBase.objects.all()
        ctx['rentalbases'] = rentalbases

        return ctx


class RepairmentsView(TemplateView):
    template_name = 'repairments.html'

    def get_context_data(self, **kwargs):
        ctx = super(RepairmentsView, self).get_context_data(**kwargs)
        repairments = Repairments.objects.all()
        ctx['repairments'] = repairments

        return ctx


def repairment_edit(request, id):
    instance = get_object_or_404(Repairments, id=id)
    form = RepairmentsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/carservice/repairments')
    return render(request, 'edit_form.html', {'form': form})


def repairment_delete(request, id):
    try:
        repairment_select = Repairments.objects.get(id=id)
    except Repairments.DoesNotExist:
        return redirect('/carservice/repairments')
    repairment_select.delete()
    return redirect('/carservice/repairments')
