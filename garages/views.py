from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, _get_queryset, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView, View, FormView
from .models import *
from .forms import *


# Create your views here.

class IndexView(ListView):
    template_name = 'garages/index.html'
    fields = (
        'name',
        'address',
        'phone',
        'description',
    )
    page_title = "Home"
    model = Garage

    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return None


class GarageDetailView(DetailView):
    page_title = "Garage View"
    model = Garage
    exclude = ()

    nodes = Category.objects.all()

    def get_object(self, queryset=None):
        return Garage.objects.first()

        # def dispatch(self, request, *args, **kwargs):
        #     self.garage = Garage.objects.first()
        #     self.page_title = "{} Information".format(self.garage.name)
        #
        #     def get_list_or_none(klass, *args, **kwargs):
        #         queryset = _get_queryset(klass)
        #         obj_list = list(queryset.filter(*args, **kwargs))
        #         if obj_list:
        #             return obj_list
        #         return []
        #
        #     self.manufacturers = get_list_or_none(Manufacturer, garage=self.garage)
        #     return super().dispatch(request, *args, **kwargs)


class RegisterOrLoginView(ListView):
    template_name = 'registerorlogin.html'
    page_title = "Register Or Login"

    def get_queryset(self):
        return None
        return super().get_queryset()


class LoginView(FormView):
    page_title = "Login"
    template_name = "login.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('garages:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None:
            if user.is_active:
                login(self.request, user)
                if self.request.GET.get('from'):
                    return redirect(
                        self.request.GET['from'])  # SECURITY: check path
            else:
                form.add_error(None, "User isn't active anymore - please contact admin")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Username or Password incorrect")
            return self.form_invalid(form)
        return redirect('garages:index')


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("garages:index")


# class SignupRestaurantView(FormView):
#     page_title = "Signup Restaurant User"
#     template_name = "login.html"
#     form_class = SignupForm
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return redirect('campaigns:restaurant_list')
#         return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         if form.cleaned_data['password'] != form.cleaned_data.pop('password_recheck'):
#             form.add_error(None, "Passwords do not match")
#             return self.form_invalid(form)
#         user = User.objects.create_user(**form.cleaned_data)
#         user = authenticate(**form.cleaned_data)
#
#         # Add new user to ProfileUser and CampaignUser Or WriterUser
#         restaurant_owner = RestaurantOwner(user=user, )
#         restaurant_owner.full_clean()
#         restaurant_owner.save()
#
#         # Login
#         if user is not None:
#             if user.is_active:
#                 login(self.request, user)
#             else:
#                 form.add_error(None, "Disabled account")
#                 return self.form_invalid(form)
#             if self.request.GET.get('from'):
#                 return redirect(
#                     self.request.GET['from'])  # SECURITY: check path
#             return redirect('bite:restaurant_list')


class SignupCustomerView(FormView):
    page_title = "Customer Signup"
    template_name = "login.html"
    form_class = SignupForm
    # logger.error("Enter form_valid")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('garages:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # logger.error("Enter form_valid")
        if form.cleaned_data['password'] != form.cleaned_data.pop('password_recheck'):
            form.add_error(None, "Passwords do not match")
            return self.form_invalid(form)
        # logger.error("Checked Passwords Match")
        # user = User.objects.create_user(**form.cleaned_data)
        user = authenticate(**form.cleaned_data)
        # logger.error("Authenticated User")

        # Add new user to ProfileUser and CampaignUser Or WriterUser
        customer = User(user=user, )
        customer.full_clean()
        customer.save()

        # Login
        if user is not None:
            if user.is_active:
                login(self.request, user)
            else:
                form.add_error(None, "Disabled account")
                return self.form_invalid(form)
            if self.request.GET.get('from'):
                return redirect(
                    self.request.GET['from'])  # SECURITY: check path
            return redirect('garages:index')
