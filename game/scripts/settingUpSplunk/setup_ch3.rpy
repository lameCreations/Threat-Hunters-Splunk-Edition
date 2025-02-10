label install_splunk_enterprise:
    scene bg_server_room  # Assuming you have a server room background image
    #show screen terminal  # If you have a custom screen for CLI simulation

    n sensai "Next, we'll set up our Splunk environment by installing Splunk Enterprise. This is the main GUI for managing Splunk, and we'll repeat this process across our architecture."

    n sensai "We're using Splunk version 9.3.0, the latest at the time of writing. We'll download the tarball for Linux since clustering isn't supported on macOS or Windows."

    n sensai "First, you'll need to download the installation package from Splunk's website. Here's the URL we'll use:"
    n sensai "https://www.splunk.com/en_us/download/splunk-enterprise.html?locale=en_us"
    n sensai "You'll need a Splunk account, which is free, just provide a username and email."

    n sensai "When downloading, I recommend using the WGET method for servers without a GUI:"
    n sensai "Click on 'Copy WGET Link' to get the download command. Paste this into each server's CLI for efficient downloads."

    n sensai "If you encounter an error, you might need to install wget. The command could look like this:"
    n sensai "sudo apt-get update && sudo apt-get install wget"

    n sensai "Once downloaded, let's move to installation. First, create a dedicated Splunk user for security:"
    n sensai "sudo adduser splunk"
    n sensai "Set a password and leave other settings blank."

    n sensai "Extract the tar file:"
    n sensai "Navigate to where you downloaded it, then use:"
    n sensai "sudo tar -xvzf splunk-9.3.0-XXXXXX-Linux-x86_64.tgz -C /opt"
    n sensai "Replace 'XXXXXX' with the actual version code from your download."

    n sensai "Change permissions to avoid running Splunk as root:"
    n sensai "sudo chown -R splunk:splunk /opt/splunk"

    n sensai "Start Splunk for the first time, switching to the Splunk user:"
    n sensai "su - splunk"
    n sensai "/opt/splunk/bin/splunk start --accept-license"
    n sensai "You'll need to accept the EULA and set up your initial admin credentials."

    n sensai "To ensure Splunk starts on boot:"
    n sensai "sudo /opt/splunk/bin/splunk enable boot-start -user splunk"

    n sensai "Now, access the Splunk Web Interface by pointing your browser to your server's IP with port 8000."
    n sensai "If you forget your server's IP, use:"
    n sensai "ip addr show"

    n sensai "Remember, this installation will be repeated for each node in our Splunk architecture. Now, let's configure our License Server."

    jump install_license_server

label install_license_server:
    scene bg_control_panel  # Assuming you have a control panel background
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n sensai "Alright, now let's configure the license server. In my setup, the Management Console and License Server share the same host."

    n sensai "Installing Splunk on this host follows the same steps we just went through. Now, let's turn it into a license server."

    n sensai "Navigate to Settings > Licensing in the Splunk interface:"
    n sensai "By default, it's a standalone license. To make it a server, click 'Add License' and upload your license file."

    n sensai "If you don't have a license yet, you can add it later. But for now, let's verify our setup:"
    n sensai "Go back to Settings > Licensing to confirm everything's in order."

    n sensai "Your Splunk instance is now a license server, ready for the rest of your architecture build-out."

    jump setup_license_server

label setup_license_server:
    # Here you would define the next steps or interactive elements for the setup process
    n sensai "With the general concept of setting up a Splunk System, let's move on to configuring an indexer. This is where your logs will be stored and searchable."

    jump install_indexer
    return

label install_indexer:
    scene bg_server_room  # Assuming you have a server room background image
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n sensai "Setting up an indexer follows the same initial steps as installing Splunk Enterprise. Here's what to do next:"

    n sensai "Log into the Splunk web interface and go to Settings > Forwarding and Receiving."

    n sensai "Since we're setting up an indexer, we need it to receive data. Click 'Configure Receiving', then hit the 'New Receiving Port' button in the top right."

    n sensai "Enter `9997` and save it. This port will listen for incoming log data."

    n sensai "You'll need to repeat this for all your indexers, ensuring they're all set to listen on port 9997."

    n sensai "Now, let's configure the license for each indexer. Without a valid license, you'll face violations, and eventually, you won't be able to search your data."

    n sensai "Go to Settings > Licensing on each indexer. If they're already peers to the license server, you're good. But if not, here's how to make them peers:"

    n sensai "Click on 'Change to Peer' under Licensing. If the button isn't there, they might already be peers."

    n sensai "Select the option to 'Designate a different Splunk instance as the manager license server'. Enter the license server's IP followed by :8089 in the 'Manage license server URI' field."

    n sensai "Save your settings, then restart each indexer. Navigate to Settings > Server Controls and click 'Restart Splunk'."

    n sensai "After restarting, check the status. Go to Settings > Licensing to ensure all indexers are correctly licensed and ready to receive data."

    n sensai "With these steps, your indexers are now configured to index your logs. Next, we'll combine these into an indexer cluster for better performance and redundancy."

    jump setup_indexer

