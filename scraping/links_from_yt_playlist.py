from pytube import Playlist, YouTube
import os
# p=Playlist("https://www.youtube.com/playlist?list=PL34jslVRIs1ffryd-uXG3CCk5oVew1bW2")
p=Playlist("https://www.youtube.com/playlist?list=PLYmZ9-bsohD5eSTwyNnyIjia7S82v4pfm")

[print(i) for i in p]
print(len(p))

# place="./sdo_youtube"
# try:
    # os.mkdir(place)
# except Exception as e:
    # print(e)
# p=[
# ]
# noDl=0
# for link in p:
    # yt=YouTube(link)
    # try:
        # yt.streams.filter(only_audio=True).first().download(place)
        # # yt.streams.get_by_itag(140).download(place)
        # # print(f"Downloaded {yt.title}")
    # except Exception as e:
        # # print(e)
        # print(f"Couldn't download: {yt.title}: {link}")
        # noDl+=1
# print(f"Couldn't download {noDl} tracks of total {len(p)}")

# print(p)
# print(len(p))
