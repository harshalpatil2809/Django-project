from .form import TweetForm, UserRegistrationForm
from .models import Tweet, UserProfile
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout


# Create your views here.
def tweet(request):
    return render(request, 'Layout.html', {'user':request.user})

# To Show the all tweeets
def Showtweet(request):
    tweets = Tweet.objects.all().order_by('-create_at')
    return render(request, 'Showtweet.html', {'tweets': tweets})

def FullTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, "Full_T.html", {"tweet": tweet})


# To Create the tweet
@login_required
def CreateTweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('showtweet')
        else:
            print(form.errors)
    else:
        form = TweetForm()

    return render(request, 'Create_T.html', {'form': form})


# To Edit the tweet
@login_required
def EditTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('showtweet')
        else:
            print(form.errors)
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'Create_T.html', {'form': form})


@login_required
def DeleteTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        tweet.delete()
        return redirect('showtweet')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'Delete_T.html', {'form': form})


# User Registration Form
def UserRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            # Create user profile with image
            image = request.FILES.get('image')
            UserProfile.objects.create(user=user, image=image)
            
            login(request, user)
            return redirect('showtweet')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


# User Login Form
def Login(request):
    return render(request, "registration/login.html")


# User Logout Form
def Logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('showtweet')

    return render(request, 'registration/Logedout.html')