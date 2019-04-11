class WateringPeriod:
    def __init__(self, area_name, watering_time, watering_time_duration, days_of_week_arr, period_id=0):
        self.watering_time = watering_time
        self.period_id = period_id
        self.area_name = area_name
        self.watering_time_duration = watering_time_duration
        self.days_of_week_arr = days_of_week_arr

    def info(self):
        print("Area: {}".format(self.area_name))
        print("Watering duration: {} sec. (from: {})"
              .format(self.watering_time_duration, self.watering_time))
        for day in self.days_of_week_arr:
            print("Days of watering: " + day)

    def __dict__(self):
        return {"area_name": self.area_name,
                "watering_time": self.watering_time,
                "period_id": self.period_id,
                "watering_time_duration": self.watering_time_duration,
                "days_of_week_arr": self.days_of_week_arr}


def ob_from_dict(d):
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
