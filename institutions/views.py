from django.views.generic import ListView
from .models import Institution, MOHArea, DSDivision


class InstiturionListView(ListView):
    """List of Institutions"""

    model = Institution


class MOHAreaListView(ListView):
    """List of MOH Areas"""

    model = MOHArea


class DSDivisionListView(ListView):
    """List of DS Areas"""

    model = DSDivision
