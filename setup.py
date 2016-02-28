import cx_Freeze

executables = [cx_Freeze.Executable('game.py')]
cx_Freeze.setup(
    name="A Bit Racey",
    options={
        "build_exe":{"packages":["pygame"],"include_files":["images/racecar.png"]}
    },
    executables= executables
)