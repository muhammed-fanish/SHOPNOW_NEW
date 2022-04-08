from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(OrderItem)
admin.site.register(Message)
