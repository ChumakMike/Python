import json_model
import wateringPeriod
from wateringPeriod import WateringPeriod


class Storage:
    """ Class for data storage operations """
    def __init__(self, filename):
        """ 
        >>> Storage("./test_files/")
        >>> Storage ("data.json")
        """
        try:
            json_file = json_model.load_file(filename)
        except FileNotFoundError:
            json_file = json_model.write_empty_file(filename)
        self.file_object = json_model.load_dict(json_file)
        self.localScheduleList = wateringPeriod.list_from_dict(self.file_object.get("items"))
        self.nextId = self.file_object.get("nextId")

    def create(self, wp: WateringPeriod):
        """ Adds new object to local list

        #>>> wp = WateringPeriod("TestApi", 0, 0, [])
        #>>> create(wp) == get_nextid() - 1
        True
        #>>> create(wp) == get_nextid()
        False
        """
        wp.period_id = self.nextId
        self.nextId = self.nextId + 1
        self.localScheduleList.append(wp)
        return wp.period_id

    def read_all(self):
        return self.localScheduleList

    def read(self, period_id):
        try:
            return next(filter(lambda x: x.period_id == period_id, self.localScheduleList))
        except StopIteration:
            raise Exception("there aren't such element")

    def update_ob(self, to_upd, kwargs):
        if kwargs.get('area_name'):
            to_upd.area_name = kwargs.get('area_name')
        if kwargs.get('watering_time'):
            to_upd.watering_time = kwargs.get('watering_time')
        if kwargs.get('days_of_week_arr'):
            to_upd.days_of_week_arr = kwargs.get('days_of_week_arr')
            return to_upd.period_id

    def update(self, period_id, **kwargs):
        try:
            to_upd = next(filter(lambda x: x.period_id == period_id, self.localScheduleList))
            self.update_ob(to_upd, kwargs)
            return to_upd
        except StopIteration:
            raise Exception("there aren't such element")

    def delete(self, period_id):
        try:
            self.localScheduleList.remove(next(filter(lambda x: x.period_id == period_id, self.localScheduleList)))
        except StopIteration:
            raise Exception("there aren't such element")

    def delete_all(self):
        self.localScheduleList.clear()
        self.nextId = 0

    def save_session(self):
        json_model.write_file(self.filename, {"nextId": self.nextId,
                                              "items": [ob.__dict__() for ob in self.localScheduleList]})


# python -m doctest -v api.py
if __name__ == "__main__":
    import doctest
    doctest.testmod
