import unreal 
import json

config_path = unreal.Paths.project_dir() + 'user_config.json'
with open(config_path) as json_file:
    user_config = json.load(json_file)
unreal.log("Hi {}!".format(user_config["name"]))