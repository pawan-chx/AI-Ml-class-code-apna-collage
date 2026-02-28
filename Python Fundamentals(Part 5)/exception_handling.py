try:
    x = int(input("Enter x:" ))
    ans = 10/x
    
except ZeroDivisionError:     # ZerodivisionError ka matlab 0(zero) se kisi ko divide karna jo 
    print("Divide by 0 is no allowed")

except ValueError:
    print("Invalid input")   

else:
    print(f"ans = {ans}")        

finally:    #ye hamesa run hoga
    print("End of program")

    #agar aur inbuilt exception ko janna hai to search on ki inbuild exception in python isme to do hi likha hai