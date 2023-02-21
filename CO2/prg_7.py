# word=str(input("enter the word:"))
# s="ing"
# for i in range(0,len(word)):
#     if word[-3]=='i' and word[-2]=='n' and word[-1]=='g':
#         print(word+"ly")
#         break
#     else:
#         print(word+"ing")
#         break
    
# #or
word=str(input("enter the word:"))
if word.endswith("ing"):
    word+='ly'
else:
    word+='ing'
print(word)