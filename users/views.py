# from django.shortcuts import render, redirect
# from .forms import UserForms
# from django.http import HttpResponse
# from .models import User
# def index(request):
#     if request.method == "POST":
#         my_form = UserForms(request.POST)
#         if my_form.is_valid():
#             name = my_form.cleaned_data["name"]
#             surname = my_form.cleaned_data["surname"]
#             gender = my_form.cleaned_data["gender"]
#             adult = my_form.cleaned_data["adult"]
#             users_form = User(name=name,surname=surname,gender=gender, adult=adult)
#             users_form.save() 
#             return redirect('/polls/all')
#     else:
#         form = UserForms()
#     return render(request, 'users/index.html', {"form": UserForms})


# def succes(request):
#     return HttpResponse("Succes")