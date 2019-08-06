import random

from datacenter.models import Chastisement, Schoolkid, Mark, Lesson, Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print(f'Найдено несколько учеников с именем {name}. Уточните запрос.')
    except ObjectDoesNotExist:
        print(f'Ученик с именем {name} отсутствует в базе.')


def delete_chastsements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def set_commendation(schoolkid, subject):
    COMMENDATIONS = ['Молодец!',
                     'Отлично!'
                     'Хорошо!',
                     'Гораздо лучше, чем я ожидал!'
                     'Ты меня приятно удивил!',
                     'Ты сегодня прыгнул выше головы!',
                     'Я поражен!',
                     'Уже существенно лучше!',
                     'Потрясающе!']
    year = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lesson = Lesson.objects.filter(group_letter=group_letter, year_of_study=year, subject__title=subject).order_by('-date')[0]
    Commendation.objects.create(text=random.choice(COMMENDATIONS), schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher, created=lesson.date)