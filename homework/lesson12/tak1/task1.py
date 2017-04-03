content=open('content', 'r').readlines()
word=input("Put your word")

output=[]

for line in content:
    #print(line)
    if word in line:
        output.append(str(content.index(line)) + " " + line)

out=open('output', 'w')

out.writelines(output)