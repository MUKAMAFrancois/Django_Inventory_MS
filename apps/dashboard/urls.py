
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index_home'),
    path('staffs/',views.staffs, name='staffs'),
    path('orders/',views.orders, name='orders'),
    path('products/',views.products, name='products'),

    #crud

    path('staff_details/<int:pk>/',views.Details_of_Staff.as_view(),name='staff_details'),


   # path('add_new_product/',views.Add_New_Product.as_view(),name='add_new_product'),
   path('edit_product/<int:pk>/',views.Edit_Product.as_view(),name='edit_product'),
    path('delete_product/<int:pk>/',views.Delete_Product.as_view(),name='delete_product'),
     #delete using function based view

    # path('deleteproduct/<int:pk>/',views.delete_product, name='delete_product'),

    path('makerequest/<int:id>/',views.make_request, name='make_request'),
    


]
