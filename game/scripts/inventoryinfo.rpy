label inventory_info:

    scene darkcyberbg

    menu:
        "What would you like to see within the Inventory Menu?"

        "Review the Inventory for the Scenario Data":
            n sensai "A wise choice to know your own network before proceeding"
            jump networkInventoryList

        "Learn about common systems in an inventory and what are common attacks against these devices":
           
            jump networkToolsTutorials

        "Return to Main Menu":
            jump mainMenu
            
    
    #call screen network_inventory

label networkInventoryList:
    scene networkinventorybg
    call screen network_inventory

label networkToolsTutorials:
    scene commonsystemsbg
    call screen common_system

screen network_inventory:
    modal True
    imagemap:
        ground "networkinventory.png"
        # SQL Server
        hotspot (708, 962, 550, 99) action Jump("inventory_info")


screen common_system:
    modal True   
    imagemap:
        ground "commonsystems.png"
        # SQL Server
        hotspot (125, 77, 211, 227) action Jump("sqldatabase_overview")
        # Domain Controllers
        hotspot (508, 76, 221, 223) action Jump("domaincontroller_overview")
        # Firewall
        hotspot (846, 85, 217, 215) action Jump("firewall_overview")
        # Web Server
        hotspot (1237, 85, 207, 214) action Jump("webserver_overview")
        # SCCM
        hotspot (1527, 90, 316, 194) action Jump("sccm_overview")
        # Exchange Server
        hotspot (87, 457, 271, 241) action Jump("exchange_overview")
        # BYOD
        hotspot (427, 460, 312, 233) action Jump("byod_overview")
        # Samba
        hotspot (836, 460, 230, 238) action Jump("samba_overview")
        #  Server
        hotspot (1183, 475, 310, 218) action Jump("server_overview")
        # Workstation
        hotspot (1563, 460, 243, 252) action Jump("workstation_overview")
        # Return to Title
        hotspot (236, 908, 548, 96) action Jump("inventoryTitle")
        # Return to Main Menu
        hotspot (1074, 904, 554, 106) action Jump("mainMenu")

label sqlServerOverview:
    scene darkcyberbg
    n sensai "We shall teach you the power of SQL"
    jump inventory_info

label domainControllersOverview:
    scene darkcyberbg
    n sensai "We shall teach you the power of Domain Controller"
    jump inventory_info

label firewallReview:
    scene darkcyberbg
    n sensai "We shall teach you the power of Firewall"
    jump inventory_info

label webServerOverview:
    scene darkcyberbg
    n sensai "Welcome to Web Server"
    n sensai "This product does a lot of things"
    jump inventory_info

label sccmOverview:
    scene darkcyberbg
    n sensai "So you want to learn about SCCM"
    n sensai "This is generic information"
    jump inventory_info 

label exchangeOverview:
    scene darkcyberbg
    n sensai "Exchange Server, you want to set up?"
    jump inventory_info

label byodOverview:
    scene darkcyberbg
    n sensai "BYOD you want to set up?"
    jump inventory_info

label sambaOverview:
    scene darkcyberbg
    n sensai "We shall teach you the power of Samba"
    jump inventory_info

label serverOverview:
    scene darkcyberbg
    n sensai "Welcome to Server"
    n sensai "This product does a lot of things"
    jump inventory_info

label workstationOverview:
    scene darkcyberbg
    n sensai "So you want to learn about workstation"
    n sensai "This is generic information"
    jump inventory_info 

label inventoryTitle:
    scene darkcyberbg
    n sensai "We'll go back to Inventory Title"
    jump inventory_info
