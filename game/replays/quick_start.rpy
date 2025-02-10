default replays = {
    "Splunk SA": [
        {"label": "planning_best_practices", "image": "replays/ch1_planning_best_practices.png"},
        {"label": "install_splunk_enterprise", "image": "replays/ch1_installing_splunk.png"},
        {"label": "install_license_server", "image": "replays/ch1_installing_license_server.png"},
        {"label": "install_indexer", "image": "replays/ch1_installing_indexer.png"},
        {"label": "install_license_server", "image": "replays/ch1_installing_license_server.png"},
        {"label": "install_indexer", "image": "replays/ch1_installing_forwarder.png"},
        {"label": "install_indexer", "image": "replays/ch1_installing_deployment_server.png"},
        {"label": "install_indexer", "image": "replays/ch1_installing_management_console.png"},
        {"label": "install_indexer", "image": "replays/ch1_installing_shc.png"},   
        {"label": "install_indexer", "image": "replays/ch4_common_troubleshooting.png"},  
        {"label": "install_indexer", "image": "replays/ch5_upgrading_splunk_instances.png"},  
        {"label": "install_indexer", "image": "replays/ch5_common_conf.png"}, 
                     
    ],
    "Chapter 2": [
        {"label": "install_license_server", "image": "sensai.png"},
        {"label": "install_indexer", "image": "sensai.png"},
    ]
}

default current_chapter = "Splunk SA"

screen quick_start():
    
    tag menu
    modal True
    
    vbox:
        align (0.5, 0.1)
        text "Replay Gallery" size 40
        
    # Chapter Selection Buttons
    hbox:
        align (0.5, 0.2)
        spacing 20
        for chapter in replays:
            textbutton chapter action SetVariable("current_chapter", chapter)

    # Display Replay Thumbnails for the Selected Chapter
    #grid 2 3 len(replays[current_chapter]):
    grid 6 3:
        align (0.5, 0.6)
        spacing 10
        
        for replay in replays[current_chapter]:
            imagebutton:
                idle replay["image"]
                action Start(replay["label"])

    