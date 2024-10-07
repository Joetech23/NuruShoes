from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
admin.site.site_header = "Karma Admin"
admin.site.site_title = "Karma Admin"
admin.site.index_title = "Welcome to Your Karma Admin"

# from django.contrib.auth.models import User
# user = User.objects.create_superuser(
#     username='josh',
#     email='your_email@example.com',
#     password='josh234'
# )
# print('Superuser created successfully!')
# admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)