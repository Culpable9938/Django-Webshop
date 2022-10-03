from django.contrib import admin

# Register your models here.
from .models import Jewelry, Comment, Topic, User, CartItem, Order, Color, Tag, Order

admin.site.register(Tag),
admin.site.register(Color),
admin.site.register(Order),
admin.site.register(CartItem),
admin.site.register(User),
admin.site.register(Jewelry),
admin.site.register(Comment),
admin.site.register(Topic)