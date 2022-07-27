from django.urls import path
from productapp import views


urlpatterns = [
    path("sign-up/",views.UserCreationView.as_view(),name="sign-up"),
    path("login",views.UserLoginView,name="login"),
    path("products/",views.ProductView,name="products")

]