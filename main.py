

text=""
dic = {}
words=0

with open("books/frankenstein.txt",mode="rt") as file:
    contents = file.read()

contents_words=contents.split()
lowered_string = contents.lower()


for x in lowered_string:
    if x in dic:
        dic[x] = dic[x] + 1
    else:
        dic[x] = 1


print ("Begin analysis of books/frankenstein.txt")
print (f"The book contains:",len(contents),"words")

for x,y in dic.items():
    if x.isalpha() == True:
        print("The",x,"character was fount",y,"times")