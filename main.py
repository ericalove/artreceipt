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

    def transaction():
        prompt_text = "Start transaction? [Y] or [N] "
        prompt = input(prompt_text)
        while prompt.lower() != "y" and prompt.lower() != "n":
            print(error)
            prompt = input(prompt_text)
        if prompt.lower() == "n":
            print("Thank you for visiting! Stop by again soon. :)")
        elif prompt.lower() == "y":
            def buy_painting():
                painting_prompt_text = "Did you buy a painting? [Y] or [N] "
                painting_prompt = input(painting_prompt_text)
                if painting_prompt.lower() == "y":
                    lg_painting_amount = int(input("How many large paintings? "))
                    sm_painting_amount = int(input("How many small paintings? "))
                while painting_prompt.lower() != "y" and painting_prompt.lower() != "n":
                    print(error)
                    painting_prompt = input(painting_prompt_text)

            buy_painting()

            # print("Large Paintings: " + str(lg_painting_amount))

            def buy_print():
                print_prompt_text = "Did you buy a print? [Y] or [N] "
                print_prompt = input(print_prompt_text)
                if print_prompt.lower() == "y":
                    lg_print_amount = int(input("How many large prints? "))
                    sm_print_amount = int(input("How many small prints? "))
                while print_prompt.lower() != "y" and print_prompt.lower() != "n":
                    print(error)
                    print_prompt = input(print_prompt_text)

            buy_print()

            def buy_postcard():
                postcard_prompt_text = "Did you buy any postcards? [Y] or [N] "
                postcard_prompt = input(postcard_prompt_text)
                if postcard_prompt.lower() == "y":
                    postcard_amount = int(input("How many postcards? "))
                while postcard_prompt.lower() != "y" and postcard_prompt.lower() != "n":
                    print(error)
                    postcard_prompt = input(postcard_prompt_text)

            buy_postcard()

            print("Your receipt: ")
        # else:
        #     print(error)
        #     prompt

    # print("Large Paintings: " + str(lg_painting_amount))
    transaction()


receipt()
