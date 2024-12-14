
from django.urls import path
from .views import (
    AthleteList,
    AthleteCreate,
    AthleteUpdate,
    AthleteDelete,
    CompetitionList,
    CompetitionCreate,
    CompetitionUpdate,
    CompetitionDelete,
    athlete_competitions_view
)

urlpatterns = [
    # Маршруты для спортсменов
    path('', AthleteList.as_view(), name='athlete-list'),
    path('create/', AthleteCreate.as_view(), name='athlete-create'),
    path('<int:pk>/update/', AthleteUpdate.as_view(), name='athlete-update'),
    path('<int:pk>/delete/', AthleteDelete.as_view(), name='athlete-delete'),

    # Маршруты для соревнований
    path('competitions/', CompetitionList.as_view(), name='competition-list'),
    path('competitions/create/', CompetitionCreate.as_view(), name='competition-create'),
    path('competitions/<int:pk>/update/', CompetitionUpdate.as_view(), name='competition-update'),
    path('competitions/<int:pk>/delete/', CompetitionDelete.as_view(), name='competition-delete'),

    # Список спортсменов и их участие в соревнованиях
    path('athlete-competitions/', athlete_competitions_view, name='athlete-competitions'),
]
