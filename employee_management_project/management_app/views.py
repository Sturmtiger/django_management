from django.shortcuts import render, HttpResponse, reverse, get_object_or_404
from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.all()
    return render(
        request,
        'management_app/index.html',
        {'companies': companies},
        )


def details(request, id):
    company = get_object_or_404(Company, id=id)
    return render(
        request,
        'management_app/details.html',
        {'company': company},
    )