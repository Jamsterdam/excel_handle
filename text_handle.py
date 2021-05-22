############### well, I have to say, this is a clumsy script, but anyway it works.

# import the content
str = "https://www.notion.so/Apex-Machinery-Pvt-Limited-667016afe96845dd975fadf11dad907c"

# strip the notion address part
body = str.strip("https://www.notion.so/")

#revere the left part, then it is easy to remove the long meaningless tail.
back = body[::-1]
part1,sep,part2 = back.partition("-")
clientName = part2[::-1]
print(clientName)

