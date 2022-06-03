import unreal 

@unreal.uclass()
class EditorUtils(unreal.EditorUtilityLibrary):
	pass

@unreal.uclass()
class EditorUtilsLib(unreal.BlueprintFunctionLibrary):
    @unreal.ufunction(params=[str], static=True, meta=dict(Category="Editor Utils lib"))
    def move_selected(dir):
        selected_assets = EditorUtils.get_selected_assets()
        if len(selected_assets) == 0:
            unreal.log_warning("No asset selected")
        for n, asset in enumerate(selected_assets):
            unreal.log("selected asset {}:".format(n+1))
            unreal.log(asset.get_full_name())
            unreal.log(asset.get_name())
            unreal.log(asset.get_path_name())
            unreal.log(asset.get_class().get_name())
            unreal.log(asset.get_class())
            unreal.log("##############################")
            prefix = ""
            # pattern matching (switch) introduced in python 3.10
            if isinstance(asset, unreal.EditorUtilityWidgetBlueprint):
                prefix = "UW"
            elif isinstance(asset, unreal.Blueprint):
                prefix = "BP"
            elif isinstance(asset, unreal.Material):
                prefix = "M"
            elif isinstance(asset, unreal.MaterialInstance):
                prefix = "MI"
            target_path_name = "/".join(("/Game", dir, "_".join((prefix, asset.get_name()))))
            unreal.EditorAssetLibrary.rename_asset(asset.get_path_name(), target_path_name)
    
    @unreal.ufunction(params=[int], static=True, meta=dict(Category="Editor Utils lib"))
    def create_blueprint(count):
        for i in range(count):
            # if we try to create an asset at a certain folder that doesn't exists
            # unreal will automatically catch that and create the folder structure
            bp_name = "MyPlayerController{}".format(i) 
            bp_path = "/Game/PlayerController"
            # assets are created through factories 
            factory = unreal.BlueprintFactory()
            # we need to set the parent in the factory 
            # note that also factory derives from object
            factory.set_editor_property("ParentClass", unreal.PlayerController)
            asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            asset = asset_tools.create_asset(bp_name, bp_path, None, factory)
            # much faster to change than in c++ no need to recompile anything :)
            unreal.EditorAssetLibrary.save_loaded_asset(asset)

unreal.log("Imported PyEditorUtils")