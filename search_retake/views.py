from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from .pagination import StandardResultsSetPagination
from .serializers import RetakeSerializers
from .models import Retake, Discipline, Teacher, Group


def search_retake(request):
    return render(request, 'search_retake.html')


class RetakeListing(ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = RetakeSerializers

    def get_queryset(self):
        query_list = Retake.objects.all()

        discipline = self.request.query_params.get('discipline', None)
        teacher = self.request.query_params.get('teacher', None)
        course = self.request.query_params.get('course', None)
        group = self.request.query_params.get('group', None)

        if discipline:
            query_list = query_list.filter(discipline=discipline)
            print(query_list, '\n\n\n')
        if teacher:
            query_list = query_list.filter(teacher=teacher)
        if course:
            query_list = query_list.filter(group__course=course)
        if group:
            query_list = query_list.filter(group=group)
        return query_list


def get_disciplines(request):
    if request.is_ajax and request.method == 'GET':
        discipline_ids = Retake.objects.order_by('discipline').values_list('discipline').distinct()
        disciplines = [(i[0], str(Discipline.objects.get(id=i[0]))) for i in list(discipline_ids)]
        data = {
            'disciplines': disciplines,
        }
        return JsonResponse(data, status=200)


def get_teachers(request):
    if request.is_ajax and request.method == 'GET':
        discipline = request.GET.get('discipline')
        teacher_ids = Retake.objects.filter(discipline=discipline).order_by('teacher').values_list('teacher').distinct()
        teachers = [(i[0], str(Teacher.objects.get(id=i[0]))) for i in list(teacher_ids)]
        data = {
            'teachers': teachers,
        }
        return JsonResponse(data, status=200)


def get_groups(request):
    if request.is_ajax and request.method == 'GET':
        course = request.GET.get('course')
        groups = Retake.objects.filter(group__course=course).order_by('group').values_list('group').distinct()
        groups = [(i[0], str(Group.objects.get(id=i[0]))) for i in list(groups)]
        data = {
            'groups': groups,
        }
        return JsonResponse(data, status=200)