label setup_indexer:
    # Here you would define the next steps or interactive elements for setting up the cluster
    n sensai  "Now that we've got our indexers set up, let's cluster them for better performance and redundancy. Here's where the master node comes into play."

    jump install_indexer_cluster
    return

label install_indexer_cluster:
    scene bg_control_panel  # Assuming you have a control panel background image
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n sensai "We have three indexers at 192.168.1.181, .182, and .183, all listening on port 9997. Let's designate 192.168.1.184 as our master node."

    n sensai "First, set up the master node. Go to Settings > Indexer Clustering and click 'Enable Indexer Clustering'."

    n sensai "Select 'Manager Node'. Don't configure this as a peer or search head. Set your replication and search factors; for three indexers, the default values should work."

    n sensai "You can choose to use a cluster master key for added security. Enter a cluster label and set a password, then click 'Next' and 'Restart' to finalize."

    n sensai "After the master node is set up, let's add our peer nodes. On each indexer, go to Settings > Indexer Clustering again."

    n sensai "Choose 'Peer Node' and point each to the master node at 192.168.1.184. Here's how you do that:"

    n sensai "Specify the manager node's IP and port. Use HTTP or HTTPS based on your configuration. Set a unique replication port for each, like 8080 for one, then 8081 for the next, and so on."

    n sensai "If you used a cluster key, input it. Then enable the peer node and restart each indexer after configuration."

    n sensai "To recap, for each indexer:"
    n sensai "- Enable clustering, select Peer Node, point to the master node."
    n sensai "- Set a unique replication port."
    n sensai "- Enter the cluster key if you used one."
    n sensai "- Enable the peer node and restart."

    n sensai "Once all indexers are restarted, check back on the master node. Go to Indexer Clustering to see if your peers are listed."

    n sensai "It might take a few minutes for the nodes to sync and replicate. But once it's done, you'll see each indexer's details, confirming your cluster is operational."

    n sensai "The beauty here is that once configured, the manager node takes over. You don't need to manage the indexers manually anymore."

    n sensai "With our indexer cluster now set up, we're ready to move on to configuring our search capabilities."

    jump setup_indexer_cluster

label setup_indexer_cluster:
    # Here you would define the next steps or interactive elements for setting up search head clusters
    n sensai "With our indexer cluster now up and running, we need to ensure the manager node's internal logs are being sent to these indexers for analysis and storage."

    jump install_forwarding_logs
    return

label install_forwarding_logs:
    scene bg_control_panel  # Assuming you have a control panel background image
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n sensai "Let's configure log forwarding on the manager node. Navigate to the Forwarding and Receiving settings."

    n sensai "Click 'Add New' to configure forwarding for each indexer in our cluster. Here's how we set it up:"

    n sensai "For Indexer 1, enter `192.168.1.181:9997`."
    n sensai "For Indexer 2, enter `192.168.1.182:9997`."
    n sensai "And for Indexer 3, enter `192.168.1.183:9997`."

    n sensai "Make sure to use port `9997` for all of them. Save these settings once you've added each entry."

    n sensai "After saving, double-check that all settings are correct. If there's an issue, correct it now."

    n sensai "Now, let's verify that the logs are being forwarded using some SPL commands. First, set your time range to the last 30 seconds to check for recent logs:"

    n sensai "Use this command in the Splunk search bar:"
    n sensai "`index=_internal earliest=-30s`"

    n sensai "Then, to get a count by host, extend it like this:"
    n sensai "`index=_internal earliest=-30s | stats count by host`"

    n sensai "Run this search to see if logs from the manager node are being sent to the indexers. Look for data indicating transmission to our indexers."

    n sensai "Finally, check where the data is actually stored:"
    n sensai "`index=_internal earliest=-30s | stats count by host`"
    n sensai "You should see the logs on the indexers, not on the manager node itself."

    n sensai "By following these steps, we've ensured that the manager node's internal logs are being forwarded to our indexer cluster, making them searchable and stored safely across our system."

    n sensai "Now that our logs are forwarding correctly, let's move on to setting up the search capabilities of our Splunk environment."

    jump setup_forwarding_logs

