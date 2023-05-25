from typing import Coroutine
from django.shortcuts import redirect, render
from .models import blogpost, Category, Comment
from .models import Contact
from django.contrib import messages
from django.db import models
from django.contrib import admin
from blogtheme.models import FooterHeading, FooterLink, Navlog, copyrightClaim
from blogtheme.models import Nav_menu
from blogtheme.models import Nav_social_media_icon


# Create your views here.
def blog(request):
    blog = blogpost.objects.all().order_by("-id")
    categoryp = Category.objects.all()
    featured_posts = blogpost.objects.filter(featured_post=True)
    featured_category = Category.objects.filter(featured=True)
    return render (request, 'blog/index.html', {'blogs':blog, "categoryp":categoryp, "navThemeBar":baseData(), "featured_posts":featured_posts, "featured_category":featured_category})

def blogpostreadmore(request, slug):
    blogp = blogpost.objects.get(slug = slug)
    comments = Comment.objects.filter(blog_post__slug = slug).order_by("-id")
    categoryp = Category.objects.all()
    featured_posts = blogpost.objects.filter(featured_post=True)
    featured_category = Category.objects.filter(featured=True)
    return render(request, 'blog/blogpost.html',{"blogp":blogp, "categoryp":categoryp, "comments":comments, "navThemeBar":baseData() , "featured_posts":featured_posts, "featured_category":featured_category})
    

def categoryposts(request, category):
    blogp = blogpost.objects.filter(category__name = category)
    categoryp = Category.objects.all()
    featured_posts = blogpost.objects.filter(featured_post=True)
    featured_category = Category.objects.filter(featured=True)
    return render(request, 'blog/index.html',{"featured_category":featured_category,"blogs":blogp, "featured_posts":featured_posts, "categoryp":categoryp, "navThemeBar":baseData()})
    
def Contactus(request):
    featured_category = Category.objects.filter(featured=True)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, "Thank you for Contact us")
        return render(request, "blog/contactus.html",{"featured_category":featured_category,"navThemeBar":baseData()})    
    return render(request, "blog/contactus.html", {"featured_category":featured_category,"navThemeBar":baseData()})

def postComment(request):
    if request.method == "POST":
        slugComment = request.POST['slug']
        userComment = request.POST['user']
        commentComment = request.POST['comment']

        blogpostComment = blogpost.objects.get(slug = slugComment)
        
        comment = Comment(user = userComment, blog_post=blogpostComment, comment=commentComment)
        comment.save()

        messages.success = "your comment has been added successfully"
        return redirect("/blog/"+slugComment)
    return redirect('/')

def baseData():
    logo = Navlog.objects.filter(logo="logo").first()
    pages = Nav_menu.objects.all()
    righticon = Nav_social_media_icon.objects.all()
    foot1 = FooterLink.objects.filter(head__sno = "first")
    foot2 = FooterLink.objects.filter(head__sno = "second")
    foot3 = FooterLink.objects.filter(head__sno = "third")
    foot4 = FooterLink.objects.filter(head__sno = "fourth")
    footh1 = FooterHeading.objects.filter(sno="first").first()
    footh2 = FooterHeading.objects.filter(sno="second").first()
    footh3 = FooterHeading.objects.filter(sno="third").first()
    footh4 = FooterHeading.objects.filter(sno="fourth").first()
    copy = copyrightClaim.objects.filter(location="footer").first()
    dict_to_return = {
        "logo":logo,
        "pages":pages,
        "righticon":righticon,
        "footer":{
            "foothead":{
                "footh1":footh1,
                "footh2":footh2,
                "footh3":footh3,
                "footh4":footh4
            },
            "footerlink":{
                "foot1":foot1,
                "foot2":foot2,
                "foot3":foot3,
                "foot4":foot4
            },
            "copyrightmsg":copy
        }

    }
    return dict_to_return
