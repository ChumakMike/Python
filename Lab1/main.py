import api
from wateringPeriod import WateringPeriod

wp = WateringPeriod("uu", "23", "4", ["f", "d"])
wp1 = WateringPeriod("uu", "23", "4", ["f", "d"])
api.create(wp)
api.create(wp1)
api.save_session()
