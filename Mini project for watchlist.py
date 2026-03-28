
watchlist=[]
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
        print(f"{moviename} Movie is added in your watchlist ")
    elif choice==2:
        removemoviename=input("Enter the movie name for remove:")
        if removemoviename==watchlist:
            print("You typed movie name is wrong...")
            print("Try Again")
        else:
            watchlist.remove(removemoviename)
            print(f"{removemoviename} movie is removed from the watchlist")
    elif choice==3:
        print("Your Watchlist...................................")
        if not watchlist:
            print("Your Watchlist is Empty......................")
        else:
            for i in range(len(watchlist)):
                print(f"{i+1}.{watchlist[i]} movie")
    elif choice==4:
        print("Thank you.............Happy Watching........")
        break
    else:
        print("Invalid choice.......................................")    
