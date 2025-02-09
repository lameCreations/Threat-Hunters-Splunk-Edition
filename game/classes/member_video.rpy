init python:
    class member_video(object):
        def __init__(self, url, title, about):
            self.title = title
            self.url = url
            self.about = about

label InitializeMemberVideos:
    default mvideo1 = member_video("https://youtu.be/Q8cAmfmvDsA","Splunk System Admin Training","Free training for members of my youtube channel on how to setup and run Splunk on Linux or Windows.")
    $ ListOfMember.append(mvideo1)
    default mvideo2 = member_video("https://youtu.be/qy4POqMXPLo","Splunk User Training","Free training for members of L.A.M.E. Creations on how to use many of the SPL commands and examples of use cases.")
    $ ListOfMember.append(mvideo2)
    default mvideo3 = member_video("https://youtu.be/BH0_Hry9jxs","L.A.M.E. Custom Apps to Improve Productivity","Free training for members of L.A.M.E. Creations on the custom apps that L.A.M.E. has created to increase their own productivity and to extradite training.")
    $ ListOfMember.append(mvideo3)
    default mvideo4 = member_video("https://youtu.be/8MWXXsJoUbo","Looking for IOCs Across All Time | How to search for events like SolarFlare Quickly and Efficiently","It can be a time consuming process to search for Intel data across huge data sets and especially over long periods of time.  This training video will demonstrate lessons learned in my career and how to build a resilient and fast system to search for IOCs across all of your historical data if the occasion should arise.")
    $ ListOfMember.append(mvideo4)
    default mvideo5 = member_video("https://youtu.be/wfOBW5cd32M","Splunk Advanced Search and Reporting Tutorial","This is the Beta Release of my Search and Reporting Tutorial.  It will be refined over time.")
    $ ListOfMember.append(mvideo5)
    default mvideo6 = member_video("https://youtu.be/9i1KhKhLU1g","Splunk Dashboards and Visualizations Training","Free training for members of my youtube channel on how to create dashboards and improve those dashboards with visualizations.")
    $ ListOfMember.append(mvideo6)


