init python:
    class powershell_video(object):
        def __init__(self, url, title, about):
            self.title = title
            self.url = url
            self.about = about

label InitializePowerShellVideos:
    default pvideo1 = powershell_video("https://youtu.be/OaYYcm2Vgz4","Microsoft PowerShell For Beginners | Viewing Results Using Out-Gridview","PowerShell Out-Gridview cmdlet provides a user the ability to sort and filter the results in an easy to use gui.  This video demonstrates how to use this powerful cmdlet.")
    $ listOfPowershell.append(pvideo1)
    default pvideo2 = powershell_video("https://youtu.be/x2ugNlDfI24","Microsoft PowerShell For Beginners | Using Passwords in Your Scripts and How to Protect the Password","A beginner tutorial on how to use Microsoft PowerShell and how to use passwords in your script without having the password be available in plain text.")
    $ listOfPowershell.append(pvideo2)
    default pvideo3 = powershell_video("https://youtu.be/zlcY-5FvaN0","Microsoft PowerShell For Beginners | Filtering Sorting and Viewing Windows EventLogs","A beginner tutorial on how to use Microsoft PowerShell and how to retrieve Windows EventLogs.  When piped to the out-gridview you can sort filter and view logs in a close to SIEM like view.")
    $ listOfPowershell.append(pvideo3)
    default pvideo4 = powershell_video("https://youtu.be/nubRKc-geIo","Manipulating Time Values Within PowerShell","This tutorial will demo how to use and manipulate time string within PowerShell")
    $ listOfPowershell.append(pvideo4)
    default pvideo5 = powershell_video("https://youtu.be/X2VgHs0Emvs","Math Functions Within PowerShell","PowerShell natively handles many Math Functions.  This video will show you some of the math functions available within PowerShell")
    $ listOfPowershell.append(pvideo5)
    default pvideo6 = powershell_video("https://youtu.be/Da5ix_taCgc","Arrays and PowerShell","Arrays are an integral part of data manipulation.  This video will cover how many of the ways that Arrays can be used in Powershell.")
    $ listOfPowershell.append(pvideo6)
    default pvideo7 = powershell_video("https://youtu.be/EA7qHheXCBw","PowerShell and How to Manipulate Strings","PowerShell provides lots of methods for manipulating strings.  This tutorial will attempt to provide instruction on how to use them.")
    $ listOfPowershell.append(pvideo7)
    default pvideo8 = powershell_video("https://youtu.be/JavUl0kDfJA","Powershell How to Work with Variables and Power Shell Objects","Variables and PowerShell objects are the building blocks of Powershell and they are just as important if not more important than the cmdlets that are provided natively in powershell.  This video will demonstrate how to create variables and find the properties and methods of an object.")
    $ listOfPowershell.append(pvideo8)


    default pvideo9 = powershell_video("https://youtu.be/D2UtBLsx5Wo","PowerShell and the Get-Alias Cmdlet","If you are struggling to understand peoples online queries and get-alias may be a great tool to unlocking the mysteries of their script.  People often shorthand their scripts using aliases.  Get-Alias will allow you to interpret the shorthand commands and leverage the Get-help command to better understand the script.")
    $ listOfPowershell.append(pvideo9)
    default pvideo10 = powershell_video("https://youtu.be/nJxunAQFA8M","Using Powershell to Extract Fields from Windows Event Logs","A problem was raised on how to pull usernames and times out of logon events in Windows Event Security Logs with Powershell.  This video provides a step by step process of how a PowerShell script was created that helped achieve this goal.")
    $ listOfPowershell.append(pvideo10)
    default pvideo11 = powershell_video("https://youtu.be/DGk2MCWmFGY","PowerShell and How To Get Help on How To Use Any Cmdlet","PowerShell has a cmdlet Get-Help that will provide you all of the documentation for using that cmdlet.  It is also a great tool for learning what cmdlets you have on your system.  This video should help you understand how to leverage get-help to improve your abilities as a PowerShell user.")
    $ listOfPowershell.append(pvideo11)
    default pvideo12 = powershell_video("https://youtu.be/u6rWLk7wvRw","Creating a Domain Controller Using Powershell Scripting","Powershell scripts are the key to automation.  Using scripts allows for quickly setting up infrastructure and also building test environments.  This video will show case many different things that can be set up with Powershell.")
    $ listOfPowershell.append(pvideo12)
    default pvideo13 = powershell_video("https://youtu.be/FvHvqxLl4vU","Powershell on Linux?  Why","Powershell is a great tool to have in your log analysis tool box.  Powershell provides an object oriented approach to handling information on Linux and can provide powerful analysis tools.  This video aims to show some capabilities that makes PowerShell a useful tool on a Linux system.")
    $ listOfPowershell.append(pvideo13)
    default pvideo14 = powershell_video("https://youtu.be/bk0c3DBpwDM","PowerShell Functions and Examples","This tutorial will demonstrate why Functions are used in PowerShell and how to create them.  Parameter passing and returning values will be explained.")
    $ listOfPowershell.append(pvideo14)
    default pvideo15 = powershell_video("https://youtu.be/gBG0SeWc4PU","PowerShell Looping Examples","Powershell uses Do while and Do Until and foreach and for loops.  This tutorial will demonstrate how to use each of those loops in PowerShell.")
    $ listOfPowershell.append(pvideo15)
    default pvideo16 = powershell_video("https://youtu.be/63T1urviuyI","PowerShell If - ElseIf - Else and Switch Statements","This powershell tutorial will walk you through different logic control statements to allow powershell to take different actions depending on different situations.")
    $ listOfPowershell.append(pvideo16)
    default pvideo17 = powershell_video("https://youtu.be/iK2jfHwq628","How to Write Conditional Statements in PowerShell","PowerShell lets you evaluate conditions using equals and not equals and greater than and less than and contains and like and matches and other conditional statements.  This video will demo how to use these commands in powershell.")
    $ listOfPowershell.append(pvideo17)

