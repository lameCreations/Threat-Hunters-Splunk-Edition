# Define the starting label
label splunk_start:

    # Initialize variables
    $ s_query = ""
    $ correct_query = "index=_internal"
    $ result_data = [
        "08-17-2024 09:00:00.000 INFO  - Indexer starting up",
        "08-17-2024 09:01:45.000 INFO  - Connection established",
        "08-17-2024 09:02:30.000 WARN  - Delayed indexing detected",
        "08-17-2024 09:04:10.000 INFO  - Indexer running smoothly",
    ]
    $ error_message = ""

    # Display the initial screen
    show screen splunk_interface

    # Call the input screen
    call screen query_input

    # Check the query entered by the user
    if s_query.strip() == correct_query:
        $ error_message = ""
        # Call the results screen
        call screen results_display
    else:
        $ error_message = "Incorrect SPL Query. Please try again."
        # Retry input if the query was wrong
        call screen query_input

    return


# Screen for the main Splunk interface
screen splunk_interface():
    # Background for the Splunk-like interface
    window:
        style "default"
        background "splunk_bg.png"  # You would need a background image that looks like the Splunk interface
        has vbox

    frame:
        xalign 0.5
        yalign 0.1
        has hbox

        # Display the main Splunk search bar
        text "Search SPL:":
            style "default"
            align (0.0, 0.5)
        
        # Search input field
        input id "s_input" value VariableInputValue("s_query") allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|=><-_ ":
            style "input"
            align (0.0, 0.5)
        
        # Search button
        button:
            text "Search"
            action [Return()]

# Screen for SPL query input
screen query_input():
    modal True
    frame:
        style "input_frame"
        xalign 0.5
        yalign 0.4

        vbox:
            # Prompt the player to write the query
            text "Please write a Splunk Query to retrieve data from the _internal index":
                color "#000000"

            # Show any error message if the query was incorrect
            if error_message:
                text error_message:
                    color "#ff0000"
                    align (0.5, 0.5)

            # Show the input field and button again
            input id "s_input" value VariableInputValue("s_query") allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|=><-_ ":
                style "input"
                align (0.0, 0.5)
            
            button:
                text "Submit"
                action [Return()]

# Screen for displaying the query results
screen results_display():
    modal True
    frame:
        style "default_frame"
        xalign 0.5
        yalign 0.6

        vbox:
            text "Query Results:" style "header"

            viewport:
                draggable True
                mousewheel True

                vbox:
                    for line in result_data:
                        text line:
                            style "result_text"

# Styles for the text and input fields
style default:
    font "DejaVuSans.ttf"

style header is default:
    size 30
    color "#000000"
    bold True

style input_frame is default:
    background "#e1e1e1"
    padding (10, 10)  # Corrected padding to be a tuple
    xsize 400

style input is default:
    background "#ffffff"
    #color "#000000"
    xsize 400
    ysize 40
    font "DejaVuSans.ttf"

style default_frame is default:
    background "#e1e1e1"
    padding (10, 10)  # Corrected padding to be a tuple
    xsize 400

style result_text is default:
    color "#333333"
    size 15
    xsize 350
    line_spacing 3
