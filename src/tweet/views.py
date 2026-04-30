from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

@login_required
def tweet_view(request):
    tweets = Tweet.objects.order_by('-created_at')
    
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet")
    else:
        form = TweetForm()

    return render(request, "tweet.html", {
        "form": form,
        "tweets": tweets
    })
