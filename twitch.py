"""
The questions was something along the lines of:
    'given a string with a streamer, a category, and number of views-
    1. find the streamer with the most number of views
    2. find the category with the most highest number of views
    3. find the streamer with the least number of views
    4. find the least-viewed category'

I believe this is something along the lines of what was expected. Sadly, I didn't pass the interview the first time around.
I hope this shows my commitment to Twitch, and hope you will consider giving me a new chance to apply with a new question.

If you've received this, and actually read this, I appreciate it more than you can imagine. Thank you. 
"""

#sample input
s = "xQcOW, Just Chatting, 54000, Pokimane, Valorant, 21000, Sykkuno, GTA V, 20000, shroud, New World, 20100, summit1g, Sea of Thieves, 12300"

#this function creates a list of dictionaries, seperating streamers with their respective category and number of views.
def makeDicts(s):
    s = s.split(", ")

    dic2 = []

    for i in range(len(s) - 2):
        if i % 3 == 0:
            dic2.append({"Streamer": s[i], "Category": s[i + 1], "Views": s[i + 2]})
    
    return dic2

myDic = makeDicts(s)

#this function can return the streamer with the most views, or the highest category, etc... depending on the input
#I don't 100% recall how the format of the output was supposed to be like, so I kind of merged everything into one,
#but the original message might have been asked for a slighlty different output
def highestStream(dic2, s):
    maxViewers = 0
    maxStreamer = ""
    maxCategory = ""
    for i in range(len(dic2)):
        if maxViewers < int(dic2[i]["Views"]):
            maxViewers = int(dic2[i]["Views"])
            maxStreamer = dic2[i]["Streamer"]
            maxCategory = dic2[i]["Category"]
    if s == "Views":
        return maxViewers
    if s == "Streamer":
        return maxStreamer
    if s == "Category":
        return maxCategory

#this function will return the streamer/category with the least number of views, same as the above function, but with minimum values.  
def minStream(dic2, s):
    minViewers = float("inf")
    minStreamer = ""
    minCategory = ""
    for i in range(len(dic2)):
        if minViewers > int(dic2[i]["Views"]):
            minViewers = int(dic2[i]["Views"])
            minStreamer = dic2[i]["Streamer"]
            minCategory = dic2[i]["Category"]
    if s == "Views":
        return minViewers
    if s == "Streamer":
        return minStreamer
    if s == "Category":
        return minCategory

#some test cases.
print(f'The highest stream is {highestStream(myDic, "Streamer")} with {highestStream(myDic, "Views")} viewers, they are streaming {highestStream(myDic, "Category")}')
print(f'The smallest stream is {minStream(myDic, "Streamer")} with {minStream(myDic, "Views")} viewers, they are streaming {minStream(myDic, "Category")}')