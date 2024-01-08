from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

from .forms import CustomExportForm
from .models import *
from import_export.fields import Field


class StudentsResource(resources.ModelResource):

    def __init__(self, **kwargs):
        super().__init__()
        self.skill = kwargs.get("skill")

    full_name = Field()

    class Meta:
        model = Students

    def dehydrate_full_name(self, students):
        first_name = students.first_name
        last_name = students.last_name
        return f"{first_name} {last_name}"

    def filter_export(self, queryset, *args, **kwargs):
        return queryset.filter(skill_id=self.skill)


class StudentsAdmin(ImportExportModelAdmin):
    resource_class = StudentsResource
    export_form_class = CustomExportForm
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_editable = ('birth_date',)
    list_filter = ['projects']

    def get_export_resource_kwargs(self, request, *args, **kwargs):
        export_form = kwargs["export_form"]
        if export_form:
            return dict(skill=export_form.cleaned_data["skills"].id)
        return {}


class ProjectsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'project_name', 'description', 'start_date', 'end_date')
    list_display_links = ('id', 'project_name')
    search_fields = ('project_name', 'description')
    list_editable = ('description', 'start_date', 'end_date')
    list_filter = ['end_date']


class CertificatesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'certificate_name', 'organization_name', 'issue_date')
    list_display_links = ('id', 'certificate_name')
    search_fields = ('certificate_name', 'organization_name')
    list_editable = ('issue_date',)
    list_filter = ['issue_date']


class WorkexperiencesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'company_name', 'position_name', 'description', 'start_date', 'end_date')
    list_display_links = ('id', 'company_name')
    search_fields = ('company_name', 'position_name', 'student_id', 'description')
    list_editable = ('description', 'start_date', 'end_date')
    list_filter = ['company_name']


class EducationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'institution_name', 'specialization', 'graduation_date', 'level')
    list_display_links = ('id', 'institution_name')
    search_fields = ('student_id', 'institution_name', 'specialization', 'level')
    list_editable = ('graduation_date',)
    list_filter = ['institution_name']


class SkillsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'skill_name')
    list_display_links = ('id', 'skill_name')
    search_fields = ('id', 'skill_name')


admin.site.register(Students, StudentsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Workexperiences, WorkexperiencesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skills, SkillsAdmin)
