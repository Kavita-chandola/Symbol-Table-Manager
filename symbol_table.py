class SymbolTable:
    def __init__(self):
        # Python dictionary acts as our Hash Table
        self.table = {}

    def insert(self, name, symbol_type, scope):
        if name in self.table:
            print(f"Error: Symbol '{name}' already exists.")
        else:
            self.table[name] = {'type': symbol_type, 'scope': scope}
            print(f"Successfully inserted: {name}")

    def lookup(self, name):
        if name in self.table:
            details = self.table[name]
            print(f"Found -> Name: {name}, Type: {details['type']}, Scope: {details['scope']}")
        else:
            print(f"Error: Symbol '{name}' not found.")

    def display(self):
        if not self.table:
            print("\nSymbol Table is empty.")
            return
        
        print("\n--- SYMBOL TABLE ---")
        print(f"{'Name':<15} {'Type':<15} {'Scope':<10}")
        print("-" * 40)
        for name, details in self.table.items():
            print(f"{name:<15} {details['type']:<15} {details['scope']:<10}")
        print("-" * 40)