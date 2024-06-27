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
