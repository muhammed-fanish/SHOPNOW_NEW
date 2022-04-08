import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q 

from web.models import *


class myHome(View):
	def get(self, request):
		most_selled_product_images=None
		search_products = None
		new_products = Product.objects.all().order_by('-id')[:6]
		q = request.GET.get("q")
		if(q != None):
			search_products = Product.objects.filter(
				Q(name__icontains = q) | Q(actual_price__icontains = q) | Q(description__icontains = q)
			)
		most_selled_product = Product.objects.filter(is_best_selling=True).last()
		if ProductImage.objects.filter(product=most_selled_product).exists():
			most_selled_product_images = ProductImage.objects.filter(product=most_selled_product)
		context = {
			'new_products': new_products,
			'most_selled_product': most_selled_product,
			'most_selled_product_images': most_selled_product_images,
			'search_products' : search_products,
			"q" : q
		}
		return render(request, 'index.html', context)
class refundPolicy(View):
	def get(self, request):
		context = {
		}
		return render(request, 'refund_policy.html', context)

class shippingPolicy(View):
	def get(self, request):
		context = {
		}
		return render(request, 'shipping_policy.html', context)
class privacyPolicy(View):
	def get(self, request):
		context = {
		}
		return render(request, 'privacy_policy.html', context)

class aboutUs(View):
	def get(self, request):
		context = {
		}
		return render(request, 'about_us.html', context)

		
	

class myShop(View):
	def get(self, request):
		search_products = None
		all_products = Product.objects.all()
		q = request.GET.get("q")
		if(q != None):
			search_products = Product.objects.filter(
				Q(name__icontains = q) | Q(actual_price__icontains = q) | Q(description__icontains = q)
			)
		p = Paginator(all_products, 2)
		page = request.GET.get('page')
		products = p.get_page(page)
		for prod in products :
			prod.discount_amount = prod.actual_price - prod.offer_price
		context = {
			'products' : products,
			'search_products' : search_products,
			"q" : q
		}
		return render(request, 'shop.html', context)

class productDetails(View):
	def get(self, request, pk):
		pdt = None
		pdt_images = None
		prod_reviews = None
		related_pdts = Product.objects.all()
		if Product.objects.filter(id=pk).exists():
			pdt = Product.objects.filter(id=pk)[0]
		if ProductImage.objects.filter(product=pdt).exists():
			pdt_images = ProductImage.objects.filter(product=pdt)
		if ProductReview.objects.filter(product = pdt).exists():
			prod_reviews = ProductReview.objects.filter(product = pdt)
		context = {
			'pdt': pdt, 
			'pdt_images': pdt_images,
			'related_pdts':related_pdts,
			'prod_reviews' :prod_reviews
		}
		return render(request, 'product-details.html',context)
	
	def post(self, request, *args, **kwargs):
		pdtQty = request.POST.get('proQty')
		pdtId = request.POST.get('pdtId')
		if Product.objects.filter(id=pdtId).exists():
				pdt = Product.objects.filter(id=pdtId)[0]
		product_price = int(pdt.offer_price)
		total_price = product_price*int(pdtQty)
		context = {
			"pdtQty" : pdtQty,
			"pdt" : pdt,
			"total_price" :total_price
		}
		return render(request, 'checkout.html', context)

class checkOut(View):
	def post(self, request, *args, **kwargs):
		pdtQty = request.POST.get('pdtQty')
		pdtId = request.POST.get('pdtId')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		country = request.POST.get('country')
		address = request.POST.get('address')
		city = request.POST.get('town_city')
		state = request.POST.get('state')
		pin_code = request.POST.get('pin_code')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		user = Users.objects.create(
			first_name = first_name,
			last_name = last_name,
			country = country,
			address=address,
			city = city,
			state = state,
			pincode = pin_code,
			phone=phone,
			email = email
		)
		user.save()
		item = Product.objects.get(id = pdtId)
		order = OrderItem.objects.create(
			item = item,
			qty = pdtQty,
			user = user
		)
		order.save()
		response_data = {
				"status" : "true",
				"title" : "You have ordered " +item.name +"with Quantity " + pdtQty,
				"message" :"Thanks for your order",
				"redirect_url":"/",
				"redirect" :"true"
        }
		return HttpResponse(json.dumps(response_data),content_type='application/javascript')


class shopCart(View):
	def get(self, request):
		return render(request, 'shop-cart.html', {'data': 'data'})

class contact(View):

	def post(self, request, *args, **kwargs):
		print("INSIDE PODT............")
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		phone = request.POST.get('phone')
		print(name,email,message,phone)
		msg = Message.objects.create(
			name = name,
			email = email,
			message=message,
			phone = phone
		)
		msg.save()
		response_data = {
				"status" : "true",
				"title" : "You have submitted your message",
				"message" :"Thanks for your Message"
        }

		return HttpResponse(json.dumps(response_data),content_type='application/javascript')


	def get(self, request):
		print("CONTACT GET ---------------")
		return render(request, 'contact.html', {'data': 'data'})


class newsLetter(View):
	def post(self, request, *args, **kwargs):
		print("POST NEWSLETTER -----")
		email = request.POST.get('email')
		print(email,"EMAIL----")
		news_letter = NewsLetter.objects.create(
			email = email
		)
		news_letter.save()
		response_data = {
				"status" : "true",
				"title" : "You have submitted your email",
				"message" :"Thanks for your response"
        }
		return HttpResponse(json.dumps(response_data),content_type='application/javascript')

	def get(self, request):
		q = request.GET.get("q")
		print(q,"SEARCH --")
		

		
		



