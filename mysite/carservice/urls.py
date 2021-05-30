from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import order_delete, order_edit, employee_edit, employee_delete, address_edit, address_delete, archive_edit, \
    archive_delete, client_edit, client_delete, repairment_edit, repairment_delete

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
    path('info/', views.NewAddressView.as_view(), name='new_address'),
    path('info2/', views.NewClientView.as_view(), name='new_client'),
    path('rental_base_info/', views.RentalBaseInfoView.as_view(), name='rental_base_info'),
    path('addcar/', views.NewCarView.as_view(), name='new_car'),
    path('addrentalbaseaddress/', views.NewRentalBaseAddressView.as_view(), name='new_rental_base_address'),
    path('addrentalbase/', views.NewRentalBaseView.as_view(), name='new_rental_base'),
    path('addemployeeaddress/', views.NewEmployeeAddressView.as_view(), name='new_employee_address'),
    path('addemployee/', views.NewEmployeeView.as_view(), name='new_employee'),
    path('repair/', views.RepairView.as_view(), name='new_repair'),
    path('car/<int:pk>/', views.CarDetailsView.as_view(), name='car_details'),
    path('neworder/<int:car_pk>/', views.NewOrderView.as_view(), name='new_order'),
    path('rateorder/', views.RateOrderView.as_view(), name='rate_order'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('orders/order_edit/<int:id>', order_edit),
    path('orders/order_delete/<int:id>', order_delete),
    path('employees/', views.EmployeesView.as_view(), name='employees'),
    path('employees/employee_edit/<int:id>', employee_edit),
    path('employees/employee_delete/<int:id>', employee_delete),
    path('addresses/', views.AddressesView.as_view(), name='addresses'),
    path('addresses/address_edit/<int:id>', address_edit),
    path('addresses/address_delete/<int:id>', address_delete),
    path('archives/', views.ArchivesView.as_view(), name='archives'),
    path('archives/archive_edit/<int:id>', archive_edit),
    path('archives/archive_delete/<int:id>', archive_delete),
    path('clients/', views.ClientsView.as_view(), name='clients'),
    path('clients/client_edit/<int:id>', client_edit),
    path('clients/client_delete/<int:id>', client_delete),
    path('repairments/', views.RepairmentsView.as_view(), name='repairments'),
    path('repairments/repairment_edit/<int:id>', repairment_edit),
    path('repairments/repairment_delete/<int:id>', repairment_delete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)