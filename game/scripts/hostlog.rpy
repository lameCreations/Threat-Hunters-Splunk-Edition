label hostlogOverview:
    scene darkcyberbg
    show narrator sensai at left 

    n sensai "Host logs are an invaluable resource for gathering data about your systems."
    n sensai "Logs are generated for all types of events on your system.  The host logs are one of the best ways of detecting bad in your network"
    n sensai "These logs are valuable to you as the detection team, but they are also valuable to the bad guy."
    n sensai "The bad guy wants to be able to purge or modify your host logs to avoid being able to identify their actions"
    n sensai "There are numerous types of host logs."
    n sensai "Windows Operating System will create host logs"
    n sensai "Many of the applications on your machine will also create host logs"
    n sensai "For the purpose of this training, we are going to focus on Operating System logs and only the most common of them"
    
    scene systemSecurityEvent
    show narrator sensai at left 
    n sensai "The Security Eventlogs may contain the most valuable logs for a Cyber Analyst."
    n sensai "These logs as they are aptly named, are focused on security events."
    n sensai "The above chart outlines some of the most imporant logs that are found in the security logs."
    n sensai "Eventcode 4624 and 4625 are your logs of choice for looking for authentication (login) actions.  Including brute forcing of passwords"
    n sensai "EventCode 4720 and 4722 relate to the creation and activation of user accounts.  Often to maintain persistence in a system, the attacker will attempt to create an account on the system"
    n sensai "EventCode 4728 and 4732 are similar to 4720 and 4722 but in this case the user is being added to groups that may give them elevated privileges."
    n sensai "EventCode 4688 can be noisy, but it does alert on the creation of a new process on the system.  Often the adversary will install and run software / processes on the compromised system."
    n sensai "EventCode 1102 is the log that indicates that other logs are being erased.  As mentioned earlier, an adversary wants to cover their actions so they may resort to trying to hide their actions by deleting the logs"

    scene systemWinEvent
    show narrator sensai at left 
    n sensai "The System Eventlogs are logs related to the Windows system and changes to the way the sytem is configured"
    n sensai "The above chart outlines some of the most imporant logs that are found in the system logs."
    n sensai "EventCode 7045 is the alert that lets you know that new services have been installed on the system.  New services are often installed as a system is compromised"
    n sensai "EventCode 7030 shows that an interactive service has been changed from its default nature.  This may be a sign that an adversary is attempting to use a known service in a different way than intended to gain access to the system"
    n sensai "EventCode 1056 the ability to pivot and move to another machine is a tactic used by adversaries.  Remote Desktop Protocol (RDP) is a commonly used protocol for remote accessing other windows systems"

    scene systemMiscLog
    show narrator sensai at left 
    n sensai "We will now present additional Eventlogs that may be useful"
    n sensai "The above chart outlines some of the most imporant logs that are found in the other logs. If you are not utilziing some of the software, you will not have these event types."
    n sensai "If you are using the Windows Firewall, EventCode 2003 will let you know if the firewall has been disabled.  Disabling the firewall will leave the Windows system susceptible to many types of attacks."
    n sensai "Applocker EventCode 8003 and 8004 relates to AppLocker.  Applocker provides the capability to prevent Windows machines from running anythign but allow listed software"
    n sensai "If you are using Windows Defender Antivirus, you will have Eventcode 1116 and 1117 that can tell you if Windows Defender is blocking malicious software from being run."
    
    jump mainMenu

#    image systemWinEvent = "systemeventlogs.png"
#image systemSecurityEvent = "securityeventlogs.png"
#image systemMiscLog = "miscellaneousEventLogs.png"