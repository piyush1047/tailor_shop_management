# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib import messages
from authentication.models import CustomUser
from customers.models import Customer
from orderapp.models import Order
from expensesapp.models import expense
from revenueapp.models import revenuedetails
from django.utils import timezone
from import_export import resources
from django.contrib import messages


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new user
        user = CustomUser.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        messages.info(request, "Account created successfully!")
        return redirect('/login/')
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')  # Redirect to the index page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'index.html')


from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('/index/')  # Redirect to the login page after logout


def homepage(request):
    orderdata_count=Order.objects.all().count()
    customerdata_count=Customer.objects.all().count()
    expensedata_count=expense.objects.all().count()
    revenue_count=revenuedetails.objects.all().count()
    today = timezone.now().date()
    todayorders=Order.objects.filter(deliver_date=today)
    todayorderscount=Order.objects.filter(deliver_date=today).count()
    return render(request,'dashboard.html',{'orderdata_count':orderdata_count,'customerdata_count':customerdata_count, 'expensedata_count':expensedata_count, 'revenue_count':revenue_count, 'todayorders':todayorders,'todayorderscount':todayorderscount } )


# customer page 
class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


def export(request):
    resource = CustomerResource()
    dataset = resource.export()

    file_format = request.GET.get('format', 'xlsx')

    if file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_customers.csv"'
    elif file_format == 'json':
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="exported_customers.json"'
    else:  # Default to Excel
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="exported_customers.xlsx"'

    return response


def customerfn(request):
    customerdata=Customer.objects.all()
    return render(request,'customer.html',{'customerdata':customerdata})

