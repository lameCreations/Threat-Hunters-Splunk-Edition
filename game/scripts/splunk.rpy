label splunk:
    scene darkcyberbg
    n sensai "Welcome to the world of Splunk"
    n sensai "You may be wondering what Splunk is, or you may already have a knowledge of the tool and would better like to learn how to use the tool"
    n sensai "I will provide you an overview of the technology,"
    n sensai "minimum information to set it up in a home lab, "    
    n sensai "instructions on how to set up a more complicated network"
    n sensai "instructions on how to do day to day searches"
    #scene darkcyberbg

    call screen splunkOverview

screen splunkOverview:
    modal True
    imagemap:
        ground "splunkMenu.png"
        hotspot (92, 62, 237, 240) action Jump("splunkHelpGuide")
        hotspot (539, 49, 258, 275) action Jump("splunkHomeNetwork")
        hotspot (953, 59, 247, 253) action Jump("splunkCorporateNetwork")
        hotspot (69, 379, 391, 204) action Jump("splunkSPL")
        hotspot (76, 624, 553, 309) action Jump("splunkEnterpriseSecurity")
        hotspot (791, 609, 356, 328) action Jump("splunkMLTK")
        hotspot (1310, 621, 534, 307) action Jump("splunkSoar")
        hotspot (181, 504, 360, 72) action Jump("mainMenu")
        hotspot (1399, 513, 362, 77) action Jump("security_tools")

label splunkSoar:
    scene darkcyberbg
    n sensai "I shall teach you the power of SOAR"
    menu:
        "Welcome to Splunk SOAR.  What would you like to do?"

        "What is Splunk SOAR?":
            jump splunkSoarExplained        
   
        "Watch Youtube Videos on Splunk SOAR":
            $ renpy.run(OpenURL('https://youtube.com/playlist?list=PLFF93FRoUwXH_7yitxQiSUhJlZE7Ybmfu&si=WhwHyWmGlzhxpZLD'))
            

        "How to install an Splunk SOAR":
            $ renpy.run(OpenURL('https://youtu.be/xGiLTayok6c'))   
        
        "Back to Splunk Menu":
            jump splunk

  
    jump splunkEnterpriseSecurity

label splunkSoarExplained:
    scene darkcyberbg
    n sensai "Splunk SOAR is designed to integrate and enhance your security operations seamlessly. It orchestrates your security stack by connecting with 300+ third-party tools and supporting 2,800+ automated actions."
    n sensai "This ensures that you can streamline complex workflows across various teams and tools without the need to massively overhaul your existing security stack."
    n sensai "Splunk SOAR is a force multiplier"
    n sensai "Splunk SOAR can streamline your response and automation processes by consolidating alerts and data from the various tools in your environment, ensuring timely and prioritized responses."
    n sensai "Respond with Speed and Accuracy"
    n sensai "Splunk SOAR empowers users to easily automate security tasks with playbooks that can be customized to fit your needs." 
    n sensai "Splunk SOAR features a wide variety of prebuilt playbooks, which leverage the MITRE ATT&CK and D3FEND frameworks, are all aligned to foundational SOC tasks, and help ensure you can automate everything from small steps to end-to-end use cases."
    n sensai "Main Dashboard"
    n sensai "Splunk SOAR’s Main Dashboard provides an overview of all your data and activity, notable events, playbooks, connections with other security tools, workloads, ROI, and so much more."
    n sensai "Apps"
    n sensai "Splunk SOAR apps are the integration points between Splunk SOAR and other security technologies. Through apps, Splunk SOAR directs your other security tools to perform actions, such as direct VirusTotal to check file reputation or Cisco Firewall to block an IP. "
    n sensai "Splunk SOAR’s app model supports integration with over 300 tools and over 2800 different actions. "
    n sensai "All Splunk SOAR apps are available on www.splunkbase.splunk.com"

    n sensai "Playbooks"
    n sensai "Splunk SOAR playbooks automate security and IT actions at machine speed. Playbooks execute a sequence of actions across your tools in seconds, vs hours or more if you perform them manually. "
    n sensai "Splunk SOAR comes with 100 pre-made playbooks out of the box, so you can start automating security tasks right away."
    n sensai "Splunk SOAR’s visual playbook editor makes it easier than ever to create, edit, implement and scale automated playbooks to help your business eliminate security analyst grunt work."

    n sensai "Case Management"
    n sensai "Case management functionality is built into Splunk SOAR."
    n sensai "Using workbooks, you can codify your standard operating procedures into reusable templates."
    n sensai "Splunk SOAR supports custom and industry standard workbooks such as the NIST-800 template for incident response."
    n sensai "You can divide tasks into phases, assign tasks to team members, and document your work."

    n sensai "Mobile"
    n sensai "Splunk SOAR’s orchestration, automation, response, collaboration, and case management capabilities are also available from your mobile device."

    jump splunk

