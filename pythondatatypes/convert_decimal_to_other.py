# 2/28/2023 - Hanumantha Reddy Moola program to convert the int datatypes from decimal to binary/octal/hexadecimal or viceversa
# \033[1;32m this will helps to change the default color of output text to required color
# \033[1;0m this will break the continuation of color coding output
print('Press 1 to convert from decimal to binary form...')
print('Press 2 to convert from decimal to octal form...')
print('Press 3 to convert from decimal to hexadecimal form...')
a=int(input('Please press anyone of the above number to continue...  '))
PREFIX=''
if a in (1,2,3):
    if(a==1):
        i=int(input('ENTER AN INTEGER TO CONVERT TO BINARY FORM : '))
        j=bin(i)
        PREFIX+='0b'
        j=j.removeprefix(PREFIX)
        print('\033[1;32mHere is the converted output of the integer',i,'to binary form',j,'\033[0;m')
    elif(a==2):
        i=int(input('ENTER AN INTEGER TO CONVERT TO OCTAL FORM : '))
        j=oct(i)
        PREFIX+='0o'
        j=j.removeprefix(PREFIX)
        print('\033[1;32mHere is the converted output of the integer',i,'to octal form',j,'\033[0m')
    else:
        i=int(input('ENTER AN INTEGER TO CONVERT TO HEXADECIMAL FORM : '))
        j=hex(i)
        PREFIX+='0x'
        j=j.removeprefix(PREFIX)
        print('\033[1;32mHere is the converted output of the integer',i,'to hexadecimal form',j,'\033[0m')
else:
    print('\033[1;31mPlease select anyone of the above option, you entered',a,'value is invalid input\033[0m')
