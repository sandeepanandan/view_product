from django.urls import path
from productapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.UserCreationView.as_view(),name="sign-up"),
    path("login",views.userloginview,name="login"),
    path("products/",views.productview,name="products"),
    path("logout/",views.logoutview,name="logout")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)