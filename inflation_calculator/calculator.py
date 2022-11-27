def formatted_input(text, err):
    while True:
        try:
            response = float(input(text))
            break
        except:
            print(f"Please enter a valid number for {err}.")

    return response


def prompt_user():
    starting_amount = formatted_input("Amount: ", "amount")
    inflation = formatted_input("Inflation %: ", "inflation percentage") / 100
    percentage = (
        formatted_input(
            "1 = once your money is below 1%\n10 = once your money is below 10%\netc...\nPercentage: ",
            "value percentage",
        )
        / 100
    )

    return starting_amount, inflation, percentage


def calculate():
    starting_amount, inflation, percentage = prompt_user()
    year = 1
    useless = starting_amount * percentage

    while True:
        deduction = starting_amount * inflation
        starting_amount -= deduction

        if starting_amount < useless:
            print(
                f"\nYour money is less than {percentage * 100}% of its original value after {year} years"
            )
            break

        year += 1


if __name__ == "__main__":
    calculate()
