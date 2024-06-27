print ("WELCOME TO BIMA GHAR ")
print("1: CREATE-ACCOUNT ","2: LOGIN", sep="\n")
ch=input("Enter your choice:")
if ch=="1" or ch=="CREATE-ACCOUNT":
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
elif ch=="2" or ch=="LOGIN":
    o=input("Enter the username:")
    p=input("Enter your password:")
print ("What do you want to have?", "1.Car Insurance", "2.Two wheeler insurance", "3.Life Insurance ", sep="\n")
ins=input("Enter the type of insurance:")
if ins=="1" or ins=="Car-Insurance":
    print("1. Create a new policy ","2. Renew your policy ")
    ins1=input(" ")
    if ins1=="1":
        a=input("Enter the vheicle registration Number:")
        d=input("Mention your RTO & City:")
        f=input("Name your vhecile manufacturer:")
        g=input("Get your vheicle model:")
        s=int(input("Enter the year of manufacturing:"))
        x=int(input("Enter your vehicle cubic capacity:"))
        at=int(input("Enter the vehicle seating capacity:"))
        b=input("Press 'y' if there is claim or Press 'n' if there is no claim:")
        if b=="n":
            v=int(input("Enter the NCB discount:"))
        m=input("has owner changed (y/n):")
        ae=input("Do you want to have PAID DRIVER LEGAL LIABALITY COVER (y/n):")
        ar=input("Do you want to have OWNER DRIVER COVER of 15 lak (y/n):")
        # If you have a valid driving licence then you have to adopt "yes" only otherwise you have not a valid driving licence
        ay=input("Do you want UNNAMED PASSENGER COVER (y/n):")
        print("1. comprehensive policy ", "2.Third party policy", sep='\t')
        ins2=input(" ")
        if ins2=="1":
            h=int(input("Enter the EX SHOWROOM PRICE:"))
            import datetime
            j=datetime.datetime.now()
            k=(j.year-s)*10
            l=h-((k/100)*h)
            z=50000
            if l<=z:
                print("The IDV of vehicle is :50000")
            else:
                print("The present value of your vehcile is(IDV):", h-((k/100)*h))
            if (j.year-s)<=5:
                c=((h-((k/100)*h))*3.19)/100
                print(c)
                if m=="y" and b=="y":
                    v=0
                else:
                    v=v+10
                    if v>=50:
                        v=50
                    else:
                        v=v
                        print("NCB discount:",v)
                        print("NCB disounted premium:",(c-(v/100)*c))
                aw=0
                if x<=1500:
                    aw=2172
                else:
                    aw=3125
                print("Charges of cc:", aw)
                    
                if ar=="y":
                    aw=aw+300
                else:
                    aw=aw+0
                print("price after adding onwer cover:", aw)
                    
                if ae=="y":
                    aw=aw+50
                else:
                    aw=aw+0
                print("Premium after adding paid driver cover:", aw)
                    
                if ay=="y":
                    aw=aw+(at*100)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))
            else:
                 c=((h-((k/100)*h))*3.51)/100
                print(c)
                if m=="y" and b=="y":
                    v=0
                else:
                    v=v+10
                    if v>=50:
                        v=50
                    else:
                        v=v
                        print("NCB discount:",v)
                        print("NCB disounted premium:",(c-(v/100)*c))
                aw=0
                if x<=1500:
                    aw=2172
                else:
                    aw=3125
                print("Charges of cc:", aw)
                    
                if ar=="y":
                    aw=aw+300
                else:
                    aw=aw+0
                print("price after adding onwer cover:", aw)
                    
                if ae=="y":
                    aw=aw+50
                else:
                    aw=aw+0
                print("Premium after adding paid driver cover:", aw)
                    
                if ay=="y":
                    aw=aw+(at*100)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))
           
                
