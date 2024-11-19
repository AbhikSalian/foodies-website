from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Foodiee
from .models import FoodImages, Wishlist, Cart, FoodReview, CartItem
from django.contrib import messages
from .forms import UploadForms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


# def Home(request):
#     return HttpResponse("Welcome to Django Home page")
# Create your views here.


# instead of sending response like this lets render our html page
# Foodiee = [{"name":"Food1","Desc":"Ready to eat food."},{"name":"Food2","Desc":"Ready to eat food2."},{"name":"Food3","Desc":"Ready to eat food3."}]
@login_required(login_url="/Login")
def Home(request):
    Foodiees = FoodImages.objects.all()  # to display all the data in db
    context = {"Foodiees": Foodiees}
    return render(request, "Home.html", {"Foodiees": Foodiees, "context": context})


def About(request):
    return render(request, "About.html")


@login_required(login_url="/Login")
def Uploads(request):
    if request.method == "POST":
        form = UploadForms(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UploadForms()
        images = FoodImages.objects.all()

    return render(request, "Uploads.html", {"form": form, "images": images})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        #  print("Is form valid",form)
        if form.is_valid():
            # username #password
            user_name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Login")
    else:
        form = UserCreationForm()
        return render(request, "SignUp.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")


from django.shortcuts import get_object_or_404


@login_required(login_url="/Login")
def product_view(request, id):
    product = get_object_or_404(FoodImages, id=id)
    review_obj = FoodReview.objects.filter(product=product)

    return render(
        request, "Product.html", {"product": product, "review_obj": review_obj}
    )


@login_required(login_url="/Login")
def wish_list(request, id):
    product = FoodImages.objects.get(id=id)
    obj1, created = Wishlist.objects.get_or_create(user=request.user)
    obj1.product.add(product)
    obj1.save()
    return redirect("home")


@login_required(login_url="/Login")
def cart_list(request, id):
    print(id)

    # Check if the user has a cart or not
    user_cart, created = Cart.objects.get_or_create(user=request.user)

    # Fetch the product with the given ID
    product = get_object_or_404(FoodImages, id=id)

    # Create or get the CartItem for the cart and product
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

    # If the item was found and the cart item already exists, we could just update the count
    if not created:
        cart_item.cart_count += 1  # Increase count if the item is already in the cart
        cart_item.save()

    return redirect("home")


# Show list of cart items
@login_required(login_url="/Login")
def show_cartList(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, "CartList.html", {"user_products": cart_items})


@login_required(login_url="/Login")
def show_wishList(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)

    # Collect all products from all wishlists
    products_with_wishlist = []
    for wishlist in wishlists:
        # add each product along with wishlist ID
        for product in wishlist.product.all():
            products_with_wishlist.append(
                {"product": product, "wishlist_id": wishlist.id}  # includes wishlist id
            )
    return render(request, "WishList.html", {"view_products": products_with_wishlist})


from django.shortcuts import get_object_or_404, redirect
from .models import Wishlist  # Import the Wishlist model


@login_required(login_url="/Login")
def remove_wish(request, id):
    if request.user.is_authenticated:
        # Get the specific wishlist item for the logged-in user by 'id'
        wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)

        # Delete the specific wishlist item
        wishlist_item.delete()

        # Redirect to the homepage (or another page as needed)
        return redirect("home")
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect("login")


from django.http import JsonResponse


@login_required(login_url="/Login")
def show_api(request):
    start_text = request.GET.get("parameter1")
    FoodName = FoodImages.objects.filter(name__startswith=start_text).values_list()
    if FoodName:
        message = {"FoodName": FoodName[0], "name": "Hey this is my data"}
    else:
        message = {"name": "data not found"}
    return JsonResponse(message)


