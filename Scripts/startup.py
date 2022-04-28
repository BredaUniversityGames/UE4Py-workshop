import unreal 
import json
import datetime

config_path = unreal.Paths.project_dir() + 'user_config.json'
with open(config_path) as json_file:
    user_config = json.load(json_file)

now = datetime.datetime.now()
message = ["Good"]
if now.hour < 12:
    message.append("morning")
elif now.hour < 18:
    message.append("afternoon")
else:
    message.append("evening")

message.append(user_config["name"])
unreal.log(" ".join(message))