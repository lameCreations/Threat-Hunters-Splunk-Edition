label powershellOverview:
    scene powershellbg
    menu:
        "Welcome to PowerShell.  What would you like to do?"

        "What is PowerShell?":
            jump powershellDescription      
   
        "Get-Process Command":
            jump getprocessCmd
            

        "Get-Service":
            jump getserviceCmd
          

        "Get-Package":
            jump getpackage 
           
        "Get-Eventlog":
            jump geteventlog

        "Get User Information":
            jump getuserinfoCmd
        
        "Back to Main Menu":
            jump mainMenu

label getuserinfoCmd:
    scene psgetlocaluser
    show narrator sensai at left 
    n sensai "Understanding the users on your system is vital to know who may be accessing the sytem and what rights that individual may possess"
    n sensai "The cmdlet get-localuser is a simple tool to return all of the local users running on your Windows system"
    n sensai "If your machine is joined to a domain you can run the get-aduser command to pull back all users on the domain."
    jump powershellOverview

label geteventlog:
    scene psgeteventcode
    show narrator sensai at left 
    n sensai "Host logs are the lifeblood to any true hunting activity for bad on your system.  The host logs hold a wealth of knowledge to know what is happening on your system."
    n sensai "The ability to quickly review your logs is important to being able to detect malicious activity from false positives."
    n sensai "The cmdlet get-eventlog is a simple tool to return all of the logs on your Windows system"

    scene psgeteventcodeoutputgridview
    n sensai "Another tool that will make searching for your logs a lot easier is the | output-gridview command"
    n sensai "This tool gives a gui sorting and filtering interface to searching your logs"
    n sensai "To bring up this option just put a | output-gridview after your get-eventcode cmdlet like what I have done in the black box pointed to by the green arrow"
    jump powershellOverview

label getpackage:
    scene psgetpackage
    show narrator sensai at left 
    n sensai "Understanding the software running on a system is important to know what vulnerabiliteis may exist on a system"
    n sensai "You can also use it to detect if your selected security tools are installed on the system"
    n sensai "The cmdlet get-package is a simple tool to return all of the software running on your Windows system"
    jump powershellOverview

label getprocessCmd:
    scene psgetprocess
    show narrator sensai at left 
    n sensai "Understanding what is running on your systems is a valuable tool to being able to detect what should and what should not be running on your system"
    n sensai "The cmdlet get-process is a simple tool to return all of the processes running on your Windows system"
    jump powershellOverview

label getserviceCmd:
    scene psgetservice
    show narrator sensai at left 
    n sensai "Understanding what is running on your systems is a valuable tool to being able to detect what should and what should not be running on your system"
    n sensai "The cmdlet get-service is a simple tool to return all of the services running on your Windows system"
    jump powershellOverview

label powershellDescription:
    scene powershellbg
    show narrator sensai at left 
    n sensai "Powershell is an invaluable tool that is freely available to anyone using windows"
    n sensai "Powershell is a Windows equivalent tool to Bash on a Linux system"
    n sensai "Powershell provides a command line interface to run system diagnostics pull logs and gain information about your system in a scriptable format "
    n sensai "This is not going to cover everything you need to know about Powershell but we’re going to dip into some cool features that you can use to enhance your security knowledge of your system"

    jump powershellOverview


