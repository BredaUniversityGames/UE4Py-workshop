import unreal
import datetime
import random

unreal.log("It's {}".format(datetime.datetime.now()))
unreal.log("A dice roll: {}".format(random.randrange(1, 6)))