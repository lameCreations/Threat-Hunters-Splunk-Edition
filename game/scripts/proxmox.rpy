label proxmox:
  
    scene darkcyberbg
    
    menu:
        "Welcome to ProxMox, an open source (free) Virtualization Server. What would you like to do?"

        "What is ProxMox?":
            jump aboutProxmox        
   
        "Installation Videos for ProxMox":
            jump installProxmox
              
        
        "Back to Security Tools Menu":
            jump security_tools
        
        "Back to Main Menu":
            jump mainMenu

label aboutProxmox:
    scene darkcyberbg
    show narrator sensai at left 
    n sensai "Proxmox Virtual Environment is a complete, open-source server management platform for enterprise virtualization."
    n sensai "It tightly integrates the KVM hypervisor and Linux Containers (LXC), software-defined storage and networking functionality, on a single platform."
    n sensai "With the integrated web-based user interface you can manage VMs and containers, high availability for clusters, or the integrated disaster recovery tools with ease."
    n sensai "The enterprise-class features and a 100 percent software-based focus make Proxmox VE the perfect choice to virtualize your IT infrastructure,"
    n sensai "optimize existing resources, and increase efficiencies with minimal expense."
    n sensai "You can easily virtualize even the most demanding of Linux and Windows application workloads, and dynamically scale computing and storage as your needs grow, ensuring that your data center adjusts for future growth."
    jump proxmox

label installProxmox:
    menu:
        "What is ProxMox":
            $ renpy.run(OpenURL('https://youtu.be/GbOH7bX3uYI'))
        "Create Bootable CD":
            $ renpy.run(OpenURL('https://youtu.be/HJ0OTvSPfwQ'))
        "Upload ISO, Create VMs, and Clone VMs":
            $ renpy.run(OpenURL('https://youtu.be/yOd1Kx8P06c'))
        "ProxMox Main Menu":
            jump proxmox
        "Main Menu":
            jump mainMenu
