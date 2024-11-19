from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home,name="home"),
    path('About',views.About,name="about"),
    path('Upload',views.Uploads,name="upload_images"),
    path('Login',views.login_page,name="Login"),
    path('Logout',views.logout_user,name="Logout"),
    path('SignUp',views.SignUp,name="SignUp"),
    path('Product/<int:id>',views.product_view,name="Product"),
    path('addWish/<int:id>',views.wish_list,name="addWish"),
    path('addCart/<int:id>',views.cart_list,name="addCart"),
    path('show_wishlist',views.show_wishList,name="show_wishlist"),
    path('show_cartList',views.show_cartList,name="show_cartList"),
    path('show_wishlist/removewish/<int:id>/', views.remove_wish, name='removewish'),
    path('dummy',views.show_api,name="dummy"),


    
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

