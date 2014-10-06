#Ryan Cox
#03/10/14
#A program that converts ascii code to its equivalent text character and visa versa

convert = str(input("Hello, if you would like to convert ASCII code to text enter 'ASCCI' or if you would like to convert text to ASCII enter 'TEXT': "))

if convert == "ASCII":
    ASCII = int(input("Please enter the ASCII code you wish to convert: "))
    answer = chr(ASCII)
    print("The ASCII equivalent is '{0}'" .format(answer))
               

elif convert == "TEXT":
    Text = str(input("Please enter the Text you wish to convert: "))
    answer = ord(Text)
    print("The Text equivalent is '{0}'" .format(answer))


else:
    print("What you have entered is invalid, please try again. If you would like to convert ASCII code to text enter 'ASCCI' or if you would like to convert text to ASCII enter 'TEXT': ")  

               


