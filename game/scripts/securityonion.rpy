label securityonion:
    scene darkcyberbg
    show narrator sensai at left 
    n sensai "We are going to cover the bare essentials of the Security Onion software suite"
    n sensai "Security Onion is a free and open platform built by defenders for defenders. It includes network visibility, host visibility, intrusion detection honeypots, log management, and case management."
    n sensai "For network visibility, we offer signature based detection via Suricata, rich protocol metadata and file extraction using your choice of either Zeek or Suricata, full packet capture via Stenographer, and file analysis via Strelka."
    n sensai "For host visibility, we offer the Elastic Agent which provides data collection, live queries via osquery, and centralized management using Elastic Fleet."
    n sensai "Intrusion detection honeypots based on OpenCanary can be added to your deployment for even more enterprise visibility."
    n sensai "All of these logs flow into the Elastic stack and we've built our own user interfaces for alerting, hunting, dashboards, case management, and grid management."
    n sensai "Security Onion and the tools and its integrated tools are all open to the public, written by members of the cyber security community. Source code is available in GitHub for review by those interested in understanding how the system works, behind the scenes."

    scene soalerts
    show narrator sensai at left 
    n sensai "Security Onion Console (SOC) includes an Alerts interface which gives you an overview of the alerts that Security Onion is generating. You can then quickly drill down into details, pivot to Hunt or the PCAP interface, and escalate alerts to Cases."

    scene sodashboards
    show narrator sensai at left 
    n sensai "Security Onion Console (SOC) includes a Dashboards interface which includes an entire set of pre-built dashboards for our standard data types."
    
    scene sohunt
    show narrator sensai at left 
    n sensai "Security Onion Console (SOC) includes a Hunt interface which is similar to our Dashboards interface but is tuned more for threat hunting."
    
    scene sopcap1
    show narrator sensai at left 
    n sensai "Security Onion Console (SOC) includes a PCAP interface which allows you to access your full packet capture that was written to disk by Stenographer."
    n sensai "In most cases, you’ll pivot to PCAP from a particular event in Alerts, Dashboards, or Hunt by choosing the PCAP action on the action menu."

    scene sopcap2
    show narrator sensai at left 
    n sensai "Security Onion will then locate the stream and render a high level overview of the packets."

    scene sopcap3
    show narrator sensai at left 
    n sensai "You can drill into individual rows to see the actual payload data. There are buttons at the top of the table that control what data is displayed in the individual rows. By disabling Show all packet data and HEX, we can get an ASCII transcript."

    scene sopcap4
    show narrator sensai at left 
    n sensai "You can select text with your mouse and then use the context menu to send that selected text to CyberChef, Google, or other destinations defined in the actions list."

    jump security_tools