from django.db import models
from django.contrib.auth.models import User
import calendar
import datetime



def is_date_within_month(date, month, year):
    return date.month == month and date.year == year


def get_weeks_in_month(month, year):
    weeks = []
    num_days = calendar.monthrange(year, month)[1]
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, num_days)

    first_week_start = first_day - datetime.timedelta(days=first_day.weekday() + 1)
    first_week_end = first_week_start + datetime.timedelta(days=6)

    last_week_start = last_day - datetime.timedelta(days=last_day.weekday())
    last_week_end = last_week_start + datetime.timedelta(days=6)

    weeks.append((first_week_start, first_week_end))

    week_start = first_week_end + datetime.timedelta(days=1)
    while week_start < last_week_start:
        week_end = week_start + datetime.timedelta(days=6)
        weeks.append((week_start, week_end))
        week_start = week_end + datetime.timedelta(days=1)

    weeks.append((last_week_start, last_week_end))
    if not is_date_within_month(weeks[0][1], month, year):
        weeks.pop(0)
    weeks.pop(-1)

    we = list(weeks)
    i = 0
    l = []

    for x in we:
        w = x[0].strftime('%d/%m/%Y') + ' - ' + x[1].strftime('%d/%m/%Y')
        t = (w, w)
        l.append(t)
        i = i + 1

    result = tuple(l)

    return result

#semanas = get_weeks_in_month(5, 2023)


data_atual = datetime.datetime.now()
SEMANAS = get_weeks_in_month(data_atual.month, data_atual.year)


class HorasSemanais(models.Model):
    pode_null = False
    branco = True

    hr_seg = models.TimeField(null=True)
    hr_ter = models.CharField(max_length=200, null=pode_null, blank=branco)
    hr_qua = models.CharField(max_length=200, null=pode_null, blank=branco)
    hr_qui = models.CharField(max_length=200, null=pode_null, blank=branco)
    hr_sex = models.CharField(max_length=200, null=pode_null, blank=branco)
    hr_sab = models.CharField(max_length=200, null=pode_null, blank=branco)
    hr_dom = models.CharField(max_length=200, null=pode_null, blank=branco)

    semanas = models.CharField(max_length=200, null=False, blank=False, choices=SEMANAS)
    #projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="certificados_user", on_delete=models.CASCADE, null=True, blank=True)
    solicitante = models.ForeignKey(User, related_name="timesheet_user", on_delete=models.CASCADE, null=True, blank=True)
    # 0 - não submetida
    # 1 - submetida aguardando aprovação
    # 2 - submetida e aprovada
    # 3 - reprovada
    situacao = models.IntegerField(default=0)
    # submetida = models.BooleanField(default=False)
    # aprovada = models.BooleanField(default=False)
    # reprovada = models.BooleanField(default=False)

