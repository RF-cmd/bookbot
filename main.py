print ("hello world")

text=""


with open("books/frankenstein.txt",mode="rt") as file:
    contents = file.read()

contents_words=contents.split()
