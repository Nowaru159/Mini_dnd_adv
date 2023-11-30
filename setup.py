from cx_Freeze import setup, Executable

setup(
    name="mini_adv_dnd",
    version="1.0",
    description="laugh and play",
    executables=[Executable("mini_dnd_adv.py")],
)
