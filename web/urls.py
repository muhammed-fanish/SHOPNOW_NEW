from django.urls import path
from web.views import *
app_name = "web"
urlpatterns = [

	path('', myHome.as_view(), name="home"),
	path('myShop', myShop.as_view(), name="myShop"),
	path('productDetails/<int:pk>/', productDetails.as_view(), name="productDetails"),
	path('shopCart', shopCart.as_view(), name="shopCart"),
	path('contact', contact.as_view(), name="contact"),
	path('checkOut', checkOut.as_view(), name="checkOut"),
	path('refundPolicy', refundPolicy.as_view(), name="refundPolicy"),
	path('shippingPolicy', shippingPolicy.as_view(), name="shippingPolicy"),
	path('privacyPolicy', privacyPolicy.as_view(), name="privacyPolicy"),
	path('aboutUs', aboutUs.as_view(), name="aboutUs"),
	path('newsLetter', newsLetter.as_view(), name="newsLetter")

]
