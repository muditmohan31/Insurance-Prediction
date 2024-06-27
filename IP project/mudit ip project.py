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
print ("What do you want to have?", "1.Car Insurance", "2.Two wheeler insurance", "3.Commercial vehicle policy ", sep="\n")
ins=input("Enter the type of insurance:")
if ins=="1" or ins=="Car-Insurance":
    print("PREMIUM CALCULATOR")
    a=input("Enter the vheicle registration Number:")
    d=input("Mention your RTO & City:")
    f=input("Name your vhecile manufacturer:")
    g=input("Get your vheicle model:")
    s=int(input("Enter the year of manufacturing :"))
    x=int(input("Enter your vehicle cubic capacity :"))
    at=int(input("Enter the vehicle seating capacity :"))
    b=input("Press 'y' if there is claim or Press 'n' if there is no claim :")
    if b=="n" or b=="y":
        sq=input("is last poilcy is expired by more than 90 days (y/n):")
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
                l=z
                print("The IDV of vehicle is :50000")
            else:
                print("The present value of your vehcile is(IDV):", h-((k/100)*h))
            if (j.year-s)<=5 and x<=1500:
                c=((h-((k/100)*h))*3.19)/100
                print("the raw premium",c)
            elif (j.year-s)<=5 and x>1500:
                c=((h-((k/100)*h))*3.90)/100
                print("The raw premium",c)
            if sq=="y" and b=="y":
                v=0
            elif sq=="n" and b=="n":
                v=v
            elif sq=="n" and b=="y":
                v=v
            elif sq=="y" and b=="n":
                v=v
            if m=="y" and b=="y":
                v=0
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="y" and b=="n"):
                v=v+10
                if v>=50:
                    v=50
                else:
                    v=v
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="n" and b=="y"):
                v=v+10
                if v>=50:
                    v=50
                else:
                    v=v
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="n" and b=="n"):
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
            elif ar=="n":
                aw=aw+0
            print("price after adding onwer cover:", aw)
                    
            if ae=="y":
                aw=aw+50
            elif ae=="n":
                aw=aw+0
            print("Premium after adding paid driver cover:", aw)
                    
            if ay=="y":
                aw=aw+(at*100)
            elif ay=="n":
                aw=aw+0
            print("premium after adding unknown passenger cover:", aw)
            print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
            print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            
            if (j.year-s)>5 and x<=1500:
                c=((h-((k/100)*h))*3.51)/100
                print("The raw premium",c)
            elif (j.year-s)>5 and x>1500:
                c=((h-((k/100)*h))*4.5)/100
                print("The raw premium",c)
            if sq=="y" and b=="y":
                v=0
            elif sq=="n" and b=="n":
                v=v
            elif sq=="n" and b=="y":
                v=v
            elif sq=="y" and b=="n":
                v=v
            if m=="y" and b=="y":
                v=0
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="y" and b=="n"):
                v=v+10
                if v>=50:
                    v=50
                else:
                    v=v
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="n" and b=="y"):
                v=v+10
                if v>=50:
                    v=50
                else:
                    v=v
                print("NCB discount:",v)
                print("NCB disounted premium:",(c-(v/100)*c))
            elif (m=="n" and b=="n"):
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
            elif ar=="n":
                aw=aw+0
            print("price after adding onwer cover:", aw)
                    
            if ae=="y":
                aw=aw+50
            elif ae=="n":
                aw=aw+0
            print("Premium after adding paid driver cover:", aw)
                    
            if ay=="y":
                aw=aw+(at*100)
            elif ay=="n":
                aw=aw+0
            print("premium after adding unknown passenger cover:", aw)
            print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
            print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))

        if ins2=="2":
            h=int(input("Enter the EX SHOWROOM PRICE:"))
            import datetime
            j=datetime.datetime.now()
            k=(j.year-s)*10
            l=(h-((k/100)*h))*0
            print("The present value of your vehcile is(IDV):", l)
            if (j.year-s)<=5 and x<=1500:
                c=((h-((k/100)*h))*3.19)/100
            elif (j.year-s)<=5 and x>1500:
                c=((h-((k/100)*h))*3.90)/100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            else:
                if (j.year-s)>5 and x<=1500:
                    c=((h-((k/100)*h))*3.51)/100
                elif (j.year-s)>5 and x>1500:
                    c=((h-((k/100)*h))*4.5)/100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))

