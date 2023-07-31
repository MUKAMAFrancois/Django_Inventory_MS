# This is a simple demonstration of normal Inventory Management system using Django( Backend) and Bootstrap (client side).

Django is best Web application framework that is being used by large companies.

Before using this project for study purposes, you must know:
** Python basics ( classes, functions)
** Django MVT architecture (models, views, templates) 
** django signals
** CRUD (Create, Read, Upadate and Delete) functionalies.


###### you will see some commented codes for CBV performing similar roles as FBV

In this project:
--> We created two apps : users and dashboard.

-->In the users app, a user can create new account after he is redirected to login page. He can logout and At the moment of creating an account his profile is directly created using Django signals.

--> A user can edit his profile, where I have used Django ModelForms.
--> User has chance to change his password and whenever he has forgotten the password he can get chance to reset it.

---> The Admin( and permitted staffs) has their Interface where they have full permissions and anyone with no these permissions has his own inteface.

**A normal client can only make a request, view his profile, and view the product details**

**Admin can Enter a new product in database (Create a product), Update details of Product, Delete a product, View all profiles, view his own profile, View products, and assigning permissions ***




