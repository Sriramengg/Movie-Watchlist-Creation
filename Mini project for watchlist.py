import json
def save_data(data):
    with open("datab.json","w")as f:
        json.dump(data,f)
def load_data():
    with open("datab.json","r")as f:
        return json.load(f)

us=load_data()

watchlist=[]
while True:
    print("...................Watchlist.........................")
    print("1.Create a New Account")
    print("2.Login to your watchlist account")
    print("3.Remove your watchlist account")
    print("4.Exit")
    choic=int(input("Enter your choice:(1,2,3,4)........."))
    if choic==1:
        print("...............Watchlist Login...................")
        while True:
            user=input("Enter your New Username:")
            if(len(user)<=7):
                print("⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️  ⚠️")
                print("Please Change your username to extend with upto 8 characters")
            elif user in us:
                print("Username already exist.................⚠️")
            else:
                break
        while True:
            pasw=input("Enter your Password:")
            if(len(pasw)<=8):
                print("⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️  ⚠️")
                print("Please Change your Password to extend with upto 8 characters")
            else:
                break
        us[user]={"Password":pasw,"Watchlist":[]}
        save_data(us)
        print("Successfully Created your Account  ✅")
    elif choic==2:
        user=input("Enter your Username:")
        pasw=input("Enter the Password:")
        if user in us and us[user]["Password"]==pasw:
            print(f"Welcome {user}!")
            watchlist=us[user]["Watchlist"]

        
    
    
            while True:
                print(".....................................................")
                print("Edit the Your watchList............")
                print("1.Add Movie")
                print("2.Remove Movie")
                print("3.Display watchlist all movies")
                print("4.Exit")
                choice =int(input("Enter Your choice:(1,2,3,4)......"))
                if choice==1:
                    moviename=input("Enter the movie name:")
                    watchlist.append(moviename)
                    save_data(us)
                    print(f"{moviename} Movie is added in your watchlist ")
                elif choice==2:
                    
                    while True:
                        removemoviename=input("Enter the movie name for remove:")
                        if removemoviename not in watchlist:
                            print("You typed movie name is wrong...")
                            print("Try Again")
                        else:
                            watchlist.remove(removemoviename)
                            save_data(us)
                            print(f"{removemoviename} movie is removed from the watchlist!")
                            break
                elif choice==3:
                    print("Your Watchlist...................................")
                    if not watchlist:
                        print("Your Watchlist is Empty......................")
                    else:
                        for i in range(len(watchlist)):
                            print(f"{i+1}.{watchlist[i]} movie")
                elif choice==4:
                    print("Thank you.............Happy Watching........Logging Out")
                    break
                else:
                    print("Invalid choice.......................................")    

        else:
            print("⚠️ Please check the Username and Password")
    elif choic==4:
        print("Thank you.............Happy Watching")
        break
