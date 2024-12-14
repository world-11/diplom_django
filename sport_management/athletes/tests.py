from django.test import TestCase, Client
from datetime import date
from models import *


class AthleteTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.athlete = Athlete.objects.create(name="Иван Иванов", age=25)
        self.competition = Competition.objects.create(title="Чемпионат мира", date=date.today())

    def test_athlete_creation(self):
        response = self.client.post('/create/', {'name': 'Петр Петров', 'age': 30})
        self.assertEqual(response.status_code, 302)
        new_athlete = Athlete.objects.last()
        self.assertEquals(new_athlete.name, 'Петр Петров')
        self.assertEquals(new_athlete.age, 30)

        '''
    def test_athlete_update(self):
        pk = self.athlete.pk
        response = self.client.post(f'/update/{pk}/', {'name': 'Сергей Сергеев', 'age': 28})
        updated_athlete = Athlete.objects.get(pk=pk)
        self.assertEqual(updated_athlete.name, "Сергей Сергеев")
        self.assertEqual(updated_athlete.age, 28)

    def test_athlete_deletion(self):
        pk = self.athlete.pk
        response = self.client.delete(f'/delete/{pk}')
        with self.assertRaises(Athlete.DoesNotExist):
            Athlete.objects.get(id=pk)

    def test_competition_creation(self):
        data = {
            'title': 'Кубок России',
            'date': date.today(),
            'participants': [self.athlete.id],
        }
        response = self.client.post("/competitions/create/", data=data)
        last_competition = Competition.objects.last()
        self.assertIn(last_competition.participants.first(), data['participants'])

    def test_participation_in_competition(self):
        participation = self.competition.participants.add(self.athlete)
        athlete = Athlete.objects.filter(competitions=self.competition).first()
        self.assertIsNotNone(athlete)

'''