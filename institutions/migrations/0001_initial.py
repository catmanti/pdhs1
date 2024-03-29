# Generated by Django 5.0.1 on 2024-01-28 05:15

import django.db.models.deletion
import wagtail.search.index
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("code_name", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="DSDivision",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("area", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "DS Division",
            },
        ),
        migrations.CreateModel(
            name="MOHArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("area", models.FloatField(blank=True, null=True)),
                (
                    "PHM_areas",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="#PHM Areas"
                    ),
                ),
                (
                    "PHI_areas",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="#PHI Areas"
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="institutions.district",
                    ),
                ),
            ],
            options={
                "verbose_name": "MOH Area",
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_si", models.CharField(max_length=60)),
                (
                    "type",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "telephone_nu",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "ds_division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="institutions.dsdivision",
                    ),
                ),
                (
                    "moh_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="institutions.moharea",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dsdivision",
            name="moh_area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="institutions.moharea",
                verbose_name="MOH Area",
            ),
        ),
    ]
