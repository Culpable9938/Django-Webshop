from django.contrib import admin
from .models import Rig, RigImage, Font, Bead, Message, Decor
# Register your models here.
admin.site.register(Font),
admin.site.register(Decor),
admin.site.register(Message),
admin.site.register(Bead),
admin.site.register(Rig),
admin.site.register(RigImage),