label splunkMLTK:
    scene darkcyberbg
    n sensai "We shall teach you the power of MLTK"
    n sensai "The Splunk Machine Learning Toolkit acts like an extension to the Splunk platform and includes machine learning Search Processing Language (SPL) search commands, macros, and visualizations."
    n sensai "On top of the platform extensions meant for machine learning, MLTK has guided modeling dashboards called Assistants. Assistants walk you through the process of performing particular analytics."
    n sensai "Types of machine learning"
    n sensai "Machine learning is a process for generalizing from examples. You can use these generalizations, typically called models, to perform a variety of tasks, such as predicting the value of a field, forecasting future values, identifying patterns in data, and detecting anomalies from new data."
    n sensai "Without data and correct examples, it is difficult for machine learning to work at all."
    n sensai "The machine learning process starts with a question. You might ask one of these questions:"
    n sensai "Am I being hacked?"
    n sensai "How hot are the servers?"
    n sensai "How many visits to my site do I expect in the next hour?"
    n sensai "What is the price range of houses in a particular neighborhood?"
    n sensai "There are different types of machine learning, including:"
    n sensai "Regression"
    n sensai "Regression modeling predicts a number from a variety of contributing factors. Regression is a predictive analytic. For example, you might have utilization metrics on a machine, such as CPU percentage and amount of disk reads and writes."
    n sensai "You can use regression modeling to predict the amount of power that that machine is likely to draw both now and in the future."
    n sensai "Classification"
    n sensai "Classification modeling predicts a category or a class from a number of contributing factors. Classification is a predictive analytic."
    n sensai "For example, you might have data on user behavior on a website or within a software product. You can use classification modeling to predict whether that customer is going to churn."
    n sensai "Forecasting"
    n sensai "Forecasting is a predictive analytic that predicts the future of a single value moving through time. Forecasting looks at past measurements for a single value, like profit per day or CPU usage per minute, to predict future values."
    n sensai "For example, you might have sales results by quarter for the past 5 years. Use forecast modeling to predict sales for the upcoming quarter."
    n sensai "Clustering"
    n sensai "Clustering groups similar points of data together. For example, you might want to group customers together based on their buying behaviors, such as how much they tend to spend or how many items they buy at one time. Use cluster modeling to group together the features you specify."
    n sensai "Anomaly detection"
    n sensai "Anomaly detection finds outliers in your data by computing an expectation based on one of the machine learning types, comparing it with reality, and triggering an alert when the discrepancies between the two values is large."

    jump splunk

label splunkSPL:
    scene darkcyberbg
    n sensai "We shall teach you the power of SPL"

    menu:
        "Welcome to Splunk SPL Tutorial"
        "Watch youtube playlists on how to search with SPL":
            $ renpy.run(OpenURL('https://www.youtube.com/playlist?list=PLFF93FRoUwXF-iLxJw6JxVQC473PqkZzB'))
        "Watch youtube playlists on common SPL commands":
            $ renpy.run(OpenURL('https://www.youtube.com/playlist?list=PLFF93FRoUwXEGaNAmZTc9pek9WzUq6unp'))
            
        "Watch youtube playlists on how to create dashboards":
            $ renpy.run(OpenURL('https://www.youtube.com/playlist?list=PLFF93FRoUwXEuaoqQR2Ghe57vmO8IG4yh'))


    jump splunk

