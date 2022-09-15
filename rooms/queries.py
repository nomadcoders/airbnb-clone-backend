from . import models


def get_all_rooms():
    return models.Room.objects.all()
