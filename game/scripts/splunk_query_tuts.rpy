label splunk_query_tuts:
    $imageCounter = 0
    
    scene splunk_bg
    menu:
        "What would you like to do?" 
           
        "Learn What Data Is Available":
            jump splunk_tut_data_available
        "SPL Commands":
            jump splunk_tut_spl_menu       
        
        "Main Menu":
            jump mainMenu
        

label splunk_tut_data_available:
    show narrator sensai at left 
    menu:
        "What would you like to do?" 
           
        "Learn How to Query My Existing Data?":
            jump splunk_tut_data_available_walkthrough
        "Run Meta Command":
            jump splunk_tut_run_meta       
        
        "Main Splunk Tutorial Menu":
            jump splunk_query_tuts

label splunk_tut_spl_menu:
    show narrator sensai at left
    n sensai "I have not completed this yet"
    jump splunk_query_tuts

label splunk_tut_data_available_walkthrough:
    show narrator sensai at left
    n sensai "One day I will do this"
    jump splunk_query_tuts

label splunk_tut_run_meta:
    $ nextLabel = "splunk_tut_meta_hosts"
    $ currentLabel = "splunk_tut_run_meta"
    $ current_splunk_tuts_image = listOfMetadata_tuts[imageCounter]
    #$ current_splunk_tuts_image = "splunk_meta_search/meta_sourcetypes_1.png"

    show narrator sensai at left
    n sensai "We are going to run the meta command to pull back all sources"
    n sensai "| metadata index=botsv3 type=sourcetypes"
    
    call screen splunk_tuts_interface
    jump splunk_tut_meta_hosts

label splunk_tut_meta_hosts:
    $ currentLabel = "splunk_tut_meta_hosts"
    $ nextLabel = "mainMenu"
    n sensai "The '| metadata index=botsv3 type=sourcetypes' returns a list of all of your sourcetypes on your Splunk instance."
    n sensai "If you want to see all of the hosts sending logs to Splunk, use a similar command"
    n sensai " '| metadata index=botsv3 type=hosts' notice it is the same command but instead of using sources, we use the hosts"
    $ imageCounter=0
    $ current_splunk_tuts_image = listofMetadata_host_tuts[imageCounter]
    call screen splunk_tuts_interface

    n sensai "Welcome back from your ride"

    jump splunk_query_tuts

label addOne:
    if (currentLabel == "splunk_tut_run_meta"):
        $ array_length = len(listOfMetadata_tuts)
        if (imageCounter < array_length - 1):
            $ imageCounter += 1
            $ current_splunk_tuts_image = listOfMetadata_tuts[imageCounter]
            call screen splunk_tuts_interface
        else:
            jump expression nextLabel
    elif(currentLabel == "splunk_tut_meta_hosts"):
        $ array_length = len(listofMetadata_host_tuts)
        if (imageCounter < array_length - 1):
            $ imageCounter += 1
            $ current_splunk_tuts_image = listofMetadata_host_tuts[imageCounter]
            call screen splunk_tuts_interface
        else:
            jump expression nextLabel

screen splunk_tuts_interface:
    modal True
    imagemap:
        ground current_splunk_tuts_image
        hotspot (777, 919, 366, 75) action Jump("mainMenu")
        hotspot (1831, 267, 64, 41) action Jump("addOne")
   
    textbutton "Return" action Return():
        style "my_button_style"
        xpos 0.35 
        ypos 0.06
    textbutton "Next" action Jump("addOne"):
        style "my_button_style"
        xpos 0.55
        ypos 0.06