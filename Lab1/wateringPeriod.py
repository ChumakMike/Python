class WateringPeriod:
    """ Class of watering period information """
    def __init__(self, area_name, watering_time, watering_time_duration, days_of_week_arr, period_id=0):
        """Create object of WateringPeriod class

        >>> wp1 = WateringPeriod("TEST", 0, 0, ["Monday", "Tuesday"])
        >>> wp2 = WateringPeriod("TEST", 0, 0, ["Monday", "Tuesday"])
        >>> wp3 = WateringPeriod("TEST1", 0, 0, [])
        >>> wp1.__eq__(wp2)
        True
        >>> wp1.__eq__(wp3)
        False
        """
        self.watering_time = watering_time
        self.period_id = period_id
        self.area_name = area_name
        self.watering_time_duration = watering_time_duration
        self.days_of_week_arr = days_of_week_arr

    def info(self):
        """Prints information about watering period object.

        >>> wp = WateringPeriod("TEST", 0, 0, [])
        >>> wp.info()
        Area: TEST
        Watering duration: 0 sec. (from: 0)
        >>> wp1 = WateringPeriod("TEST", 0, 0, ["Friday", "Monday"])
        >>> wp1.info()
        Area: TEST
        Watering duration: 0 sec. (from: 0)
        (Friday)
        (Monday)
        """
        print("Area: {}".format(self.area_name))
        print("Watering duration: {} sec. (from: {})"
              .format(self.watering_time_duration, self.watering_time))
        for day in self.days_of_week_arr:
            print("(" + day + ")")

    def __dict__(self):
        """Convert WateringPeriod object to dict

        >>> wp = WateringPeriod("TEST", 0, 0, [])
        >>> wp.__dict__()
        {'area_name': 'TEST', 'watering_time': 0, 'period_id': 0, 'watering_time_duration': 0, 'days_of_week_arr': []}
        >>> wp = WateringPeriod("TEST", 0, 0, ["Thursday", "Friday"])
        >>> wp.__dict__()
        {'area_name': 'TEST', 'watering_time': 0, 'period_id': 0, 'watering_time_duration': 0, 'days_of_week_arr': ['Thursday', 'Friday']}
        """
        return {"area_name": self.area_name,
                "watering_time": self.watering_time,
                "period_id": self.period_id,
                "watering_time_duration": self.watering_time_duration,
                "days_of_week_arr": self.days_of_week_arr}

    def __eq__(self, other):
        """Compare objects of WateringPeriod class

        >>> wp1 = WateringPeriod("TEST", 0, 0, [])
        >>> wp2 = WateringPeriod("TEST", 0, 0, [])
        >>> wp3 = WateringPeriod("TEST1", 0, 0, [])
        >>> wp1.__eq__(wp2)
        True
        >>> wp1.__eq__(wp3)
        False
        """
        if self.area_name == other.area_name:
            if self.watering_time_duration == other.watering_time_duration:
                if self.watering_time == other.watering_time:
                    if self.days_of_week_arr == other.days_of_week_arr:
                        return True
        return False


def ob_from_dict(d):
    """Convert dict to WateringPeriod object

    >>> d1 = {"area_name": "TEST", "watering_time": 0, "period_id": 0, "watering_time_duration": 0, "days_of_week_arr": []}
    >>> wp1 = WateringPeriod("TEST", 0, 0, [])
    >>> wp1.__eq__(ob_from_dict(d1))
    True
    >>> d2 = {"area_name": "TEST", "watering_time": 0, "period_id": 0, "watering_time_duration": 0, "days_of_week_arr": ["Friday", "Thursday"]}
    >>> wp2 = WateringPeriod("TEST", 0, 0, ["Friday", "Thursday"])
    >>> wp2.__eq__(ob_from_dict(d2))
    True
    """
    return WateringPeriod(d.get('area_name'),
                          d.get('watering_time'),
                          d.get('watering_time_duration'),
                          d.get('days_of_week_arr'),
                          d.get('period_id'))


def list_from_dict(d_list):
    """Convert dict to list of WateringPeriod objects
    >>> d1 = [ {'area_name': "TEST", 'watering_time': 0, 'period_id': 0, 'watering_time_duration': 0, 'days_of_week_arr': []}]
    >>> list_from_dict(d1) == [WateringPeriod("TEST", 0, 0, [])]
    True
    """
    ob_list = list()
    for d in d_list:
        ob_list.append(ob_from_dict(d))
    return ob_list


# python -m doctest -v wateringPeriod.py
if __name__ == "__main__":
    import doctest
    doctest.testmod
