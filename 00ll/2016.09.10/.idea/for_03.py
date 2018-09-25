def stripnulls(data):
    "strip whitespace and nulls"
    return data.replace("\00","").strip()

class MP3FileInfo():
    "store ID3v1.0 MP3 tags"
    tagDataMap = {"title":(3,33,stripnulls),
              "artist":(33,63,stripnulls),
              "album":(33,93,stripnulls),
              "year":(93,97,stripnulls),
              "commment":(97,126,stripnulls),
              "genre":(127,128,ord)}

print (MP3FileInfo())
print (MP3FileInfo.tagDataMap)
m = MP3FileInfo()
print (m .tagDataMap)