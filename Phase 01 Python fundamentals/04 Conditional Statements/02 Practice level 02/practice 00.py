while True:
    # this helps to take input form the user
    user_input = input("enter anything that you can :  (Or to stop write the  exit )")

    #  helps to stop the loop , in simple steps
    if user_input == "exit":
        print("program band ho gya sir ji !")
        break
    # Input ko wapas terminal per print karna
    print(f"Apka output :{user_input}\n")
