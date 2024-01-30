"""For Institutions and DS Divisions MOH Areas"""
from django.db import models

#  Wagtail part
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index


@register_snippet
class District(models.Model):
    """District"""

    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=10)

    def __str__(self):
        return self.code_name.__str__()


@register_snippet
class MOHArea(index.Indexed, models.Model):
    """MOH Area"""

    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area = models.FloatField(blank=True, null=True)
    PHM_areas = models.IntegerField(null=True, blank=True, verbose_name="#PHM Areas")
    PHI_areas = models.IntegerField(null=True, blank=True, verbose_name="#PHI Areas")

    class Meta:
        verbose_name = "MOH Area"

    panels = [
        FieldPanel("name"),
        FieldPanel("district"),
        FieldPanel("area"),
        FieldPanel("PHM_areas"),
        FieldPanel("PHI_areas"),
    ]
    search_fields = [
        index.SearchField("name"),
        index.AutocompleteField("name"),
    ]

    def __str__(self):
        return self.name.__str__()


@register_snippet
class DSDivision(models.Model):
    """DS Division"""

    name = models.CharField(max_length=50)
    area = models.FloatField(blank=True, null=True)
    moh_area = models.ForeignKey(
        MOHArea, on_delete=models.CASCADE, verbose_name="MOH Area"
    )

    class Meta:
        verbose_name = "DS Division"

    def __str__(self):
        return self.name.__str__()


@register_snippet
class Institution(models.Model):
    """Institution"""

    TYPES = [
        ("BHA", "BHA"),
        ("BHB", "BHB"),
        ("BHC", "BHC"),
        ("DHA", "DHA"),
        ("DHB", "DHB"),
        ("DHC", "DHC"),
        ("PMCU", "PMCU"),
        ("MOH", "MOH"),
        ("UNIT", "UNIT"),
        ("TH", "TH"),
        ("ADC", "ADC"),
        ("SDC", "SDC"),
        ("Other", "Other"),
    ]
    name = models.CharField(max_length=50)
    name_si = models.CharField(max_length=60)
    type = models.CharField(max_length=5, choices=TYPES)
    ds_division = models.ForeignKey(DSDivision, on_delete=models.PROTECT)
    moh_area = models.ForeignKey(MOHArea, on_delete=models.PROTECT)
    telephone_nu = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name.__str__()
