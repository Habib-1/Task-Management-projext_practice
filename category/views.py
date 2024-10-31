from django.shortcuts import render,redirect
from .import forms
# Create your views here.
# def addCategory(request):
#     if request.method=='POST':
#         cat_Form=forms.category_form(request.POST)
#         if cat_Form.is_valid():
#             cat_Form.save()
#             return redirect('home')
        
#     else:
#         cat_Form=forms.category_form()
#     return render(request,"category.html",{'form':cat_Form})

def addCategory(request):
    if request.method=='POST':
         form_c=forms.category_form(request.POST)
         if form_c.is_valid():
              form_c.save()
              return redirect('home')
    else:
        form_c=forms.category_form() 
   
    return render(request,'category.html',{'form':form_c})