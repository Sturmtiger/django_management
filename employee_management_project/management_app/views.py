from django.shortcuts import render, get_object_or_404
from .models import Company

# Create your views here.


def index(request):
    """Companies list view."""
    companies = Company.objects.all()
    return render(
        request,
        'management_app/index.html',
        {'companies': companies},
        )


def details(request, company_id):
    """Company details view."""
    company = get_object_or_404(Company, id=company_id)
    return render(
        request,
        'management_app/details.html',
        {'company': company},
    )
