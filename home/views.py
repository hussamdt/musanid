from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import Settings


#@login_required()
def home(request):
    
    title = 'Home Page'
    featured_articles = Article.objects.filter(published = True).filter(featured = True).order_by('create_date')[:3]
    second_articles = Article.objects.filter(published = True).filter(featured = False).order_by('create_date')
    
    context = {'title': title,
               'featured_articles': featured_articles,
               'second_articles': second_articles
            }
            
    return render(request,'home/index.html', context)


def single_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request,'home/single_article.html', context);

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'home/contact.html', {'form': form})
    
    # send email need to be implemented
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, 'home/contact.html', {'form': form})
    
    #email_to = Settings.email
    subject = f"{form.cleaned_data['email']} querying {form.cleaned_data['subject']} service"
    message = f"You have new query from:\n Name: {form.cleaned_data['name']}\n Email: {form.cleaned_data['email']}\n Message:\n {form.cleaned_data['message']}"
    email = form.cleaned_data['email']
    email_to = ['faisal.almansour@musanid.com', 'almogbil.f@musanid.com']

    try:
        send_mail(subject, message, email, email_to, fail_silently=False)
        # send user to Thank you page (will be developed after server test)
        return render(request, 'home/thanks_page.html')
    except Exception as e:
        # Exception return temporarly for development purpose
        return HttpResponse(f'Server Eror {str(e)} <br><br> <button onclick="window.history.back()">Back</button>')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'home/login.html')
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'home/login.html', {'message': 'wrong username or password'})
    

def logout_view(request):
    logout(request)
    return redirect('/login')



