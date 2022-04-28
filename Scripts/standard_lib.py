import unreal
import datetime
import random
import json

unreal.log("It's {}".format(datetime.datetime.now()))
unreal.log("A dice roll: {}".format(random.randrange(1, 6)))

user_config = {
  "name": "Bob",
  "screen_size": (1920, 1080),
  "is_active": True,   
}

unreal.log("The project is located at {}".format(unreal.Paths.project_dir()))
with open(unreal.Paths.project_dir()+'user_config.json', 'w') as f:
    json.dump(user_config, f)