from django.contrib import admin
from .models import Foodiee
from .models import FoodImages
from .models import Wishlist
from .models import Cart
from .models import FoodReview
from .models import CartItem

# Register your models here.

admin.site.register(Foodiee)


class FoodUploadAdmin(admin.ModelAdmin):
    list_display = ('name','category','cost','images')
    list_filter = ('name','cost')
    search_fields =('category','cost')
    fields = ['name','category','cost','images']
admin.site.register(FoodImages,FoodUploadAdmin)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(FoodReview)
admin.site.register(CartItem)