def addcustomerfn(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_contact = request.POST.get('customer_contact')
        customer_address = request.POST.get('customer_address')
        cs = Customer(
            customer_name=customer_name,
            customer_contact=customer_contact,
            customer_address=customer_address,
        )
        cs.save()
        messages.success(request,'Added successfully')

        return redirect('customer')
    return render(request,'add_customer.html')

def deletecustomer(request,id):
    cs=Customer.objects.get(id=id)
    cs.delete()
    return redirect('/customer')

def Editcustomer(request):
    cs=Customer.objects.all()
    context={
        'cs':cs
    }
    return redirect(request,"customer.html",context)

def Updatecustomer(request,id):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_contact = request.POST.get('customer_contact')
        customer_address = request.POST.get('customer_address')
        cs = Customer(
            id=id,
            customer_name=customer_name,
            customer_contact=customer_contact,
            customer_address=customer_address,
        )
        cs.save()
        messages.success(request,'Update Successfully')
        
        return redirect('/customer')
    return render(request,'customer.html')
# end customer page


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order


def export_order(request):
    resource = OrderResource()
    dataset = resource.export()

    file_format = request.GET.get('format', 'xlsx')

    if file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_orders.csv"'
    elif file_format == 'json':
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="exported_orders.json"'
    else:  # Default to Excel
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="exported_orders.xlsx"'

    return response


# order page start
def orderfn(request):
    customerbt=Customer.objects.all()
    orderdata=Order.objects.all()


    return render(request,'orders.html',{'orderdata':orderdata,'customerbt':customerbt,})

def add_order(request):
    orderdata=Order.objects.all()
    customerbt=Customer.objects.all()
    if request.method == 'POST':
        order_name = request.POST.get('order_name')
        customer = request.POST.get('customer')
        description=request.POST.get('description')
        order_date=request.POST.get('order_date')
        deliver_date=request.POST.get('deliver_date')
        priority=request.POST.get('priority')
        Total_payment = float(request.POST.get('Total_payment', 0))  # Convert to float
        Advance_Payment = float(request.POST.get('Advance_Payment', 0))  # Convert to float
        due_payment=Total_payment-Advance_Payment
        quantity=request.POST.get('quantity')
        product_img=request.FILES.get('product_img')
        garment_type=request.POST.get('garment_type')

        # Create an order instance
        order = Order(
            order_name=order_name,
            customer=Customer.objects.get(customer_name=customer),
            description=description,
            order_date=order_date,
            deliver_date=deliver_date,
            priority=priority,
            Total_payment=Total_payment,
            Advance_Payment=Advance_Payment,
            due_payment=due_payment,
            quantity=quantity,
            product_img=product_img,
            garment_type=garment_type
        )
        
        # Set measurements based on garment type
        if  garment_type == 'Topwear':
            order.neck_size = request.POST.get('neck_size')
            order.chest_size = request.POST.get('chest_size')
            order.sleeve_length = request.POST.get('sleeve_length')
            order.shirt_length  = request.POST.get('shirt_length')
            order.stomach = request.POST.get('stomach')
            order.heap = request.POST.get('heap')
            order.shoulder = request.POST.get('shoulder')
            order.remark_shirt = request.POST.get('remark_shirt')

        elif garment_type == 'Bottomwear':
            order.waist_size = request.POST.get('waist_size')
            order.length_size = request.POST.get('length_size')
            order.pant_heap  = request.POST.get('pant_heap')
            order.mohri = request.POST.get('mohri')
            order.thai = request.POST.get('thai')
            order.Knee_Size = request.POST.get('Knee_Size')
            order.langot = request.POST.get('langot')
            order.pindli = request.POST.get('pindli')
            order.remark = request.POST.get('remark')


        elif garment_type == 'Top-Bottom':
            order.waist_size = request.POST.get('waist_size')
            order.length_size = request.POST.get('length_size')
            order.pant_heap  = request.POST.get('pant_heap')
            order.mohri = request.POST.get('mohri')
            order.thai = request.POST.get('thai')
            order.Knee_Size = request.POST.get('Knee_Size')
            order.langot = request.POST.get('langot')
            order.pindli = request.POST.get('pindli')
            order.remark = request.POST.get('remark')
            order.neck_size = request.POST.get('neck_size')
            order.chest_size = request.POST.get('chest_size')
            order.sleeve_length = request.POST.get('sleeve_length')
            order.shirt_length  = request.POST.get('shirt_length')
            order.stomach = request.POST.get('stomach')
            order.heap = request.POST.get('heap')
            order.heap_loosing=request.POST.get('heap_loosing')
            order.shoulder = request.POST.get('shoulder')
            order.remark = request.POST.get('remark')

        order.save()
        messages.success(request,'Added successfully')
        return redirect('/orders') 
    return render(request, 'add_order.html',{'customerbt':customerbt,'orderdata':orderdata})



def ordersdelete(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('/orders')

def Editorder(request):
    order=Order.objects.all()
    context={
        'order':order
    }
    return redirect(request,"orders.html",context)

def Updateorder(request,id):
    if request.method == 'POST':
        order_name = request.POST.get('order_name')
        customer = request.POST.get('customer')
        description=request.POST.get('description')
        order_date=request.POST.get('order_date')
        deliver_date=request.POST.get('deliver_date')
        priority=request.POST.get('priority')
        Total_payment=request.POST.get('Total_payment')
        Advance_Payment=request.POST.get('Advance_Payment')
        due_payment=request.POST.get('due_payment')
        quantity=request.POST.get('quantity')
        product_img=request.FILES.get('product_img')
        garment_type=request.POST.get('garment_type')

        # Create an order instance
        order = Order(
            id=id,
            order_name=order_name,
            customer=Customer.objects.get(customer_name=customer),
            description=description,
            order_date=order_date,
            deliver_date=deliver_date,
            priority=priority,
            Total_payment=Total_payment,
            Advance_Payment=Advance_Payment,
            due_payment=due_payment,
            quantity=quantity,
            product_img=product_img,
            garment_type=garment_type
          )
        
        # Set measurements based on garment type
        if  garment_type == 'Topwear':
            order.neck_size = request.POST.get('neck_size')
            order.chest_size = request.POST.get('chest_size')
            order.sleeve_length = request.POST.get('sleeve_length')
            order.shirt_length  = request.POST.get('shirt_length')
            order.stomach = request.POST.get('stomach')
            order.heap = request.POST.get('heap')
            order.shoulder = request.POST.get('shoulder')
            order.remark_shirt = request.POST.get('remark_shirt')

        elif garment_type == 'Bottomwear':
            order.waist_size = request.POST.get('waist_size')
            order.length_size = request.POST.get('length_size')
            order.pant_heap  = request.POST.get('pant_heap')
            order.mohri = request.POST.get('mohri')
            order.thai = request.POST.get('thai')
            order.Knee_Size = request.POST.get('Knee_Size')
            order.langot = request.POST.get('langot')
            order.pindli = request.POST.get('pindli')
            order.remark = request.POST.get('remark')


        elif garment_type == 'Top-Bottom':
            order.waist_size = request.POST.get('waist_size')
            order.length_size = request.POST.get('length_size')
            order.pant_heap  = request.POST.get('pant_heap')
            order.mohri = request.POST.get('mohri')
            order.thai = request.POST.get('thai')
            order.Knee_Size = request.POST.get('Knee_Size')
            order.langot = request.POST.get('langot')
            order.pindli = request.POST.get('pindli')
            order.remark = request.POST.get('remark')
            order.neck_size = request.POST.get('neck_size')
            order.chest_size = request.POST.get('chest_size')
            order.sleeve_length = request.POST.get('sleeve_length')
            order.shirt_length  = request.POST.get('shirt_length')
            order.stomach = request.POST.get('stomach')
            order.heap = request.POST.get('heap')
            order.heap_loosing=request.POST.get('heap_loosing')
            order.shoulder = request.POST.get('shoulder')
            order.remark = request.POST.get('remark')

        order.save()
        messages.success(request,'Update Successfully')
        return redirect('/orders') 
    return render(request, 'orders.html')

    
 
# end order page

# expenses

class ExpenseResource(resources.ModelResource):
    class Meta:
        model = expense


def export_expense(request):
    resource = ExpenseResource()
    dataset = resource.export()

    file_format = request.GET.get('format', 'xlsx')

    if file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_expense.csv"'
    elif file_format == 'json':
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="exported_expense.json"'
    else:  # Default to Excel
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="exported_expense.xlsx"'

    return response

def expensesfn(request):
    expensedata=expense.objects.all()
    return render(request,'expenses.html', {'expensedata':expensedata})

def addexpensesfn(request):
    if request.method == 'POST':
        expense_date = request.POST.get('expense_date')
        expense_category = request.POST.get('expense_category')
        expense_amount = request.POST.get('expense_amount')
        description = request.POST.get('description')
        exp = expense(
            expense_date=expense_date,
            expense_category=expense_category,
            expense_amount=expense_amount,
            description=description
        )
        exp.save()
        messages.success(request,'Added successfully')
        return redirect('/expenses')
    return render(request,'expenses.html')

def deleteepensesfn(request,id):
    exp=expense.objects.get(id=id)
    exp.delete()
    return redirect('/expenses')
# end expenses

# revenue 
class RevenueResource(resources.ModelResource):
    class Meta:
        model = revenuedetails


def export_revenue(request):
    resource = RevenueResource()
    dataset = resource.export()

    file_format = request.GET.get('format', 'xlsx')

    if file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_revenue.csv"'
    elif file_format == 'json':
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="exported_revenue.json"'
    else:  # Default to Excel
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="exported_revenue.xlsx"'

    return response

def revenuefn(request):
    revenue=revenuedetails.objects.all()
    data={
        'revenue':revenue
    }
    return render(request,'revenue.html', data)

def addrevenuefn(request):
    if request.method == 'POST':
        income_date = request.POST.get('income_date')
        revenue_category = request.POST.get('income-category')
        revenue_amount = request.POST.get('income-amount')
        description = request.POST.get('description')
        rev = revenuedetails(
            income_date=income_date,
            income_category=revenue_category,
            income_amount=revenue_amount,
            description=description
        )
        rev.save()
        messages.success(request,'Added successfully')
        return redirect('/revenue')
    return render(request,'revenue.html')

def deleterevenuefn(request,id):
    rev=revenuedetails.objects.get(id=id)
    rev.delete()
    return redirect('/revenue')
# end revenue
