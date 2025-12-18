from django.shortcuts import render
from .form import TweetForm
from .models import Tweet
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def tweet(request):
    return render(request, 'tweet.html')

# To Show the all tweeets
def Showtweet(request):
    tweets = Tweet.objects.all().order_by('-create_at')
    return render(request, 'Showtweet.html', {'tweets': tweets})


# To Create the tweet
def CreateTweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweets = form.save(commit=False)
            tweets.user = request.user
            tweets.save()
            return redirect('Showtweet')
    else:
        form = TweetForm()

    return render(request, 'Create_T.html', {'form': form})

