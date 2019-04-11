import json
import wateringPeriod
from wateringPeriod import WateringPeriod

with open('data.json') as json_file:
    file_object = json.load(json_file)

scheduleList = wateringPeriod.list_from_dict(file_object.get("items"))
nextId = file_object.get("nextId")


def create(wp: WateringPeriod):
    global nextId
    wp.period_id = nextId
    nextId = nextId + 1
    scheduleList.append(wp)
    return wp.period_id


def read_all():
    return scheduleList


def read(period_id):
    try:
        return next(filter(lambda x: x.period_id == period_id, scheduleList))
    except StopIteration:
        raise Exception("there aren't such element")


def update_ob(to_upd, kwargs):
    if kwargs.get('area_name'):
        to_upd.area_name = kwargs.get('area_name')
    if kwargs.get('watering_time'):
        to_upd.watering_time = kwargs.get('watering_time')
    if kwargs.get('days_of_week_arr'):
        to_upd.days_of_week_arr = kwargs.get('days_of_week_arr')


def update(period_id, **kwargs):
    try:
        to_upd = next(filter(lambda x: x.period_id == period_id, scheduleList))
        update_ob(to_upd, kwargs)
        return to_upd
    except StopIteration:
        raise Exception("there aren't such element")


def delete(period_id):
    try:
        scheduleList.remove(next(filter(lambda x: x.period_id == period_id, scheduleList)))
    except StopIteration:
        raise Exception("there aren't such element")


def delete_all():
    scheduleList.clear()
    global nextId
    nextId = 0


def save_session():
    with open('data.json', 'w') as outfile:
        json.dump({"nextId": nextId,
                   "items": [ob.__dict__ for ob in scheduleList]}, outfile, indent=4)