label setup_forwarding_logs:
    # Here you would define the next steps or interactive elements for setting up search head clusters
    n sensai "Now that we've managed to forward logs to our indexers, let's focus on distributing apps from the manager node to our indexer cluster."

    jump install_push_apps_to_indexers
    return

label install_push_apps_to_indexers:
    scene bg_control_panel  # Assuming you have a control panel background image
    #show screen splunk_cli  # If you have a custom screen for CLI simulation

    n sensai "To push apps to your indexer cluster, you'll work from the manager node. Let's dive in:"

    n sensai "First, access the manager node and navigate to the app management directory at `/opt/splunk/etc`."

    n sensai "You'll see `manager_apps` and `master_apps`. Use `manager_apps` for adding apps now. It's the current standard."

    n sensai "To add apps, you'll place them directly into the `manager_apps` directory. Think of it like placing apps in `deployment_apps` on a deployment server, but for indexers."

    n sensai "For any specific settings like SSL or data size limits, configure them in the relevant .conf files. For SSL, that would be `web.conf`, and for data size, `indexes.conf`."

    n sensai "Here's the key difference with the manager node: it uses a push mechanism. After placing your apps into `manager_apps`, you must actively push them to the indexers."

    n sensai "This means, unlike with a deployment server, where apps are pulled by clients, here you're pushing from the manager node to ensure the apps are deployed to all indexers."

    n sensai "By doing this, you centralize app management and ensure your entire indexer cluster stays updated and consistent."

    n sensai "Now that we've set up app distribution, let's move on to configuring our search environment."

    jump setup_push_apps_to_indexers

label setup_push_apps_to_indexers:
    # Here you would define the next steps or interactive elements for setting up search head clusters
    n sensai "Now that our apps are distributed, we'll deploy configuration changes to our indexer cluster using the master node's web GUI."

    jump deploy_config_bundle
    return

label deploy_config_bundle:
    scene bg_control_panel  # Assuming you have a control panel background image
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n sensai "First, log into your Splunk manager node and go to Settings > Indexer Clustering."

    n sensai "Once there, you'll see various actions. Click on 'Edit' then 'Configuration Bundle Actions'."

    n sensai "Choose 'Validate' to check for configuration errors. Remember, this isn't perfect; you should do your own checks as well."

    n sensai "After validating, click 'Check' to review. If everything's good, go ahead and 'Restart' to prep for changes."

    n sensai "Then, hit 'Push' to send the bundle to your indexers. If there's nothing new, nothing will be pushed, but this ensures your latest configs are live."

    n sensai "The master node will now restart each indexer one by one, keeping at least one online to avoid data loss. Keep an eye on the process."

    n sensai "If the new config causes issues, don't worry. You have the option to 'Rollback'. This reverts everything to how it was before your changes."

    n sensai "By following these steps, you'll deploy your configurations safely and efficiently, with the master node ensuring smooth operation throughout."

    n sensai "With our configurations deployed, let's now set up our search heads to utilize this data."

    jump install_config_bundle

label install_config_bundle:
    # Here you would define the next steps or interactive elements for setting up search head clusters
    n "Now that our configurations are deployed, let's look at maintaining balance in our indexer cluster through rebalancing."

    jump setup_rebalance_indexes
    return

label setup_rebalance_indexes:
    scene bg_control_panel  # Assuming you have a control panel background image
    #show screen splunk_gui  # If you have a custom screen for GUI simulation

    n "Rebalancing indexes in Splunk helps keep data evenly spread across your cluster, which is vital for performance."

    n "Here's why you'd want to rebalance: after updates or changes, data distribution might become uneven, impacting efficiency."

    n "To rebalance, go to Settings > Indexer Clustering in the Splunk GUI. Click 'Edit' then 'Data Rebalance'."

    n "You'll see options here for setting parameters. Let's go through them:"

    n "Set a 'Threshold' for how evenly you want the data distributed. A value like 0.9 means data can vary by up to 10% from the average."

    n "Then, there's 'Max Runtime'. This limits how long rebalancing takes, to avoid excessive downtime."

    n "Decide if you want to rebalance all indexes or just some, and whether to keep them searchable during the process."

    n "Once you've set your parameters, hit 'Start' to begin rebalancing. This will redistribute data to balance your indexers."

    n "A few best practices: do this during low-use times like off-peak hours or weekends if you've got large data sets to move."

    n "And always monitor the process. You want to make sure it finishes successfully and your indexers are back in balance."

    n "By managing data distribution this way, you keep your Splunk environment running smoothly and reliably."

    n "Now, let's move on to setting up our search capabilities with a search head cluster."

    jump install_rebalance_indexes

