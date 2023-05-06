import re

text = """
James Rew has been living on the edge, quite literally, and he nicks the first delivery with the replacement ball from Jack White straight to the breadbasket of Hassan Azad at second slip.
Somehow Azad can only fumble it down and to his right but first slip is not quite able to snag the rebound. Azad himself was dropped in the slips in the first over of the match on Thursday.
A huge let-off for Somerset and Rew.
It's Azad sad situation for the visitors.
"""

words = re.findall("\w+", text)

for w in sorted(set(words)):
    print(f"{w:15}  {words.count(w):3}")
