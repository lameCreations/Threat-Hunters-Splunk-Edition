label devTable:
    scene darkcyberbg
    show narrator sensai at left 
    call screen youtube_results(listOfYoutube)


    "What would you like to search for?"
    python:
        povname = renpy.input("Enter Search Words (max 32 chars)", length=32)
        povname = povname.strip()
        input_lower = povname.lower()
        # Check if the input matches any string in the list
        #match_found = any(input_lower == word for word in listOfYoutube.about)

        del tempListOfYoutube[:]
        

        for nYoutube in listOfYoutube :
            if povname in nYoutube.about :
                tempListOfYoutube.append(nYoutube)
            #table_text += nYoutube.url + " " + nYoutube.title
            #table_text += f"{key}: {value}\n"
            #table_text += "\n"
        #return table_text


    #call screen table_screen
    call screen ask_for_query

screen youtube_results(selectedYoutubeVideos):
    #window:
    viewport:
        scrollbars "vertical"
        xsize 800
        ysize 600
        vbox:
            for nYoutube in listOfYoutube :
                textbutton nYoutube.title text_color "#ffffff" action OpenURL(nYoutube.url)

screen table_screen:
    vbox:
        textbutton "Back" action Return()  # Button to return to previous screen
        textbutton listOfYoutube[0].title  action OpenURL('https://youtu.be/QdM6JvnYu7g?si=XbRhiK4n4n-pg4Fz')  
        text "[display_table(listOfYoutube)]"  # Display table data
        #text "[display_table(csv_data)]"  # Display table data

screen ask_for_query:
    vbox:
        textbutton "Back" action Return()  # Button to return to previous screen
        textbutton listOfYoutube[0].title action OpenURL('https://youtu.be/QdM6JvnYu7g?si=XbRhiK4n4n-pg4Fz')  
        text "[display_table(tempListOfYoutube)]"  # Display table data
        #text "[display_table(csv_data)]"  # Display table data