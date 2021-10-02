from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Mess, Space

def home_view(request):
    context = {}
    messes = Mess.objects.all()
    print(messes)
    context['messes'] = messes
    return render(request, 'home.html', context)


def mess_details_view(request, mess_name):
    context = {}
    print(mess_name)
    mess_details = Space.objects.filter(mess__name=mess_name)
    print(mess_details)
    context['spaces'] = mess_details
    return render(request, "mess_details.html", context)



def space_details_view(request, mess_name, space_name):
    context = {}
    print(mess_name)
    print(space_name)
    space_details = Space.objects.filter(mess__name=mess_name, name=space_name)[0]
    # space_details = Space.objects.filter(mess__name = "White House", name =  "W_H 1A")[0]
    print(space_details.mess_type)
    context["space"] = space_details
    return render(request, "spece_details.html", context)