label install_rebalance_indexes:
    # Here you would define the next steps or interactive elements for setting up search head clusters
   
    n sensai "Now that our indexers are rebalanced we will discuss setting up distributed searching."

    jump setup_distributed_search
    return

label setup_distributed_search:
    scene bg_classroom # or any appropriate background for the scene
    
    n "Now, let's dive into setting up Distributed Search Peers in Splunk. This is crucial for when your Search Head needs to communicate with multiple indexers."
    
    n "For each indexer that your Search Head might need to search, you'll need to configure it as a search peer. Here's how you do it:"
    
    n "First, navigate to 'Settings' and then to 'Distributed Search' in your Splunk interface."
    
    n "You'll see an option to '+ Add new' in the 'Search Peers' section. Click there to start adding peers."
    
    n "Now, you'll need to input the following details for each peer:"
    
    n "Peer URI: This is where you enter the indexer's address. It should look something like 'https://<search_head_IP>:8089'."
    
    n "Remote Username: Here, you put in the username of the admin account on the Splunk Enterprise you're connecting to."
    
    n "Remote Password: And finally, the password for that admin account."
    
    n "Remember, every detail must be correct to ensure seamless communication between your Search Head and the indexers."
    
    n "Once you've added all necessary peers, you'll be ready to perform searches across multiple indexers. This is the foundation of a powerful Splunk setup."
    
    n "Are you ready to see this in action? Let's move to the next section where we'll practice setting up these peers and running some queries across them."

    # Transition to the next part of the training/book
    jump install_distributed_search


label install_distributed_search:
    # Here you would define what happens next in the story or training scenario
    n sensai "Now that our indexers are set up as distributed search, we will discuss the other options in the manager node"

    jump setup_master_node_other_options
    return

label setup_master_node_other_options:
    scene bg_control_panel  # Assuming you have a control panel background image

    n sensai "As we delve deeper into the art of data management, let's turn our attention to the Master Node GUI. This is where you wield control over your indexer cluster like a master craftsman."

    n sensai "Under the 'Edit' button on the Indexer Clustering Main Page, you'll find several options to refine your cluster's configuration. "

    n sensai "First, consider the 'Node Type'. You can transform a Splunk instance into a manager node, a peer node for joining an indexer cluster, or a search head node. But remember, once set, these roles are usually set in stone."

    n sensai "Now, let's talk about protecting and managing your data with 'Manager Node Configuration'. Here's where you adjust the Replication Factor (RF) and Search Factor (SF):"

    n sensai "- Search Factor (SF) is about redundancy for searchable data. It's like having multiple copies of a book in different libraries. If one library burns down, your knowledge isn't lost."

    n sensai "- **Replication Factor (RF)**, on the other hand, ensures your raw data is safe. Think of it as multiple backups of a manuscript before it's published. If one draft is destroyed, you have others to fall back on."

    n sensai "The key difference? SF keeps data searchable, RF keeps data safe before it's even searchable. Increasing these factors makes your data more resilient but remember, more copies mean more storage space!"

    n sensai "Security is paramount. Change the 'Security Key' to guard against unauthorized nodes joining your cluster. Without this key, your cluster could be vulnerable."

    n sensai "For those managing multiple clusters, the 'Cluster Label' is your friend. It's like naming your pets so you know which one is which in a busy household. Use it for unique identification, easier management, and precise deployment."

    n sensai "Remember our chat on 'Configuration Bundle Actions'? That's where you push apps to your indexers, ensuring everyone's on the same page."

    n sensai "'Data Rebalance' - a topic we've covered before, it's essential to keep the load evenly spread across your indexers like evenly distributed weight in a scale."

    n sensai "And if you ever need to restart, 'Rolling Restart' is your tool. It's like changing tires on a moving car - one at a time, so you never lose momentum."

    n sensai "Lastly, if you need to step back, 'Disable Indexer Clustering' allows you to release the manager node from its duties, like stepping away from the captain's wheel."

    n sensai "Now, with these tools at your fingertips, you're equipped to manage your indexer cluster with precision. Shall we proceed to explore how these changes impact your Splunk environment?"

    # Transition to the next part of the training/book
    jump install_master_node_other_options

label install_master_node_other_options:

    # Here you would define what happens next in the story or training scenario
    return

