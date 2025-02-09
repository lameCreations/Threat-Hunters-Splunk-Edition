label powershell_search:
    scene darkcyberbg
    show narrator sensai at left 
    

    "What would you like to search for?"
    python:
        pwshpovname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        pwshpovname = pwshpovname.strip()
        pwshinput_lower = pwshpovname.lower()
       
        del tempListOfPowershell[:]
        
        for nPowershell in listOfPowershell :
            if pwshpovname.lower() in nPowershell.about.lower() or pwshpovname.lower() in nPowershell.title.lower() :
                tempListOfPowershell.append(nPowershell)
      
    call screen powershell_results(tempListOfPowershell)

screen powershell_results(selectedYoutubeVideos):
    #window:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nPowershell in selectedYoutubeVideos :
                    textbutton nPowershell.title text_color "#000000" action [SetVariable("videoTitle", nPowershell.title),SetVariable("videoDescription", nPowershell.about), SetVariable("videoURL", nPowershell.url)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_powershell_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("powershell_search")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5

label all_powershell_videos:
    call screen all_powershell_results

screen all_powershell_results:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nPowershell in listOfPowershell :
                    textbutton nPowershell.title text_color "#000000" action [SetVariable("videoTitle", nPowershell.title),SetVariable("videoDescription", nPowershell.about), SetVariable("videoURL", nPowershell.url)]
                    
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_powershell_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("powershell_search")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5