fo = open("words.txt","r")
items = fo.readlines()


final_list = final_list = [i.strip() for i in items if len(i) < 8]
print(final_list)






