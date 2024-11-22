"""
URL configuration for tailor_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('', views.login_page, name='index'),
    path('dashboard/', views.homepage, name='dashboard'),  # Add this line
    path('logout/', views.logout_user, name='logout'),  # Add this line
    # customer page crud operation
    path('addcustomerfn/' , views.addcustomerfn, name='addcustomerfn'),
    path('customer/' , views.customerfn, name='customer'),
    path('export/', views.export, name='export'),
    path('deletecustomer/<int:id>', views.deletecustomer, name='deletecustomer'),
    path('editcustomer/',views.Editcustomer,name='editcustomer'),
    path('Updatecustomer/<str:id>',views.Updatecustomer,name='Updatecustomer'),
    # end customer page 

    # order pagecrud operation
    path('orders/' , views.orderfn, name='orders'),
    path('add_order/' , views.add_order, name='add_order'),
    path('export_order/', views.export_order, name='export_order'),
    path('ordersdelete/<int:id>' , views.ordersdelete , name='ordersdelete'),
    path('editorder/',views.Editorder,name='editorder'),
    path('Updateorder/<str:id>',views.Updateorder,name='Updateorder'),

    # add expenses
    path('expenses/' , views.expensesfn, name='expenses'),
    path('addexpensesfn/' , views.addexpensesfn, name='addexpensesfn'),
    path('deleteepensesfn/<int:id>' , views.deleteepensesfn , name='deleteepensesfn'),
    path('export_expense/', views.export_expense, name='export_expense'),

    # end expenses
    # revenue page crud operation
    path('revenue/' , views.revenuefn, name='revenue'),
    path('addrevenuefn/' , views.addrevenuefn, name='addrevenuefn'),
    path('deleterevenuefn/<int:id>' , views.deleterevenuefn , name='deleterevenuefn'),
    path('export_revenue/', views.export_revenue, name='export_revenue'),

    # end revenue page
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
