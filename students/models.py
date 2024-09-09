from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Students(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    email = models.CharField(max_length=255, verbose_name="Почта")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    projects = models.ManyToManyField('Projects', verbose_name="Проекты")
    skill = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Умения")
    owner = models.ForeignKey('auth.User', related_name='Проекты', on_delete=models.CASCADE, default=1)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('student', kwargs={'student_id': self.pk})

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'


class Certificates(models.Model):
    certificate_name = models.CharField(max_length=255, verbose_name="Название")
    organization_name = models.CharField(max_length=255, verbose_name="Организация")
    issue_date = models.DateField(verbose_name="Дата выдачи")
    student = models.ForeignKey('Students', on_delete=models.PROTECT, verbose_name="Студент")
    history = HistoricalRecords()

    def __str__(self):
        return self.certificate_name

    class Meta:
        verbose_name = 'Сертификаты'
        verbose_name_plural = 'Сертификаты'


class Projects(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    history = HistoricalRecords()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Education(models.Model):
    level = models.CharField(max_length=255, verbose_name="Уровень")
    institution_name = models.CharField(max_length=255, verbose_name="Институт")
    specialization = models.CharField(max_length=255, verbose_name="Специализация")
    graduation_date = models.DateField(blank=True, verbose_name="Дата выпуска")
    student = models.OneToOneField('Students', on_delete=models.PROTECT, verbose_name="Студент")
    history = HistoricalRecords()

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class Skills(models.Model):
    skill_name = models.CharField(max_length=255, verbose_name="Название")
    history = HistoricalRecords()

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = 'Области знаний'
        verbose_name_plural = 'Области знаний'


class Workexperiences(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Компания")
    position_name = models.CharField(max_length=255, verbose_name="Позиция")
    description = models.TextField(blank=True, verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала работы")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата конца работы")
    student = models.OneToOneField('Students', on_delete=models.PROTECT, verbose_name="Студент")
    history = HistoricalRecords()

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