if ins=="2" or ins=="Two-wheeler-Insurance":
    print("PREMIUM CALCULATOR")
    a=input("Enter the vheicle registration Number:")
    d=input("Mention your RTO & City:")
    f=input("Name your vhecile manufacturer:")
    g=input("Get your vheicle model:")
    s=int(input("Enter the year of manufacturing :"))
    x=int(input("Enter your vehicle cubic capacity :"))
    at=int(input("Enter the vehicle seating capacity :"))
    b=input("Press 'y' if there is claim or Press 'n' if there is no claim :")
    if b=="n":
        sq=input("is last poilcy is expired by more than 90 days (y/n):")
        v=int(input("Enter the NCB discount:"))
        if sq=="y":
            v=0
        else:
            v=v
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
            z=10000
            if l<=z:
                print("The IDV of vehicle is :50000")
            else:
                print("The present value of your vehcile is(IDV):", h-((k/100)*h))
            if (j.year-s)<=5 and x<=150:
                c=((h-((k/100)*h))*1.5)/100
            elif (j.year-s)<=5 and x>150:
                c=((h-((k/100)*h))*2.5)/100
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
                if x<=150:
                    aw=972
                else:
                    aw=1100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            else:
                if (j.year-s)>5 and x<=150:
                    c=((h-((k/100)*h))*2.0)/100
                elif (j.year-s)>5 and x>1500:
                    c=((h-((k/100)*h))*3.0)/100
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
                if x<=150:
                    aw=972
                else:
                    aw=1100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
        if ins2=="2":
            h=int(input("Enter the EX SHOWROOM PRICE:"))
            import datetime
            j=datetime.datetime.now()
            k=(j.year-s)*10
            l=(h-((k/100)*h))*0
            print("The present value of your vehcile is(IDV):", l)
            if (j.year-s)<=5 and x<=150:
                c=((h-((k/100)*h))*1.5)/100
            elif (j.year-s)<=5 and x>1500:
                c=((h-((k/100)*h))*2.5)/100
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
                if x<=150:
                    aw=972
                else:
                    aw=1100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            else:
                if (j.year-s)>5 and x<=150:
                    c=((h-((k/100)*h))*2.0)/100
                elif (j.year-s)>5 and x>150:
                    c=((h-((k/100)*h))*3.0)/100
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
                if x<=150:
                    aw=972
                else:
                    aw=1100
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
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))

if ins=="3" or ins=="Commercial-policy":

    print("PREMIUM CALCULATOR")
    a=input("Enter the vheicle registration Number:")
    d=input("Mention your RTO & City:")
    f=input("Name your vhecile manufacturer:")
    g=input("Get your vheicle model:")
    s=int(input("Enter the year of manufacturing :"))
    x=int(input("Enter your vehicle cubic capacity :"))
    at=int(input("Enter the vehicle seating capacity :"))
    b=input("Press 'y' if there is claim or Press 'n' if there is no claim :")
    if b=="n":
        sq=input("is last poilcy is expired by more than 90 days (y/n):")
        v=int(input("Enter the NCB discount:"))
        if sq=="y":
            v=0
        else:
            v=v
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
            if (j.year-s)<=5 and x<=1500:
                c=((h-((k/100)*h))*3.21)/100
            elif (j.year-s)<=5 and x>1500:
                c=((h-((k/100)*h))*4.12)/100
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
                    aw=5172
                else:
                    aw=6125
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
                    aw=aw+((at-1)*1000)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            else:
                if (j.year-s)>5 and x<=1500:
                    c=((h-((k/100)*h))*3.94)/100
                elif (j.year-s)>5 and x>1500:
                    c=((h-((k/100)*h))*5.0)/100
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
                    aw=5172
                else:
                    aw=6125
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
                    aw=aw+((at-1)*1000)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
        if ins2=="2":
            h=int(input("Enter the EX SHOWROOM PRICE:"))
            import datetime
            j=datetime.datetime.now()
            k=(j.year-s)*10
            l=(h-((k/100)*h))*0
            print("The present value of your vehcile is(IDV):", l)
            if (j.year-s)<=5 and x<=1500:
                c=((h-((k/100)*h))*3.90)/100
            elif (j.year-s)<=5 and x>1500:
                c=((h-((k/100)*h))*4.12)/100
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
                    aw=5172
                else:
                    aw=6125
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
                    aw=aw+((at-1)*1000)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                                                   
            else:
                if (j.year-s)>5 and x<=1500:
                    c=((h-((k/100)*h))*4.0)/100
                elif (j.year-s)>5 and x>1500:
                    c=((h-((k/100)*h))*5.0)/100
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
                    aw=5172
                else:
                    aw=6125
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
                    aw=aw+((at-1)*1000)
                else:
                    aw=aw+0
                print("premium after adding unknown passenger cover:", aw)
                print("Premium after adding gst:",((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))
                    
                print(" The premium to be paid:", ((c-(v/100)*c)+aw +(18/100)*(aw+(c-(v/100)*c))))

