# CREATE AN ART SALE RECEIPT - selling a large painting, small painting, large print, small print, and postcard
# USE For and While for this as well. Try making the initial error in to a for loop towards a correct y/n entry.

# PRICE GUIDE:
large_painting = 100
small_painting = 60
large_print = 80
small_print = 45
postcard = 5
def receipt():
    error = "INVALID ENTRY: Please try again :)"
    transaction = input("Start transaction? [Y] or [N] ")
    if transaction.lower() == "n":
        print("Thank you for visiting! Stop by again soon. :)")
    elif transaction.lower() == "y":
        def buy_painting():
            painting_prompt = input("Did you buy a painting? [Y] or [N] ")
            if painting_prompt.lower() == "y":
                lg_painting_amount = int(input("How many large paintings? "))
                sm_painting_amount = int(input("How many small paintings? "))
            elif painting_prompt.lower() != "y" and painting_prompt.lower() != "n":
                print(error)

        buy_painting()

        def buy_print():
            print_prompt = input("Did you buy a print? [Y] or [N] ")
            if print_prompt.lower() == "y":
                lg_print_amount = int(input("How many large prints? "))
                sm_print_amount = int(input("How many small prints? "))
            elif print_prompt.lower() != "y" and print_prompt.lower() != "n":
                print(error)

        buy_print()

        def buy_postcard():
            postcard_prompt = input("Did you buy any postcards? [Y] or [N] ")
            if postcard_prompt.lower() == "y":
                postcard_amount = int(input("How many postcards? "))
            elif postcard_prompt.lower() != "y" and postcard_prompt.lower() != "n":
                print(error)

        buy_postcard()
    else:
        print(error)


receipt()
