#upper() To convert all characters to upper case 
#lower() -To convert all characters to lower case 
#swapcase() -Converts all lower case characters to upper case and all upper case characters to lower case 
#title() -To convert all character to title case. i.e first character in every word should be upper case and all remaining characters should be in lower case. 
#capitalize() -Only first character will be converted to upper case and all remaining characters can be converted to lower case 
s=input("enter the str")
if(s.isdigit()):
   print("digit")
elif(s.isspace()):
    print("space")
elif(s.isalpha()):
    if (s.islower()):
        print("isalpha lower")
    elif (s.isupper()):
        print("isalpha upper")
    else:
        print("isalpha")
elif(s.isalnum()):
    if (s.islower()):
        print("isalnum.Lower")
    elif(s.isupper()):
        print("isalnum.upper")
    else:
        print("isalnum")
else:
    print("Special charcter")