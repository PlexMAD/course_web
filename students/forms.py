from django import forms
from import_export.forms import ExportForm

from students.models import Skills


class CustomExportForm(ExportForm):
    skills = forms.ModelChoiceField(
        queryset=Skills.objects.all(),
        required=True)