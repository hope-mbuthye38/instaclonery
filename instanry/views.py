from django.shortcuts import render,redirect
from .models import Comment, Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, NewCommentForm, NewProfileForm


# Create your views here.
def welcome(request):
    title="Instagram's finest clone"
    images =Image.objects.all()
    return render(request, 'index.html', {'images': images})

@login_required(login_url='/accounts/login/')
def profile(request):
    title="My profile"

    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        
        return redirect('profile')

    else:
        form = NewProfileForm()
    user=current_user
    profile =Profile.get_profile(user)
    return render(request, 'profile.html', {'profile': profile, 'title': title, 'form': form})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    comments =Comment.objects.all()
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('new_comment')

    else:
        form = NewCommentForm()
    return render(request, 'new-comment.html', {"form": form, "comments": comments})

def search_results(request):
    title="Find"
    images=Image.objects.all()
    
    
    if 'image_name' in request.GET and request.GET['image_name']:
        search_term = request.GET.get('image_name')
        found_results = Image.objects.filter(name__icontains=search_term)
        message = f"{search_term}"


        return render(request, 'search.html',{'title':title,'results': found_results, 'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# Create your views here.
