from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


class StudentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_editable = ('birth_date',)
    list_filter = ['projects']


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
