define gui.input_text_color = "#FFFFFF"  # White color

define n = Character("Narrator", image="narrator")

default imageCounter = 0
default nextLabel = ""
default currentLabel = ""
default current_splunk_tuts_image = "splunk_meta_search/meta_sourcetypes_1.png"
default listOfMetadata_tuts = ["splunk_meta_search/meta_sourcetypes_1.png", "splunk_meta_search/meta_sourcetypes_2.png", "splunk_meta_search/meta_sourcetypes_3.png", "splunk_meta_search/meta_sourcetypes_4.png", "splunk_meta_search/meta_sourcetypes_5.png", "splunk_meta_search/meta_sourcetypes_6.png"]
default listofMetadata_host_tuts = ["splunk_meta_search/c1-meta-host-0.png","splunk_meta_search/c1-meta-host-1.png","splunk_meta_search/c1-meta-host-2.png"]
default listOfYoutube = []
default tempListOfYoutube = []

default listOfPowershell = []
default tempListOfPowershell = []

default listOfCribl = []
default tempListOfCribl = []

default ListOfMember = []
default tempListOfMember = []
default videoTitle="tbd"
default videoDescription="tbd"
default videoURL ="tbd"

default ListOfTools = []
default tempListOfTools = []

style btns_button:
    xysize (350, 50)
    background "button_idle.png"
    hover_background "button_idle.png"

style btns_button_text:
    xalign 0.5

style btnsdisplay_button:
    xysize (1150, 100)
    background "display_button_idle.png"
    hover_background "display_button_hover.png"

style btnsdisplay_button_text:
    xalign 0.5

# The game starts here.

# The game starts here.
define myPOV = ""
label start:

    call InitializeSplunkVideos from _call_InitializeSplunkVideos
    call InitializeCriblVideos from _call_InitializeCriblVideos
    call InitializePowerShellVideos from _call_InitializePowerShellVideos
    call InitializeMemberVideos from _call_InitializeMemberVideos
    call InitializeToolsVideos from _call_InitializeToolsVideos


    if not persistent.intro_shown:
        scene darkcyberbg
    
        show narrator sensai at left 

        n sensai "Welcome to this beginning tutorial on how to learn CyberSecurity Principles"
        n sensai "I am the Log Analyis Made Easy (L.A.M.E.) ninja sensai"
        n sensai "I have put this training together to cover many of the principles needed to succeed in the cyber security field"
        n sensai "The goal of this training is to make it available to anyone regardless of whether or not you have the infrastructure."
        n sensai "I plan to give you the tools to be able to do this at your own environment, but if you can't install the software, we will simulate it here in this training"
    
        $ persistent.intro_shown = True
    else:
        scene darkcyberbg
    
        show narrator sensai at left 
        # The text that appears when the player skips the introduction
        "Welcome back! Let's continue your journey."
        #jump splunk_start
   
    jump mainMenu

    n sensai "Well this concludes the sharing portion of this meeting" 

    # This ends the game.

    return

label mainMenu:
    call screen main_menu_selection

label ExitGame:
    $ renpy.quit()

screen main_menu_selection:
    modal True
    imagemap:
        ground "MainMenuGraphic.png"
        hotspot (209, 34, 296, 298) action Jump("powershellOverview")
        hotspot (582, 39, 308, 290) action Jump("networklogOverview")
        hotspot (959, 38, 317, 293) action Jump("hostlogOverview")
        hotspot (1346, 35, 300, 305) action Jump("security_tools")
        hotspot (179, 436, 334, 333) action Jump("trainingVideoMenu")
        hotspot (599, 432, 265, 338) action Jump("memberVideoMenu")
        hotspot (948, 432, 362, 344) action Jump("inventory_info")
        hotspot (1353, 440, 325, 344) action Jump("quickReference")
        hotspot (692, 945, 369, 65) action Jump("ExitGame")  