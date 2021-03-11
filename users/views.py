from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(form.cleaned_data.get('password1'))
        return redirect('api:token_obtain_pair')
    context = {
        'form': form,
    }
    return render(request, 'registration_form.html', context)