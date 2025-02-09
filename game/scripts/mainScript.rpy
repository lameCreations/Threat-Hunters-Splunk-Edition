# Define the variables and mission 1 setup
default score = 0
default suspicious_emails = ["urgent_finance_update@fake.com", "login_alert@secure-mail.com"]
default legit_emails = ["team_meeting@company.com", "birthday_invite@team.com"]

# Define variables for mission 2 setup
default nodes = {
    "192.168.1.10": {"destination": "10.0.0.5", "protocol": "HTTP", "volume": "500MB", "suspicious": False},
    "192.168.1.15": {"destination": "malicious.site.com", "protocol": "HTTPS", "volume": "1.5GB", "suspicious": True},
    "192.168.1.20": {"destination": "8.8.8.8", "protocol": "DNS", "volume": "50KB", "suspicious": False},
    "192.168.1.30": {"destination": "10.0.0.8", "protocol": "FTP", "volume": "2.0GB", "suspicious": True},
}
default analyzed_nodes = []


label mainGame:
    "hello World"
    jump mainGameStart

# Start the script
label mainGameStart:
    # Introduction to the mission
    scene bg_office
    #show SENTI normal at left
    show narrator sensai at left 
    "Welcome, Cadet! We have a new challenge for you."
    #SENTI "A potential phishing campaign is targeting employees of the Cyber Defense Academy."
    n sensai "A potential phishing campaign is targeting employees of the Cyber Defense Academy."
    n sensai "Your task is to identify suspicious emails from this log and escalate the threat to the security team."
    n sensai "Each correct identification earns you 10 points, but be careful! Incorrect actions will reduce your score."

    menu:
        "Start Mission 1: Phishing Expedition":
            jump phishing_mission

label phishing_mission:
    # Mission screen
    scene bg_computer
    n sensai "Here is the email log for today. Review each entry and decide if it's suspicious or legitimate."
    
    # Display the first email
    call review_email("urgent_finance_update@fake.com") from _call_review_email
    # Display the second email
    call review_email("team_meeting@company.com") from _call_review_email_1
    # Display the third email
    call review_email("login_alert@secure-mail.com") from _call_review_email_2
    # Display the fourth email
    call review_email("birthday_invite@team.com") from _call_review_email_3

    # Mission complete
    jump phishing_results

# Define a reusable email review block
label review_email(email):
    # Display the email
    n sensai "Email detected: [email]"
    menu:
        "Mark as suspicious":
            if email in suspicious_emails:
                $ score += 10
                n sensai "Good job! This email is indeed suspicious."
            else:
                $ score -= 5
                n sensai "Incorrect. This email is legitimate. Be more careful!"
        "Mark as legitimate":
            if email in legit_emails:
                $ score += 10
                n sensai "Correct! This email is legitimate."
            else:
                $ score -= 5
                n sensai "Oops, this email is actually suspicious. Check for phishing clues next time!"
    return

# Results screen
label phishing_results:
    scene bg_office
    n sensai "Mission complete! Let's review your performance."
    if score >= 30:
        n sensai "Great work, Cadet! You scored [score] points and successfully mitigated the phishing campaign."
        n sensai "Director Cross will be pleased with your effort."
    elif score >= 10:
        n sensai "Not bad, Cadet. You scored [score] points, but a few phishing emails slipped through. Stay sharp!"
    else:
        n sensai "You only scored [score] points. The campaign continues to spread. We'll need to train harder for next time."
    
    # End mission
    menu:
        "Return to the Academy":
            jump mission2start
#### Mission 2 Code ####

# Mission start
label mission2start:
    scene bg_office
    show narrator sensai at left 
    n sensai "Welcome back, Cadet! We've identified unusual network activity in the academy's systems."
    n sensai "Your task is to analyze the network map, investigate each IP node, and determine whether traffic is suspicious or legitimate."
    n sensai "Remember, suspicious traffic often involves unknown destinations, large data transfers, or uncommon protocols."

    menu:
        "Start Mission 2: Traffic Jam":
            jump traffic_jam_map

label traffic_jam_map:
    scene bg_network_map
    n sensai "This is the network map. Click on an IP address to analyze its traffic."

    # Display clickable nodes on the network map
    show screen network_map

    # Wait for all nodes to be analyzed
    while len(analyzed_nodes) < len(nodes):
        $ renpy.pause(1)

    jump traffic_results

# Define the screen for the network map
screen network_map:
    text "Network Map: Click an IP to investigate." xpos 0.5 ypos 0.1

    # IP nodes as buttons
    textbutton "192.168.1.10" action Call("review_node", "192.168.1.10") xpos 0.3 ypos 0.4
    textbutton "192.168.1.15" action Call("review_node", "192.168.1.15") xpos 0.5 ypos 0.4
    textbutton "192.168.1.20" action Call("review_node", "192.168.1.20") xpos 0.3 ypos 0.6
    textbutton "192.168.1.30" action Call("review_node", "192.168.1.30") xpos 0.5 ypos 0.6

# Analyze individual nodes
label review_node(ip):
    # Check if node has already been analyzed
    if ip in analyzed_nodes:
        n sensai "You've already analyzed this IP. Return to the map to investigate another node."
        return

    # Add the node to analyzed list
    $ analyzed_nodes.append(ip)

    # Display traffic details
    n sensai "Analyzing traffic from [ip]:"
    $ log = nodes[ip]
    n sensai "Destination: {log['destination']}\nProtocol: {log['protocol']}\nVolume: {log['volume']}"
    n sensai "Does this traffic look suspicious to you?"

    menu:
        "Mark as suspicious":
            if log["suspicious"]:
                $ score += 10
                SENTI "Correct! This traffic is suspicious and has been escalated."
            else:
                $ score -= 5
                SENTI "Incorrect. This traffic is legitimate."
        "Mark as legitimate":
            if not log["suspicious"]:
                $ score += 10
                SENTI "Correct! This traffic is legitimate."
            else:
                $ score -= 5
                SENTI "Incorrect. You missed a threat. This traffic is suspicious."

    # Return to the network map
    return

# Mission results screen
label traffic_results:
    scene bg_office
    n sensai "Mission complete! Let's review your performance."
    if score >= 30:
        n sensai "Excellent job, Cadet! You scored [score] points and successfully secured the network."
        n sensai "Your sharp instincts have earned you praise from Director Cross."
    elif score >= 10:
        n sensai "Good work, Cadet. You scored [score] points. However, a few threats slipped through. We need to stay vigilant."
    else:
        n sensai "You only scored [score] points. Unfortunately, the academy's network suffered due to missed threats. More training is needed."

    # Outcome influences the next mission
    if score >= 30:
        n sensai "Your performance has unlocked a bonus challenge in the next mission."
    else:
        n sensai "Prepare for tougher scenarios in the next mission."
    
    # End mission
    menu:
        "Return to the Academy":
            return
