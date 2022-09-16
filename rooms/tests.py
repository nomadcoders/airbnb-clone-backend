from rest_framework.test import APITestCase
from .models import Amenity, Room
from users.models import User


class TestAmenities(APITestCase):
    def setUp(self) -> None:
        Amenity.objects.create(
            name="Test Amenitiy",
            description="Test Description",
        )

    def test_get_amenities(self):

        response = self.client.get("/api/v1/rooms/amenities/")

        data = response.json()
        self.assertIs(
            type(data),
            list,
            "Should receive a list.",
        )
        self.assertEqual(
            data[0]["name"], "Test Amenitiy", "Oldest amenity should be there."
        )

    def test_create_amenity(self):

        new_amenity = {
            "name": "New Amenity",
            "description": "New Description",
        }

        response = self.client.post(
            "/api/v1/rooms/amenities/",
            data=new_amenity,
        )
        data = response.json()

        self.assertEqual(
            data["name"],
            new_amenity["name"],
        )
        self.assertEqual(
            data["description"],
            new_amenity["description"],
        )


class TestRooms(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            username="nomadcoders",
        )
        user.set_password("1234")
        user.save()
        self.client.login(
            username="nomadcoders",
            password="1234",
        )

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        print(response)
        pass
