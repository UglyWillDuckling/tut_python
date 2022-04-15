import re

txt = "Dune.2021.1080p.HDRip.X264-EVO[TGx]"
x = re.sub("\.?(1080p.*|720p.*)", "", txt)
print(x)
