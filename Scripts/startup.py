import unreal 
import json
import datetime

config_path = unreal.Paths.project_dir() + 'user_config.json'
with open(config_path) as json_file:
    user_config = json.load(json_file)

@unreal.uclass()
class WelcomeLibrary(unreal.BlueprintFunctionLibrary):
    # pure function = no exec pin
    @unreal.ufunction(ret=str, static=True, pure=True, meta=dict(Category="Welcome Python Lib"))
    def get_part_of_day():
        now = datetime.datetime.now()
        if now.hour < 12:
            return "morning"
        elif now.hour < 18:
            return "afternoon"
        else:
            return "evening"

    @unreal.ufunction(ret=str, static=True, pure=True, meta=dict(Category="Welcome Python Lib"))
    def get_user_name():
        return user_config["name"]
    
    @unreal.ufunction(params=[str], static=True, meta=dict(Category="Welcome Python Lib"))
    def set_user_name(name):
        user_config["name"] = name
        unreal.log("Set user name: " + name)
    
    @unreal.ufunction(ret=str, static=True, pure=True, meta=dict(Category="Welcome Python Lib"))
    def get_welcome_message():
        message = [
            "Good",
            WelcomeLibrary.get_part_of_day(),
            WelcomeLibrary.get_user_name(),
            ]
        
        return " ".join(message)

    @unreal.ufunction(static=True, meta=dict(Category="Welcome Python Lib"))
    def log_welcome_message():
        unreal.log(WelcomeLibrary.get_welcome_message())

    @unreal.ufunction(static=True, meta=dict(Category="Welcome Python Lib"))
    def save_user_config():
        with open(config_path, 'w') as f:
            json.dump(user_config, f)

## open a widget from python 
## careful with the path, if wrong will crash at startup
widget = unreal.EditorAssetLibrary.load_asset("/Game/Utils/UW_WelcomeWidget")
unreal.EditorUtilitySubsystem().spawn_and_register_tab(widget)