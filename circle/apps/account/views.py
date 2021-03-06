from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render

from .forms import RegistrationForm


@login_required
def dashboard(request):
    return render(request, 'account/dashboard/dashboard.html', {'section': 'profile'},)


def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data["email"]
            user.set_password(registerForm.cleaned_data["password"])
            user.is_active = False
            user.save()
            # current_site = get_current_site(request)
            # subject = 'Activate your Account'
            # message = render_to_string(
            #     "account/registration/account_activation_email.html",
            #     {
            #         "user": user,
            #         "domain": current_site.domain,
            #         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            #         "token": account_activation_token.make_token(user),
            #     },
            # )
            # user.email_user(subject=subject, message=message)
            return render(request, {'form': registerForm})
            # return render(request, "account/registration/register_email_confirm.html", {"form": registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/register.html', {'form': registerForm})
