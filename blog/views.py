from django.shortcuts import render , get_object_or_404
from .models import Post  # . means current directory
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView ,CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.

def home(request):  # function based views 
    context = { 'posts' : Post.objects.all() }
    return render(request,'blog/home.html', context)


# class based views looks for this type of template names by convention : <app>/<model>_<viewtype>.html
# for looping var , it looks for 'object' by default in the tempplate
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' # what to loop over
    ordering = ['-date_posted']  # - does opposite ordering
    paginate_by = 5     #  to give us pagination functionality

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' # what to loop over
    paginate_by = 5     #  to give us pagination functionality

    # overriding get_query_set method
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username')) # getting username from url
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin , CreateView):  # login required to access this view
    model = Post
    fields = ['title' , 'content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user # setting author to current user
        return super().form_valid(form)

# doesnt require additional template , shares with PostCreateView template
class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):  # login required to access this view
    model = Post
    fields = ['title' , 'content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user # setting author to current user
        return super().form_valid(form)
    
    def test_func(self):   # this is run by the UserPassesTestMixin
        curr_post = self.get_object() # current post
        if self.request.user == curr_post.author:
            return True
        return False

class PostDeleteView( LoginRequiredMixin , UserPassesTestMixin , DeleteView ):
    model = Post
    
    success_url = '/'

    def test_func(self):   # this is run by the UserPassesTestMixin
        curr_post = self.get_object() # current post
        if self.request.user == curr_post.author:
            return True
        return False
    
def about(request):
    return render(request, 'blog/about.html' , {'title' : 'About'})


