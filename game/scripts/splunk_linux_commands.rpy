label splunk_linux_commands:
    scene splunk_commands
    call screen splunk_linux_commands_screen

screen splunk_linux_commands_screen:
    modal True
    imagemap:
        ground "splunk_linux_commands.png"
        hotspot (777, 919, 366, 75) action Jump("mainMenu")
        