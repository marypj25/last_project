from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import my_site

def page(request, pk):
    nav_objects = my_site.objects.values('id','page_nav', 'page_nav_position').filter(page_nav_position__gt=0).order_by('-page_nav_position')
    print("nav_objects: ", nav_objects)
    content_object = my_site.objects.values().get(id=pk)
    print("content_object:\n", content_object)
    context = {'pk': pk, 'nav_objects': nav_objects, 'content_object': content_object}
    return render(request, 'home_page.html', context)




