init python:
    class cribl_video(object):
        def __init__(self, url, title, about):
            self.title = title
            self.url = url
            self.about = about

label InitializeCriblVideos:
    default cvideo1 = cribl_video("https://youtu.be/4989_n12cms","Cribl Stream Tutorial How To Install as Syslog Server","This video will focus on how to set up Cribl from scrach and set it up as a syslog server.")
    $ listOfCribl.append(cvideo1)
    default cvideo2 = cribl_video("https://youtu.be/w7Jc_DHF3_o","Cribl Log Stream Tutorials Destinations and Sources Explained","This video will help explain the numerous sources that Log Stream can get data from and the numbers destinations that Log Stream can send data.")
    $ listOfCribl.append(cvideo2)
    default cvideo3 = cribl_video("https://youtu.be/1DNEypB13Uo","Cribl Log Stream Tutorial - Setting Up Cribl to Ingest Syslog","This video will focus on setting up your cribl route to handle the Syslog that is being sent to your Cribl Log Stream Instance.")
    $ listOfCribl.append(cvideo3)
    default cvideo4 = cribl_video("https://youtu.be/pyOTqXhGeN0","Cribl Log Stream Example of Sending Syslog to FileStore","This tutorial will discuss setting up a source and destination for a Linux Syslog Server.  The source will be Syslog and the destination will be a file path on Cribl.")
    $ listOfCribl.append(cvideo4)
    default cvideo5 = cribl_video("https://youtu.be/EcXuBrUkrME","Cribl Log Stream Tutorial Using Pipelines to Change Syslog and Sending it To Splunk","This tutorial will read the syslogs that have been written to file and send them to Splunk.")
    $ listOfCribl.append(cvideo5)
    default cvideo6 = cribl_video("https://youtu.be/zlX4QDrp8c8","Cribl Handling XML Windows Event Logs","Cribl provides an easy ability to convert XML Windows EventLogs to Key Value pairs and reduce the size of the logs close to 50-70 percent.")
    $ listOfCribl.append(cvideo6)
    default cvideo7 = cribl_video("https://youtu.be/3b2rceG9MIU","Cribl Logstream Pipeline Overview","Cribl Logstream provides an extensive capability to manage and manipulate logs.  This video will cover some of the basic things that Cribl Logstream can do to manipulate and make your logs more effective.  The pipeline and functions allow the creation of new logs and field reduction and or enhancement.")
    $ listOfCribl.append(cvideo7)
    default cvideo8 = cribl_video("https://youtu.be/5ZXz-xOKxBU","Cribl Logstream Product Overview","Cribl Logstream is a must have product that should be implemented in any home network.  The free version of this product provides amazing capabilities.  This video will give an overview of some of the capabilities of this amazing log manipulation tool.")
    $ listOfCribl.append(cvideo8)

    

