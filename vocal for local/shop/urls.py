from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("sellerhome/", views.sellerhome, name="sellerhome"),
    path("sellerhome/sellershop/<int:shopid>", views.sellershop, name="sellershop"),
    path("index/<int:shopid>", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("searchbypincode/", views.searchbypincode, name="searchbypincode"),
    path("search/", views.search, name="search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("paymentdone/", views.paymentdone, name="paymentdone"),

    #path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
