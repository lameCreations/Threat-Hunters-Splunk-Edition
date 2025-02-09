label splunk_search:
    scene darkcyberbg
    show narrator sensai at left 
    #call screen youtube_results(listOfYoutube)

    "What would you like to search for?"
    python:
        povname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        povname = povname.strip()
        input_lower = povname.lower()
       
        del tempListOfYoutube[:]
        
        for nYoutube in listOfYoutube :
            if povname.lower() in nYoutube.about.lower() or povname.lower() in nYoutube.title.lower() :
                tempListOfYoutube.append(nYoutube)
      
    call screen youtube_results(tempListOfYoutube)


python early:
    def GetInputValue(id):
        return renpy.get_widget(id).value

screen youtube_results(selectedYoutubeVideos):
    #window:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nYoutube in selectedYoutubeVideos :
                    textbutton nYoutube.title text_color "#000000" action [SetVariable("videoTitle", nYoutube.title),SetVariable("videoDescription", nYoutube.about), SetVariable("videoURL", nYoutube.url)]
        vbox:          

            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:                
               
                textbutton "Search Again" text_color "#ffffff" action Jump("splunk_search")
                textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5