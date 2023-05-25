from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import shorturl
import random
import string
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/admin/login/')
def dashboard(request):
    urls = shorturl.objects.all().order_by("-id")
    return render(request, 'url/dashboard.html', {'urls': urls})


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


@login_required(login_url='/admin/login/')
def generate(request):
    if request.method == "POST":
        # generate
        pass
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_query=short)
            if not check:
                newurl = shorturl(
                    original_url=original,
                    short_query=short,
                )
                newurl.save()
                return redirect(dashboard)
            else:
                messages.error(request, "Already Exists")
                return redirect(dashboard)
        elif request.POST['original']:
            # generate randomly
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = shorturl.objects.filter(short_query=short)
                if not check:
                    newurl = shorturl(
                        original_url=original,
                        short_query=short,
                    )
                    newurl.save()
                    return redirect(dashboard)
                else:
                    continue
        else:
            messages.error(request, "Empty Fields")
            return redirect(dashboard)
    else:
        return redirect(dashboard)


def home(request, query=None):
    if not query or query is None:
        return render(request, 'url/home.html')
    else:
        try:
            check = shorturl.objects.get(short_query=query)
            check.visits = check.visits + 1
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'url/home.html', {'error': "error"})


@login_required(login_url='/admin/login/')
def users(request):
    users = User.objects.all().order_by("-id")
    return render(request, 'url/users.html', {'users':users})