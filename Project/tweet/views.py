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



def DeleteTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        tweet.delete()
        return redirect('showtweet')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'Delete_T.html', {'form': form})