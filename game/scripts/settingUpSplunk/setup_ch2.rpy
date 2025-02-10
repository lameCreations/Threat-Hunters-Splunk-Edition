label planning_best_practices:
    scene bg_office  # Assuming you have an office background image
    #show screen planning_docs  # If you have a custom screen for displaying planning documents

    show narrator sensai at left 
    n sensai "Capacity planning for Splunk is critical. Let's go through best practices for different Splunk environments."

    # Indexer Cluster
    n sensai "First, the indexer cluster. Use one if your data ingestion exceeds 300-500 GB daily. It provides better performance, load balancing, and redundancy."
    n sensai "For a standard environment, each indexer can handle 100-300 GB per day. ES and ITSI environments might push this down to 100-150 GB due to higher search loads."
    n sensai "To determine the number of indexers, divide your total daily data by the ingestion rate per indexer."

    # Search Head Cluster
    n sensai "Now, for the search head cluster. You'll need this if you're dealing with a high number of concurrent searches or need high availability."
    n sensai "In a standard environment, a single search head can manage 12-15 active users or searches. ES and ITSI benefit from clustering due to their continuous monitoring demands."

    # Resource Guidelines by Environment
    n sensai "Let’s look at resource guidelines:"
    n sensai "- Standard Splunk: Plan for 100-300 GB per indexer daily."
    n sensai "- Enterprise Security: Aim for 100-150 GB per indexer."
    n sensai "- ITSI: Similar to ES, but keep in mind the continuous service monitoring."

    # Additional Considerations
    n sensai "Remember, hardware specs, replication factor, and retention policies are crucial in your planning. You want to balance data availability with storage costs."

    n sensai "For my setup, I'm using Ubuntu Server. It's free, reliable, and well-supported. But you can use any Linux distribution you're comfortable with."

    n sensai "Here are some general hardware guidelines:"
    n sensai "- Single-instance: 12 CPU cores, 12 GB RAM, 1 Gbps NIC."
    n sensai "- For test labs, you can scale down; I managed with 4 cores and 8 GB RAM."
    n sensai "- Search head clustering typically requires 16 CPUs and 12 GB RAM per node, but for our test environment, we'll use 4 cores and 8 GB RAM."

    n sensai "Indexer requirements vary with performance needs; a low-performance one might work with 12 cores and 12 GB RAM. Storage depends on your data ingestion and retention policy."

    n sensai "For management components like the Management Console or License Server, you don't need high-end hardware. 16 CPU cores and 12 GB RAM should suffice."

    n sensai "My environment setup will use about 8 CPU cores and 8 GB RAM per instance, which is below recommended specs but suitable for our minimal data ingestion of about 500 MB per day."

    ### Fix me later
    #n sensai "Now, for better planning, I've created a capacity planning worksheet. You can find it at my GitHub repo: [github.com/lameCreations/SplunkSystemAdminCourse](https://github.com/lameCreations/SplunkSystemAdminCourse)."
    n sensai "Now, for better planning, I've created a capacity planning worksheet. You can find it at my GitHub repo: (https://github.com/lameCreations/SplunkSystemAdminCourse)."

    n sensai "Here's a quick look at my planning for our test environment:"
    n sensai "- Daily Data Ingestion: ~100 MB/day, just internal Splunk logs."
    n sensai "- Number of Indexers: One for now, but planning for three in a cluster."
    n sensai "- Indexer Clustering: Replication factor of 2, search factor of 2."
    n sensai "- Daily Search Loads: About 50 queries."
    n sensai "- Search Heads: One suffices for now, but I'll use a cluster for high availability."
    n sensai "- No ES or ITSI in this setup, so lighter on resources."

    n sensai "Remember, documenting your systems saves time in the long run, especially as we age and memory fades. Here's how I've mapped out our systems:"

    # Display the table or screenshot here if possible, or narrate the details
    n sensai "Management Console and License Server share an IP at 192.168.1.175, hostname 'lame_mc'. Deployment Server at 192.168.1.185, 'lame_ds', and so forth for all components."

    n sensai "I'll be using Proxmox for virtualization. It's free and robust, unlike ESXi which now requires payment. I'll set up eight Ubuntu Server instances to deploy Splunk Enterprise, but we'll focus on one for clarity."

    n sensai "Let's move on to actually setting up our Splunk environment in the next interactive lab."

    jump interactive_lab_setup_ch2

label interactive_lab_setup_ch2:
    # Here you would define the interactive elements for setting up Splunk
    n sensai "With the planning out of the way, let's get to the fun part—installing Splunk Enterprise on our systems."

    jump install_splunk_enterprise
    return