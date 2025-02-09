label memberVideoMenu:
    scene darkcyberbg
    show narrator sensai at left    
      
    jump all_member_videos

label memberVideoSearch:
    scene darkcyberbg
    show narrator sensai at left 
    

    "What would you like to search for?"
    python:
        memberpovname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        memberpovname = memberpovname.strip()
        memberinput_lower = memberpovname.lower()
       
        del tempListOfMember[:]
        
        for nMember in ListOfMember :
            if memberpovname.lower() in nMember.about.lower() or memberpovname.lower() in nMember.title.lower() :
                tempListOfMember.append(nMember)
      
    call screen member_results(tempListOfMember)

screen member_results(selectedYoutubeVideos):
    #window:
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nMember in selectedYoutubeVideos :
                    textbutton nMember.title text_color "#000000" action [SetVariable("videoTitle", nMember.title),SetVariable("videoDescription", nMember.about), SetVariable("videoURL", nMember.url)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_member_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("memberVideoSearch")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5

label all_member_videos:
    call screen all_member_results

screen all_member_results:
    
    hbox:
        viewport:
            scrollbars "vertical"
            xsize 1200
            ysize 600
            vbox:
                style_prefix "btnsdisplay"
                for nMember in ListOfMember :
                    textbutton nMember.title text_color "#000000" action [SetVariable("videoTitle", nMember.title),SetVariable("videoDescription", nMember.about), SetVariable("videoURL", nMember.url)]
                    #textbutton nMember.title text_color "#000000" action [SetVariable("videoTitle", nMember.title),SetVariable("videoDescription", nMember.about), SetVariable("videoURL", nMember.url),Function(renpy.notify, videoTitle)]
        vbox:
            text "{b}Selected Youtube Video Title:{/b} [videoTitle]"
            text " "
            text "{b}Video Description:{/b} [videoDescription]"
      
            style_prefix "btns"
            if videoURL.startswith("http"):
                textbutton "View Video" text_color "#ffffff" action OpenURL(videoURL) xalign 0.5
            text ""
            hbox:
                   
                textbutton "Show All" text_color "#ffffff" action Jump("all_member_videos")
                textbutton "Search Again" text_color "#ffffff" action Jump("memberVideoSearch")
            textbutton "Main Menu" text_color "#ffffff" action [SetVariable("videoTitle", "tbd"),SetVariable("videoDescription", "tbd"),SetVariable("videoURL", "tbd"),Jump("mainMenu")] xalign 0.5