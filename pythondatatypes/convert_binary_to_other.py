# 2/28/2023 - Hanumantha Reddy Moola code to convert the binary form to other form like decimal/octal/hexadecimal
# \033[1;32m this will helps to change the default color of output text to required color
# \033[1;0m this will break the continuation of color coding output
print('Press 1 to convert from binary to decimal form...')
print('Press 2 to convert from decimal to octal form...')
print('Press 3 to convert from decimal to hexadecimal form...')
a=int(input('Please press anyone of the above number to continue...  '))
if a in (1,2,3):
    if(a==1):
        STRING=str(input('ENTER A BINARY FORMAT NUMBER TO CONVERT TO DECIMAL : '))
        STRING2='01'
        i,j=0,0
        for i in range(len(STRING)):
            if(STRING[j] in STRING2):
                j+=1
            else:
                print('\033[1;31m❌ You enterd an invalid format, please try again ❌\033[0m')
                break
        if(j==len(STRING)):
            j=int(STRING,2)
            print('\033[1;32mHere is the converted output of the integer',STRING,'to decimal form',j,'\033[0m')
    elif(a==2):
        STRING=str(input('ENTER AN OCTAL FORMAT NUMBER TO CONVERT TO DECIMAL : '))
        STRING2='01234567'
        i,j=0,0
        for i in range(len(STRING)):
            if(STRING[j] in STRING2):
                j+=1
            else:
                print('\033[1;31m❌ You enterd an invalid format, please try again ❌\033[0m')
                break
        if(j==len(STRING)):
            j=int(STRING,8)
            print('\033[1;32mHere is the converted output of the integer',STRING,'to decimal form',j,'\033[0m')
    else:
        STRING=str(input('ENTER A HEXADECIMAL FORMAT NUMBER TO CONVERT TO DECIMAL : '))
        STRING2='0123456789abcdef'
        i,j=0,0
        for i in range(len(STRING)):
            if(STRING[j].lower() in STRING2):
                j+=1
            else:
                print('\033[1;31m❌ You enterd an invalid format, please try again ❌\033[0m')
                break
        if(j==len(STRING)):
            j=int(STRING,16)
            print('\033[1;32mHere is the converted output of the integer',STRING,'to decimal form',j,'\033[0m')
else:
    print('You entered an invalid integer',a,'Please provide valid input')