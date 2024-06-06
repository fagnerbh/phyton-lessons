menu = """

[d] Deposit
[w] Withdraw
[t] Transaction History 
[q] Quit

=> """

total_amount = 0
daily_limit = 500
formatted_invoice = ""
withdraw_number = 0
WITHDRAW_LIMIT = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposit = float(input("Enter the value you want to deposit: "))

        if deposit > 0:
            total_amount += deposit
            formatted_invoice += f"Deposit: R$ {deposit:.2f}\n"

        else:
            print("Invalid value for the deposit operation.")

    elif opcao == "w":
        withdraw = float(input("Enter the value to withdraw: "))

        if withdraw > total_amount:
            print("There is not enough amount in your account for this withdraw value.")

        elif withdraw > daily_limit:
            print("The daily withdraw value limit exceeded.")

        elif withdraw_number >= WITHDRAW_LIMIT:
            print("The number of daily withdraw permited exceeded.")

        elif withdraw > 0:
            total_amount -= withdraw
            formatted_invoice += f"Withdraw: R$ {withdraw:.2f}\n"
            withdraw_number += 1

        else:
            print("Invalid value.")

    elif opcao == "t":
        print("\n================ Transaction History ================")
        print("There is no Transaction History." if not formatted_invoice else formatted_invoice)
        print(f"\nTotal Amount: R$ {total_amount:.2f}")
        print("=======================================================")

    elif opcao == "q":
        break

    else:
        print("Invalid Operation. Please enter one the options from the given menu.")