from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое
from django.urls import reverse_lazy

from blog.forms import DocumentForm
from .forms import SignUpForm


from .models import Documents, Comments
from .forms import DocumentForm
from .forms import CommentForm



def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Documents(docfile=request.FILES['docfile'])
            author = request.user
            published_date = timezone.now()
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Documents.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'blog/post_list.html', context)




@login_required
def post_list(request):
    Document = Documents.objects.order_by('-created_date').all()
    return render(request, 'blog/post_list.html', {'Document': Document})


def post_author(request):
    Document = Documents.objects.filter(request.user)


    return render(request, 'blog/post_author.html', {'Document': Document})


class BlogDeleteView(DeleteView): # Создание нового класса
    model = Documents
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('my-view')



@login_required
def post_detail(request, pk):
    new = get_object_or_404(Documents, pk=pk)
    comment = Comments.objects.filter(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(post_detail, pk)
    else:
        form = CommentForm()
    return render(request, "blog/post_detail.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})



#def post_edit(request, pk):
   # post = get_object_or_404(Documents, pk=pk)
    #if request.method == "POST":
       # #form = DocumentForm(request.POST)
       # form = DocumentForm(request.POST, request.FILES)
       # if form.is_valid():
           # form = form.save(commit=False)
           # Documents.author = request.user
           # Documents.published_date = timezone.now()
           # Documents.save()
           # return redirect('blog/post_list.html', pk=post.pk)
    #else:
       # form = DocumentForm()
    #return render(request, 'blog/post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post_new = form.save(commit=False)
            post_new.author = request.user
            post_new.save()
            return redirect('my-view')
    else:
        form = DocumentForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
        return redirect('my-view')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {'form': form})

