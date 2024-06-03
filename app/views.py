from django.shortcuts import render
from .models import Group, chat


# Create your views here.
def index_page(request, groupname):
    group = Group.objects.filter(name=groupname).first()
    print(group)
    if group:
        chats=chat.objects.filter(group=group)

    else:
        group = Group.objects.create(name=groupname)
        group.save()
        chats = []


    return render(request, 'index.html', {'groupname': groupname, 'chats': chats})
