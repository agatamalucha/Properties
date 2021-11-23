from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.test import Client
from core import models
from home import views
from django.contrib.auth import get_user_model

HOME_URL = reverse("home:home")
DASHBOARD_URL = reverse("home:dashboard")
RESTAURANT_SEARCH_URL = reverse("home:restaurant-search")
SEARCH_NAME_URL = reverse("home:search-name")
SEARCH_CUISINE_URL = reverse("home:search-cuisine")
MY_RESTAURANTS_URL = reverse("home:my-restaurants")
MY_EVENTS_URL = reverse("home:my-events")


def sample_superuser():
    user = get_user_model().objects.create_superuser(
        username="superuser",
        email="superuser@gmail.com",
        password="test1234",
    )
    return user


def sample_restaurant():
    restaurant = models.RestaurantModel.objects.create(
        name="test",
        cuisine="test",
        rating=3,
        price_rating=3,
        longitude="123",
        latitude="123",
        image="test",
        review="test",
        day=3,
        budget=3,
        link="test",
    )

    return restaurant

def sample_restaurant_list_model():
    restaurant_list_model = models.RestaurantListModel.objects.create(
        title="test",
        address="test",
        rating=3.1,
        cuisine_1="test1",
        cuisine_2="test2",
        cuisine_3="test3",
        link="test",
    )

    return restaurant_list_model

def sample_poi():
    poi = models.PoiModel.objects.create(
        name="test",
        ticket_adult=3.1,
        ticket_child=3.1,
        longitude="test",
        latitude="test",
        image="test",
        day=2,
        budget=2,
        link="test",
    )
    return poi

def sample_acc():
    acc = models.AccommodationModel.objects.create(
        name="test",
        price=25.50,
        longitude="test",
        latitude="test",
        amenities= "test",
        image="test",
        day=2,
        budget=2,
        link="test",
    )
    return acc

def sample_carrental():
    car = models.CarRentalModel.objects.create(
        company="test",
        type="test",
        price=25.50,
        image="test",
        budget=2,
        link="test",
    )
    return car

def sample_event():
    event = models.EventModel.objects.create(
        name="test",
        date="2021-04-24",
        ticket_adult = 3.1,
        ticket_child = 3.1,
        longitude="test",
        latitude="test",
        image="test",
        day=2,
        budget=2,
        link="test",
    )
    return event

class GetRangeTests(TestCase):

    def test_range(self):
        r = views.get_range(2)
        self.assertEqual(r, range(0,2))

class HomeViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = sample_superuser()
        self.sample_restaurant=sample_restaurant()
        self.sample_acc = sample_acc()
        self.sample_carrental = sample_carrental()
        self.sample_event = sample_event()
        self.sample_restaurant_list_model=sample_restaurant_list_model()
        self.sample_poi = sample_poi()


    def test_retrieve_my_restaurants(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(MY_RESTAURANTS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-restaurants.html")
        self.assertEqual(len(response.context['restaurants']), 1)

    def test_retrive_my_events(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(MY_EVENTS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-events.html")
        self.assertEqual(len(response.context['cars']), 1)
        self.assertEqual(len(response.context['accommodation']), 1)
        self.assertEqual(len(response.context['events']), 1)
        self.assertEqual(len(response.context['pois']), 1)

    def test_build_home_view(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(HOME_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertEqual(len(response.context['cars']), 1)
        self.assertEqual(len(response.context['accommodation']), 1)
        self.assertEqual(len(response.context['events']), 1)
        self.assertEqual(len(response.context['pois']), 1)
        self.assertEqual(len(response.context['restaurants']), 1)
        self.assertEqual(response.context['budget'], 11)


    def test_dashboard(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(DASHBOARD_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")


    def test_restaurant_search(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(RESTAURANT_SEARCH_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant-search.html")
        self.assertEqual(len(response.context['restaurant_types']), 1)



    def test_retrieve_search_name(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(SEARCH_NAME_URL , {"query": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant-search.html")
        # print(str(response.context))
        self.assertEqual(len(response.context['queryset']), 1)


    def test_retrieve_search_cuisine(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(SEARCH_CUISINE_URL , {"query": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant-search.html")
        # print(str(response.context))
        self.assertEqual(len(response.context['queryset']), 1)





