from cx_Freeze import setup, Executable
import os

path = "./gameSprites"
asset_list = os.listdir(path)
asset_list_complete = [os.path.join(path, gameSprites).replace("\\", "//") for gameSprites in asset_list]
print(asset_list_complete)

executables = [Executable("main.py")]
files = {"include_files": asset_list_complete, "packages": ["pygame"]}

setup(
    name="OtterRiver",
    version="1.0",
    description="OtterRiver app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)