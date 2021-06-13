from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, EditingProfilePageView, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from theblog.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    # form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):  # passing categories data to create a dropdown menu on navbar
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

# class EditProfilePageView(generic.UpdateView):
#     model = Profile
#     template_name = 'registration/edit_profile_page.html'
#     fields = ['profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'bio']
#     success_url = reverse_lazy('home')

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditingProfilePageView
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
