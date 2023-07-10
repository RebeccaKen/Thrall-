from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})