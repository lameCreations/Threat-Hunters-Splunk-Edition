label toolsVideoMenu:
    scene darkcyberbg
    show narrator sensai at left    
      
    jump all_tool_videos

label toolVideoSearch:
    scene darkcyberbg
    show narrator sensai at left 
    

    "What would you like to search for?"
    python:
        toolpovname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        toolpovname = toolpovname.strip()
        toolinput_lower = toolpovname.lower()
       
        del tempListOfTools[:]
        
        for nTools in ListOfTools :
            if toolpovname.lower() in nTools.about.lower() or toolpovname.lower() in nTools.title.lower() :
                tempListOfTools.append(nTools)
      
    call screen tool_results(tempListOfTools)

screen tool_results(selectedYoutubeVideos):
    #window:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nTools in selectedYoutubeVideos :
                    textbutton nTools.title text_color "#000000" action [SetVariable("videoTitle", nTools.title),SetVariable("videoDescription", nTools.about), SetVariable("videoURL", nTools.url)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_tool_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("toolVideoSearch")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5

label all_tool_videos:
    call screen all_tool_results

screen all_tool_results:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nTools in ListOfTools :
                    textbutton nTools.title text_color "#000000" action [SetVariable("videoTitle", nTools.title),SetVariable("videoDescription", nTools.about), SetVariable("videoURL", nTools.url)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_tool_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("toolVideoSearch")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5
