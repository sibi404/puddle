from django.shortcuts import render,redirect
from item.models import Category,Item
from . forms import SignupForm,LoginForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {'items':items,'categories':categories}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         # print("This is form ",form)
#         print("Reached here")
#         if form.is_valid():
#             print("dfdffsfdfadfsfffffffffffffffffffffffffffffffffffffffffff")
#             first_name = form.cleaned_data['username']
#             print("This is username ",first_name)
#             return redirect('/')
#         else:
#             print("Error")
#             print(form.errors)
#     else:
#         form = LoginForm()

#     return render(request,'login.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("This is signup form ",form)

        if form.is_valid():
            print("This is the username ",form.cleaned_data['username'])
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request,'signup.html',{'form':form})