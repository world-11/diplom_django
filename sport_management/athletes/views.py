from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Athlete, Competition
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
import logging

logger = logging.getLogger(__name__)

# Главная страница (спортсмены)
class AthleteList(ListView):
    model = Athlete
    template_name = 'athlete_list.html'
    context_object_name = 'athletes'


class AthleteCreate(SuccessMessageMixin, CreateView):
    model = Athlete
    fields = ['name', 'age']
    success_url = reverse_lazy('athlete-list')
    success_message = "Спортсмен успешно создан!"

    def form_valid(self, form):
        # Получаем имя спортсмена из формы
        athlete_name = form.cleaned_data['name']
        # Запись в лог
        logger.info(f"Спортсмен {athlete_name} был успешно создан.")
        return super().form_valid(form)


class AthleteUpdate(SuccessMessageMixin, UpdateView):
    model = Athlete
    fields = ['name', 'age']
    success_url = reverse_lazy('athlete-list')
    success_message = "Спортсмен успешно обновлен!"

    def form_valid(self, form):
        # Получаем имя спортсмена из формы
        athlete_name = form.cleaned_data['name']
        logger.info(f"Спортсмен {athlete_name} был успешно обновлен.")
        return super().form_valid(form)


class AthleteDelete(SuccessMessageMixin, DeleteView):
    model = Athlete
    success_url = reverse_lazy('athlete-list')
    success_message = "Спортсмен удален."


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        logger.info(f"Спортсмен был успешно удален.")
        return super().delete(request, *args, **kwargs)


# Страница соревнований
class CompetitionList(ListView):
    model = Competition
    template_name = 'competition_list.html'
    context_object_name = 'competitions'


class CompetitionCreate(SuccessMessageMixin, CreateView):
    model = Competition
    fields = ['title', 'date', 'participants']
    success_url = reverse_lazy('competition-list')
    success_message = "Соревнование создано!"


class CompetitionUpdate(SuccessMessageMixin, UpdateView):
    model = Competition
    fields = ['title', 'date', 'participants']
    success_url = reverse_lazy('competition-list')
    success_message = "Соревнование обновлено!"


class CompetitionDelete(SuccessMessageMixin, DeleteView):
    model = Competition
    success_url = reverse_lazy('competition-list')
    success_message = "Соревнование удалено."
    logging.info(f'Соревнование удалено.')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


# Страница со списком спортсменов и их участием в соревнованиях
def athlete_competitions_view(request):
    athletes = Athlete.objects.all()
    competitions = Competition.objects.all()
    context = {'athletes': athletes, 'competitions': competitions}
    return render(request, 'athlete_competitions.html', context)

