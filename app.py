#we will be covering mostly important syntax gaps.

'''
#In general, [] paranthesis are for lists, () paranthesis are for tuples, and {} paranthesis are for dictionaries.
#try/catch -> try/except
'''
#Python gives us the ability to check what permissions of a file we have.
#Incase we want to read from a file, we can simply ask, is he readable? is he writable?
#If the file does not exist, indicate it by mode w+, which will create the new file.
new_file = open("Members.txt","r")
print(new_file.readable())
print(new_file.writable())
new_file.close()