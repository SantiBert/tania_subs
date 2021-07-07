import pdb
from django.shortcuts import render, HttpResponseRedirect
from django.utils.html import format_html
from django.views.generic import FormView
from django.contrib import messages
from .models import Suscribes
from .form import SuscribeForm


def LendingCreateView(request):
    text1 = 'Felicidades podes descargar '
    text2 = 'aquí'
    if request.method == 'POST':
        form = SuscribeForm(request.POST)
        if form.is_valid():
            messages.success(
                request, format_html("<p class='mb-0'>{}<a href='https://drive.google.com/file/d/1G4dDTn9cnAwRYrIn-9IbcOoNxJsT5G1D'>{}</a></p>", text1, text2))
            form.save()
    else:
        form = SuscribeForm()
    return render(request, 'index.html', {'form': form})


"""
class LendingCreateView(FormView):
    model = Suscribes
    form_class = SuscribeForm
    template_name = 'index.html'
    success_url = None

    def form_valid(self, form):
        text1 = 'Felicidades podes descargar '
        text2 = 'aquí'
        messages.success(self.request, format_html(
            "<p class='mb-0'>{}<a href='https://drive.google.com/file/d/1G4dDTn9cnAwRYrIn-9IbcOoNxJsT5G1D'>{}</a></p>", text1, text2))
        form.save()
        return super(self).form_valid(form)
"""
