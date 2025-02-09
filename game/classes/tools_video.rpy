init python:
    class tools_video(object):
        def __init__(self, url, title, about):
            self.title = title
            self.url = url
            self.about = about

label InitializeToolsVideos:
    default tvideo1 = tools_video("https://youtu.be/jhKmYT3SEac","Free Tools To Use For Creating Quality YouTube Videos","This is a tutorial on how I make my YouTube videos.  I use the following tools on my Ubuntu Linux box. I use Kazam for video recording. Audacity for removing background sound from my mic. KdenLive for piecing together videos and sound together to one video.")
    $ ListOfTools.append(tvideo1)
    default tvideo2 = tools_video("https://youtu.be/n27s80wXr_A","I Can't Read the Content on the Page - What Do I Do?","This quick video will demo how to take a screen shot of the language you can't read and how to use Google Lens to quickly translate that image for you.")
    $ ListOfTools.append(tvideo2)
    default tvideo3 = tools_video("https://youtu.be/PwriGyeCiEg","Navigation Pages Made Simple","Suggestion / Tutorial for a way of tracking the IP addresses of multiple systems in your network.")
    $ ListOfTools.append(tvideo3)
    default tvideo4 = tools_video("https://youtu.be/6PjNibpJxyQ","Gravwell - A Modern Alternative to Splunk and Elastic for Log Collection | Overview","This video will cover the basic concepts of how to use Gravwell and how it provides many of the same tools that are found in other Log tools.   This is a great product to use at home and see if it makes sense for your companies logging solution.")
    $ ListOfTools.append(tvideo4)
    


