from symbol_table import SymbolTable

def main():
    st = SymbolTable()
    
    while True:
        print("\n1. Insert Symbol")
        print("2. Lookup Symbol")
        print("3. Display Table")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            name = input("Enter Name: ")
            symbol_type = input("Enter Type (e.g., int, float, func): ")
            scope = input("Enter Scope (e.g., Global, Local): ")
            st.insert(name, symbol_type, scope)
        
        elif choice == '2':
            name = input("Enter Name to search: ")
            st.lookup(name)
            
        elif choice == '3':
            st.display()
            
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()