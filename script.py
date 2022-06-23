a=open("Rules.txt", "r",encoding='utf-8')
b=open("Rulespy.txt","w",encoding='utf-8')
for i in range (300):
    s=a.readline()
    if ":" in s or "*" in s:
        b.write(s[5:len(s)-2]+"\n")