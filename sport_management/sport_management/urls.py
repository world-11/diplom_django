"""
URL configuration for sport_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from athletes.views import (
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
    path('admin/', admin.site.urls),
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