label splunkEnterpriseSecurity:
    scene darkcyberbg
    menu:
        "Welcome to Splunk Enterprise Security.  What would you like to do?"

        "What is Enterprise Security?":
            $ renpy.run(OpenURL('https://youtu.be/-v7hVZpAqrw?si=4R-AH6ICTTGzUOPR'))         
   
        "Watch Youtube Videos on Enterprise Security":
            $ renpy.run(OpenURL('https://youtube.com/playlist?list=PLFF93FRoUwXHM36f_pIHw7pgOmSuV2r21&si=eCPZMxCjYSnPboxQ'))
            

        "How to setup an Enterprise Security Server":
            $ renpy.run(OpenURL('https://youtu.be/Iol1CHyv23A?si=T39u25RFKncG8l03'))   
          

        "How to install Enterprise Security":
            $ renpy.run(OpenURL('https://youtu.be/QdM6JvnYu7g?si=XbRhiK4n4n-pg4Fz'))  
           
       
        "Back to Splunk Menu":
            jump splunk

    #n sensai "Welcome to Enterprise Security Overview"
    #n sensai "This product does a lot of things"
    jump splunkEnterpriseSecurity

screen splunkEnterpriseSecurityOverview:
    modal True


label splunkHelpGuide:
    scene darkcyberbg
    n sensai "So you want to learn about Splunk"
    n sensai "Splunk is a leading data analytics platform that enables organizations to collect, index, search, and analyze large volumes of machine-generated data from various sources in real-time." 
    n sensai "It provides valuable insights into operational performance, security threats, and compliance issues, helping organizations to improve their cybersecurity posture."
    n sensai "Key Features:"
    n sensai "Data Aggregation: Splunk collects data from diverse sources, including servers, applications, network devices, and security tools, aggregating it into a centralized platform for analysis."
    n sensai "Real-time Monitoring: Splunk allows organizations to monitor their IT infrastructure and security environment in real-time, enabling rapid detection and response to cyber threats."
    n sensai "Search and Investigation: With its powerful search capabilities, Splunk enables users to quickly search, correlate, and analyze data to identify security incidents, anomalies, and trends."
    n sensai "Advanced Analytics: Splunk offers advanced analytics features, including machine learning and statistical analysis, to identify patterns and predict future security threats."
    n sensai "Custom Dashboards and Reports: Splunk allows organizations to create custom dashboards and reports to visualize data, track key performance indicators, and generate actionable insights for cybersecurity teams and executive leadership."
    n sensai "Integration with Security Tools: Splunk integrates with a wide range of security tools and technologies,"
    n sensai "including SIEM solutions, endpoint detection and response (EDR) platforms, threat intelligence feeds, and security orchestration automation and response (SOAR) systems, enhancing visibility and orchestration across the cybersecurity ecosystem."
    n sensai "Benefits:"
    n sensai "Improved Threat Detection and Response:"
    n sensai "By aggregating and analyzing data from across the IT environment, Splunk helps organizations to detect and respond to security threats more effectively, reducing the time to detect and mitigate cyber attacks."
    n sensai "Enhanced Visibility and Compliance: Splunk provides comprehensive visibility into security events, user activities, and compliance-related data, helping organizations to meet regulatory requirements and industry standards."
    n sensai "Operational Efficiency: Splunk automates data collection, analysis, and reporting processes, streamlining security operations and enabling cybersecurity teams to focus on high-priority tasks."
    n sensai "Proactive Security Monitoring: With its real-time monitoring capabilities and predictive analytics, Splunk enables organizations to proactively identify and mitigate security risks before they escalate into major incidents."
    n sensai "Data-driven Decision Making: Splunk empowers organizations to make data-driven decisions by providing actionable insights and intelligence based on analysis of large datasets, enabling better risk management and strategic planning."
    n sensai "Overall, Splunk is a powerful tool for improving cybersecurity by providing real-time visibility, advanced analytics, and actionable insights into security threats and vulnerabilities across the organization's IT infrastructure. "
    n sensai "By leveraging Splunk's capabilities, organizations can strengthen their security posture, enhance threat detection and response capabilities, and mitigate cyber risks effectively."
    
    
    
    jump splunk 

label splunkHomeNetwork:
    scene darkcyberbg
    n sensai "Home Network you want to set up?"
    jump splunk

label splunkCorporateNetwork:
    scene darkcyberbg
    n sensai "Corporate Network you want to set up?"
    jump splunk



