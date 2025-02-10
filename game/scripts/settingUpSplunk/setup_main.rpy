define e = Character("Expert", color="#0066cc")

label setup_start:
    scene bg_workshop  # Assuming you have a background image named 'workshop'
    #show screen lab_setup  # If you have a custom screen for UI elements

    show narrator sensai at left 

    n sensai "Welcome to the overview of Splunk infrastructure, where we’ll dive into the Splunk environment and get a basic setup overview."
    n sensai "It’s crucial to approach this with a plan; you can’t just throw together a Splunk environment haphazardly."
    n sensai "We’ll walk through what we aim to achieve and outline the structure of our Splunk environment in our test lab."

    menu:
        "What are the main objectives for this section?"
        "Identify common systems and resources needed for Splunk infrastructure.":
            n sensai "Exactly, we need to identify common systems within a Splunk environment and understand the resources required for these various infrastructures."

    n sensai "For our Splunk environment, here are several key components we’ll need to set up:"

    # Indexer Cluster
    n sensai "First, we'll set up an indexer cluster. For it to be effective, you need at least three indexers."
    n sensai "With only two, it’s not really a cluster—it’s more like a direct backup."
    n sensai "In a proper indexer cluster, data is distributed across three or more indexers, with each piece of data stored on at least two."
    n sensai "If one indexer goes down, you can still search all your data."
    n sensai "To manage this, you’ll need a master/manager node, which controls the cluster and ensures data replication."

    # License Server
    n sensai "Next, we need to address Splunk licensing. All systems require a license, so we'll use a single license server that all other systems will point to."

    # Management Console
    e "We will also set up a Management Console to monitor the health of all our systems in one place."

    # Deployment Server
    n sensai "For managing updates and configurations, we'll need a Deployment Server. It's essential for handling configurations on Universal Forwarders."
    n sensai "Universal Forwarders operate through the command line without a GUI, so connecting them to a Deployment Server ensures they receive the necessary apps and commands."
    n sensai "I used to manage standalone search heads with this, but as environments grew complex, I've shifted to using Git for managing search head configurations."

    # Search Head Cluster
    n sensai "Now, let's talk about setting up a search head cluster. It consists of multiple search heads, typically at least three, with one acting as the captain."
    n sensai "The captain coordinates activities, ensuring searches are distributed and results are gathered efficiently."
    n sensai "For managing apps in this cluster, you’ll use a deployer instead of a deployment server."

    # Managing Configurations
    n sensai "Each component in Splunk has a different way to manage apps:"
    n sensai "- The Master Node for indexer clusters."
    n sensai "- A Deployer for search head clusters."
    n sensai "- And a Deployment Server for Universal Forwarders and standalone instances."

    # Combining Roles or Keeping Them Separate
    n sensai "When setting up, consider how to allocate resources:"
    n sensai "- The License Server doesn’t need much, so it can be combined with others."
    n sensai "- The Management Console might need its own machine in larger setups."
    n sensai "- The Deployment Server depends on how many devices it manages."
    n sensai "- The Master Node should be separate for high indexing loads."

    n sensai "In our test environment, with modest scale, we can combine these roles onto one machine, but as your setup grows, you'll want to separate them."

    # End of the tutorial section
    n sensai "That’s a basic overview of setting up a Splunk environment. Let's move on to the interactive lab where you'll apply what you've learned."

    jump interactive_lab  # Assuming you have a label for where the lab starts

label interactive_lab:
    # Here you would define the interactive elements of the lab, 
    # where users might click to set up components or make choices about infrastructure setup
    n sensai "We've just covered the basic setup of a Splunk environment. Now, let's delve into some planning best practices to ensure your deployment can handle current and future workloads effectively."

    jump planning_best_practices
    return

