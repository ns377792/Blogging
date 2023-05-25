from django.shortcuts import redirect, render

from blog.models import Category
from .models import Page
from blog.views import baseData
# Create your views here.
def page(request, page):
    pagedata = Page.objects.filter(url = page).first()
    featured_category = Category.objects.filter(featured=True)
    categoryp = Category.objects.all()
   
    
    if pagedata is not None:
        context = {
            "page":pagedata,
            "navThemeBar":baseData(),
            "featured_category":featured_category,
             "categoryp":categoryp,
            
        }
        if pagedata.sidebar:
            return render(request, "pages/page_with_sidebar.html", context)
        else:
            return render(request, "pages/page.html", context)
    else:
        return redirect("/")