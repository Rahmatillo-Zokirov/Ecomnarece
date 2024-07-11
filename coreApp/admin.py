from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from userApp.models import User
from .models import *
from orderApp.models import *
from actionApp.models import *



class CustomUserAdmin(UserAdmin):
    fieldsets = [
        ('Auth',
         {'fields':
              ['username', 'password'],
          },
         ),
        ('Details',
         {'fields': ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'birth_date', 'gender',
                     'address', 'date_joined'],
          },
         )
    ]


admin.site.register(User, CustomUserAdmin)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(Banner)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)





