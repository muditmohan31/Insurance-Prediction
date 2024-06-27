user={'mudit':'mud' ,'yugank':'yug' ,'monika':'mon' , 'vivek':'viv'}
u=input("Enter the username:")
if u in user:
    i=input("Enter your password:")
    if i==user[u]:
        print("WELCOME")
    elif i!=user[u]:
        print("INCORRECT PASSWORD")
        i=input("Enter your password:")
        
elif u not in user:
        print("YOU ARE NOT AN EXISTING USER PLEASE CREATE ACCOUNT")
        q=input("Enter the first name:")
        w=input("Enter the last nmame :")
        e=int(input("Enter your Mobile number:"))
        r=input("Mention your Email id:")
        t=input("Enter your Date of Birth:")
        y=int(input("Enter your age:"))
        if y>=18:
            u=input("Enter the username:")
            i=input("Enter your password:")
            print(u,i, sep="\n")
        else:
            print("SORRY!! You are not egligile to have account on BIMA GHAR ")
    
    
