from django.shortcuts import render, redirect
from .forms import userForm
from .models import User

def createUser(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlist")
    else:
        form = userForm()

    return render(request, "actions/createUser.html", {"form": form})  

def showUsers(request):
    users= User.objects.all()
    return render(request, "actions/userlist.html", {"data":users})

def deleteUser(request, id):
    user= User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect("userlist")
    return render(request, "actions/delete.html", {"user": user})

def updateUser(request, id):
    user= User.objects.get(id=id)
    form= userForm(request.POST or None, instance=user)
    if form.is_valid():
         form.save()
         return redirect("userlist")
    return render(request, "actions/updateUser.html", {"form": form})

    
