label cribl_search:
    scene darkcyberbg
    show narrator sensai at left
    
    "What would you like to search for?"
    python:
        criblpovname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        criblpovname = criblpovname.strip()
        criblinput_lower = criblpovname.lower()
       
        del tempListOfCribl[:]
        
        for nCribl in listOfCribl :
            if criblpovname.lower() in nCribl.about.lower() or criblpovname.lower() in nCribl.title.lower() :
                tempListOfCribl.append(nCribl)
      
    call screen cribl_results(tempListOfCribl)

screen cribl_results(selectedYoutubeVideos):
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
               
                for nCribl in selectedYoutubeVideos :
                    textbutton nCribl.title text_color "#000000" action [SetVariable("videoTitle", nCribl.title),SetVariable("videoDescription", nCribl.about), SetVariable("videoURL", nCribl.url)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_cribl_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("cribl_search")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5

label all_cribl_videos:
    call screen all_cribl_results

screen all_cribl_results:
    
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nCribl in listOfCribl :
                    textbutton nCribl.title text_color "#000000" action [SetVariable("videoTitle", nCribl.title),SetVariable("videoDescription", nCribl.about), SetVariable("videoURL", nCribl.url)]
                   
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_cribl_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("cribl_search")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5