screen custom_input(prompt, result):
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text prompt
            input default "" length 20 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 " value VariableInputValue(result)
            textbutton "OK" action Return(VariableInputValue(result))

# Define the Ren'Py script

# Declare the Ren'Py script
label splunk_build_statistical_detection:
    "Welcome to Anomaly Detection."

    # Main menu
    menu:
        "Which Anomaly Detection Method Do You Want to Use?"
        "1) Time Based Anomaly Detection":
            jump time_based_anomaly
        "2) Percent Deviation Detection":
            jump percent_deviation_anomaly
        "3) Exit":
            "Goodbye."
            return

label time_based_anomaly:
    # Collect inputs for Time Based Anomaly Detection
    $ time_stats_index = renpy.input("What index contains your data?", default="")

    "You Entered [time_stats_index]"
    $ time_stats_sourcetype = renpy.input("What sourcetype do you want to use?")
    $ time_stats_filterData = renpy.input("Do you want to filter data from the base query? (true/false)")

    if time_stats_filterData.lower() == "true":
        $ time_stats_willInclude = renpy.input("Will you be including data? (true/false)")
        
        if time_stats_willInclude.lower() == "true":
            $ time_stats_includeField = renpy.input("What field will you be using in your include?")
            $ time_stats_commaListInclude = renpy.input("Provide comma-separated list of included values:")

        $ time_stats_willExclude = renpy.input("Will you be excluding data? (true/false)")
        
        if time_stats_willExclude.lower() == "true":
            $ time_stats_excludeField = renpy.input("What field will you be using in your exclude?")
            $ time_stats_commaListExclude = renpy.input("Provide comma-separated list of excluded values:")

    $ time_stats_anomalyFields = renpy.input("What fields should we baseline?")
    $ time_stats_numDaysBaseline = renpy.input("How many days do you want to baseline?")

    # Output result for Time Based Anomaly Detection
    "index=[time_stats_index] sourcetype=[time_stats_sourcetype] earliest=-[time_stats_numDaysBaseline]d | stats earliest(_time) as firstSeenTime by [time_stats_anomalyFields] | eval anomalyTime = now() - 86400 | where firstSeenTime > anomalyFields"

    # Return to main menu or end
    jump splunk_build_statistical_detection

label percent_deviation_anomaly:
    # Collect inputs for Percent Deviation Anomaly Detection
    $ percent_deviation_index = renpy.input("What index contains your data?")
    $ percent_deviation_sourcetype = renpy.input("What sourcetype do you want to use?")
    $ percent_deviation_filterData = renpy.input("Do you want to filter data from the base query? (true/false)")

    if percent_deviation_filterData.lower() == "true":
        $ percent_deviation_willInclude = renpy.input("Will you be including data? (true/false)")
        
        if percent_deviation_willInclude.lower() == "true":
            $ percent_deviation_includeField = renpy.input("What field will you be using in your include?")
            $ percent_deviation_commaListInclude = renpy.input("Provide comma-separated list of included values:")

        $ percent_deviation_willExclude = renpy.input("Will you be excluding data? (true/false)")
        
        if percent_deviation_willExclude.lower() == "true":
            $ percent_deviation_excludeField = renpy.input("What field will you be using in your exclude?")
            $ percent_deviation_commaListExclude = renpy.input("Provide comma-separated list of excluded values:")

    $ percent_deviation_anomalyFields = renpy.input("What fields should we baseline?")
    $ percent_deviation_numDaysBaseline = renpy.input("How many days do you want to baseline?")

    # Output result for Percent Deviation Anomaly Detection
    "index=[percent_deviation_index] sourcetype=[percent_deviation_sourcetype] earliest=-[percent_deviation_numDaysBaseline]d | stats earliest(_time) as firstSeenTime by [percent_deviation_anomalyFields] | eval anomalyTime = now() - 86400 | where firstSeenTime > anomalyFields"

    # Return to main menu or end
    jump splunk_build_statistical_detection
