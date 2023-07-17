from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
import datetime
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def send_daily_report(request):
    # Query sales data for the day
    sales_list = Sale.objects.filter(timestamp__date=datetime.date.today())


    # Render the email template
    email_template = 'daily_sales_report.html'
    email_context = {'sales_list': sales_list}
    email_html = render_to_string(email_template, email_context)
    email_text = strip_tags(email_html)

    # Generate the email content
    subject = 'Daily Sales Report'
    message = email_text

    # Send the email
    recipient_email = 'recipientemai;@gmail.com' #Add recipient email here.
    send_mail(subject, message, from_email='ekocash@gmail.com', recipient_list=[recipient_email], html_message=email_html)

    # Render a response
    return render(request, 'report_sent.html')




def record_sale(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])

        product = Product.objects.get(pk=product_id)

        if product.quantity >= quantity:
            sale = Sale(product=product, quantity=quantity, payment_method=request.POST['payment_method'], sold_price=request.POST['sold_price'])
            sale.save()

            product.quantity -= quantity
            product.save()

            return redirect('product_list')
        else:
            error_message = "Insufficient quantity available."
            products = Product.objects.all()
            return render(request, 'product_list.html', {'products': products, 'error_message': error_message})

    else:
        products = Product.objects.all()
        return render(request, 'sale_form.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def index(request):
    products = Product.objects.all()
    total_items = Product.objects.count()
    user_count = User.objects.count()
    total_min_price = Product.objects.aggregate(total_min_price=Sum('min_price'))['total_min_price']
    return render(request, 'admin/index.html', {'products': products, 'total_min_price': total_min_price, 'total_items':total_items, 'user_count':user_count})

def inventory(request):
    products = Product.objects.all()
    total_items = Product.objects.count()
    user_count = User.objects.count()
    total_min_price = Product.objects.aggregate(total_min_price=Sum('min_price'))['total_min_price']
    return render(request, 'admin/inventory.html', {'products': products, 'total_min_price': total_min_price, 'total_items':total_items, 'user_count':user_count})

def Reports(request):
    return render(request, 'admin/Reports.html')

def Total_Sales(request):
    sales = Sale.objects.order_by('timestamp')
    return render(request, 'admin/Total_Sales.html',{'sales': sales})

def User_Accounts(request):
        # Retrieve the user information from the User model
    user_info = User.objects.values('username', 'is_staff', 'date_joined', 'last_login').first()

    # Pass the user information to the template context
    context = {
        'account_name': user_info['username'],
        'user_type': 'Staff' if user_info['is_staff'] else 'Regular',
        'creation_date': user_info['date_joined'],
        'last_login': user_info['last_login'],
    }

    return render(request, 'admin/User_Accounts.html', context)

def add_product(request):
    if request.method == 'POST':
        sku = request.POST['sku']
        name = request.POST['name']
        quantity = request.POST['quantity']
        buy_price = request.POST['buy_price']
        min_price = request.POST['min_price']


        product = Product(sku=sku, name=name, quantity=quantity, buy_price= buy_price, min_price=min_price)
        product.save()

        return redirect('inventory')  # Redirect to a view that displays the list of products

    return render(request, 'admin/add_product.html')

def base(request):
    return render(request, 'admin/base.html')


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'admin/delete_product.html', {'product': product})


def search_sugestions(request):
    query = request.GET.get('term', '')
    products = Product.objects.filter(name__icontains=query).values_list('name', flat=True)
    suggestions = list(products)
    return JsonResponse(suggestions, safe=False)


