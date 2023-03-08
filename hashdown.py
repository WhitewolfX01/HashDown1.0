import hashbody.nameprinterhashdown
hashbody.nameprinterhashdown.printname()
for k in range(1000):
    print("\n--- HashDown1.0 Menu ---\n1. Generate Hash\n2. Identify Hash\n")
    ch = int(input("Enter Your Choice\n>>> "))
    match ch:
        case 1:
            from hashbody.hashgenbody import hashgen
            hashgen()
            
        case 2:
            import hashbody.hashdownbody
            st = input("\nEnter the hash:\n")
            print("\nPossible Hash Types:")
            hashbody.hashdownbody.body(st)
            

