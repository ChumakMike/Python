class WateringPeriod:
    def __init__(self, area_name, watering_time, watering_time_duration, days_of_week_arr, period_id=0):
        self.watering_time = watering_time
        self.period_id = period_id
        self.area_name = area_name
        self.watering_time_duration = watering_time_duration
        self.days_of_week_arr = days_of_week_arr

    def info(self):
        """
           Prints information about watering period object.
        """
        print("Area: {}".format(self.area_name))
        print("Watering duration: {} sec. (from: {})"
              .format(self.watering_time_duration, self.watering_time))
        for day in self.days_of_week_arr:
            print("Days of watering: " + day)

    def __dict__(self):
        """
        Convert WateringPeriod object to dict

        >>> wp = WateringPeriod("TEST", 0, 0, [])
        >>> wp.__dict__
        {"area_name": "TEST",
         "watering_time": 0,
         "period_id": 0,
         "watering_time_duration": 0,
         "days_of_week_arr": []}
        """
        return {"area_name": self.area_name,
                "watering_time": self.watering_time,
                "period_id": self.period_id,
                "watering_time_duration": self.watering_time_duration,
                "days_of_week_arr": self.days_of_week_arr}

    def __eq__(self, other):
        """
            Compare objects of WateringPeriod

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
    """
    Convert WateringPeriod object to dict

    >>> d = {"area_name": "TEST", "watering_time": 0, "period_id": 0, "watering_time_duration": 0, "days_of_week_arr": []}
    >>> wp1 = WateringPeriod("TEST", 0, 0, [])
    >>> wp1.__eq__(ob_from_dict(d))
    True
    """
    return WateringPeriod(d.get('area_name'),
                          d.get('watering_time'),
                          d.get('watering_time_duration'),
                          d.get('days_of_week_arr'),
                          d.get('period_id'))


def list_from_dict(d_list):
    ob_list = list()
    for d in d_list:
        ob_list.append(ob_from_dict(d))
    return ob_list


if __name__ == "__main__":
    import doctest
    doctest.testmod