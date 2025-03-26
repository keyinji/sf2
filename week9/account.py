accounts_dict = {}
with open('accounts.txt', 'r') as file:
    for line in file:
        parts = line.split()
        account_number = int(parts[0])
        last_name = parts[1]
        balance = float(parts[2])  
        accounts_dict[account_number] = {last_name: balance}
print(accounts_dict)