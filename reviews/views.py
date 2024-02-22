from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import TouristReview
from .forms import ReviewForm
from .. import reviews


def review_list(request):
    if request.method == 'GET':
        review = TouristReview.objects.all()
        return render(request, 'review.html', {'review': reviews})

def add_review(request):
    if request.method == 'POST':
        form =  ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')




