from django.shortcuts import render, HttpResponse, redirect
from url.models import shorturl

def urlshort(request, query=None):
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