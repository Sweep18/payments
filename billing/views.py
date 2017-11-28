from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from .forms import PaymentForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'billing/login.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class BillingView(LoginRequiredMixin, FormView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('error'))
        return super(BillingView, self).dispatch(request, *args, **kwargs)

    form_class = PaymentForm
    template_name = 'billing/main.html'


class ErrorView(LoginRequiredMixin, TemplateView):
    template_name = 'billing/error.html'
