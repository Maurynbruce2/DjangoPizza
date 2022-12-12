from django.contrib import admin
from .models import Pizza
from .models import Topping
from .models import Comment
from .models import Image

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
admin.site.register(Image)