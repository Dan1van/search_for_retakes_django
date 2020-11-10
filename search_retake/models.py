from django.db import models
from django.core.exceptions import ValidationError

from smart_selects.db_fields import ChainedForeignKey


class Group(models.Model):
    _COURSE_CHOICES = (
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс')
    )

    course = models.IntegerField(choices=_COURSE_CHOICES, verbose_name='Курс', help_text='Выберите курс')
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите группу', unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя', help_text='Введите имя преподавателя')
    fathers_name = models.CharField(max_length=100, verbose_name='Отчество', help_text='Введите отчество преподавателя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', help_text='Введите фамилию преподавателя')

    def __str__(self):
        return f'{self.last_name} {self.name[0]}. {self.fathers_name[0]}.'

    def display_discipline(self):
        return ', '.join([discipline.name for discipline in self.disciplines.all()])

    display_discipline.short_description = 'Дисциплина'


class Discipline(models.Model):
    _SEMESTER_CHOICES = (
        (1, '1 семестр'),
        (2, '2 семестр'),
        (3, '3 семестр'),
        (4, '4 семестр'),
        (5, '5 семестр'),
        (6, '6 семестр'),
        (7, '7 семестр'),
        (8, '8 семестр')
    )

    _EXAM_TYPE = (
        (1, 'Зачет'),
        (2, 'Экзамен')
    )

    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название дисциплины')
    semester = models.IntegerField(choices=_SEMESTER_CHOICES, verbose_name='Семестр', help_text='Выберите семестр')
    exam_type = models.IntegerField(choices=_EXAM_TYPE, verbose_name='Вид контроля', help_text='Выберите вид контроля')
    teachers = models.ManyToManyField(Teacher, related_name='disciplines', verbose_name='Преподаватели',
                                      help_text='Выберите преподавателей')

    def display_teacher(self):
        return ', '.join([teacher.__str__() for teacher in self.teachers.all()])

    display_teacher.short_description = 'Преподаватели'

    def __str__(self):
        return f'{self.name}, {self.semester} сем.'


class Retake(models.Model):
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)
    teacher = ChainedForeignKey(
        Teacher,
        chained_field='discipline',
        chained_model_field='disciplines',
        verbose_name='Преподаватель',
    )
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    audience = models.CharField(max_length=5, verbose_name='Номер аудитории', help_text='Введите номер аудитории')
    date = models.DateTimeField(verbose_name='Дата', help_text='Введите дату пересдачи')

    def __str__(self):
        return f'{self.discipline.name}, {self.group.name}'
