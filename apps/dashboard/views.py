from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from django.urls import reverse_lazy
from apps.dashboard.forms import ProductModelForm,MakeRequestOrderForm
from django.contrib.auth.models import User
from apps.users.models import Profile
from apps.dashboard.models import ProductModel,OrderModel



@login_required(login_url='login_user')
def index(request):
    # index.html includes customers.html, let's add a way for displaying oders 
    my_orders=OrderModel.objects.all()
    products=ProductModel.objects.all()


    dictionary={
        'my_orders':my_orders,
        'products':products,
    }

    return render(request, 'dashboard/index.html', dictionary)

def make_request(request,id):
    my_orders=OrderModel.objects.all().filter(client_name=id)
    if request.method=="POST":
        request_form=MakeRequestOrderForm(request.POST)
        if request_form.is_valid():
            # The logic is to assign the order to a client who made it.
            # if commit =False, it means we haven't yet received the form
            instance=request_form.save(commit=False)
            instance.client_name=request.user # logged in user is making a request
            instance.save()

            return redirect('index_home')
        
    else:
        request_form=MakeRequestOrderForm()

    dictionary={
        'my_orders':my_orders,
        'request_form':request_form,
    }
    return render(request, 'dashboard/makeRequest.html',dictionary)

    


@login_required(login_url='login_user')
def staffs(request):
    members=User.objects.all()
    members_all=members.count()
    dictionary={
        'members':members,
        'members_all':members_all,
    }
    return render(request, 'dashboard/staffs.html', dictionary)


class Details_of_Staff(LoginRequiredMixin,DetailView):
    model=User
    template_name='dashboard/staff_details.html'


# or use function based views
""" @login_required
def staff_detail(request,pk):
    staff=User.objects.all().get(id=pk)
    context={
        'staff':staff
    }
    return render(request,'dashboard/staff_details.html',context) """

@login_required(login_url='login_user')
def products(request):
    items=ProductModel.objects.all()
    all_products=items.count()

    if request.method=='POST':
        product_form=ProductModelForm(request.POST)
        if product_form.is_valid():
            product_form.save()

            # let's add logic for flash messages
            product_name=product_form.cleaned_data.get('product_name')
            messages.success(request,f'{product_name} Successfully added')

            return redirect('products')


    else:
        product_form=ProductModelForm()

    dictionary={
        'items':items,
        'product_form':product_form,
        'all_products':all_products,
    }
    return render(request, 'dashboard/products.html',dictionary)

# using class based views to edit

class Edit_Product(LoginRequiredMixin,UpdateView):
    model=ProductModel
    fields=['product_name','category','qty']
    template_name='dashboard/edit_product.html'
    success_url=reverse_lazy('products')

# using class based views to Delete the products
# you can even use function based views def delete_product

""" @login_required
def delete_product(request,pk):
    item=ProductModel.objects.all().get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('products')
    return render(request, 'dashboard/delete_product.html') """



class Delete_Product(LoginRequiredMixin,DeleteView):
    model=ProductModel
    template_name='dashboard/delete_product.html'
    success_url=reverse_lazy('products')


# You can add new product by Class based View

""" class Add_New_Product(LoginRequiredMixin,CreateView):
    model=ProductModel
    fields='__all__'
    template_name='dashboard/add_products.html'
    success_url=reverse_lazy('products') """



@login_required(login_url='login_user')
def orders(request):
    all_orders=OrderModel.objects.all().order_by('time_of_order')
    orders_count=all_orders.count()
    dictionary={
        'all_orders':all_orders,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/orders.html',dictionary)


