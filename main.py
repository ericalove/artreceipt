# CREATE AN ART SALE RECEIPT - selling a large painting, small painting, large print, small print, and postcard
# USE For and While for this as well. Try making the initial error in to a for loop towards a correct y/n entry.

# STORE ADDRESS:
store_name = "THE ART STORE - Fine art, home goods and more!"
store_address_street = "2209 Market Ave, STE. 234"
store_address_city = "Oakland"
store_address_state = "CA"
store_address_zip = "94601"
store_address_phone = "(650) 555-3842"
store_website = "www.theartstoreoakland.biz"
# PRICE GUIDE:
large_painting = 100
small_painting = 60
large_print = 80
small_print = 45
postcard = 5


def receipt():
    error = "INVALID ENTRY: Please try again :)"
    def store_info():
        print(store_name)
        print(store_address_street)
        print(store_address_city + " " + store_address_state + ", " + store_address_zip)
        print(store_address_phone)
        print(store_website)
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
                while painting_prompt.lower() != "y" and painting_prompt.lower() != "n":
                    print(error)
                    painting_prompt = input(painting_prompt_text)
                if painting_prompt.lower() == "y":
                    lg_painting_amount = int(input("How many large paintings? "))
                    sm_painting_amount = int(input("How many small paintings? "))
                    return lg_painting_amount, sm_painting_amount

            painting_result = buy_painting()

            # print("Large Paintings: " + str(lg_painting_amount))

            def buy_print():
                print_prompt_text = "Did you buy a print? [Y] or [N] "
                print_prompt = input(print_prompt_text)
                while print_prompt.lower() != "y" and print_prompt.lower() != "n":
                    print(error)
                    print_prompt = input(print_prompt_text)
                if print_prompt.lower() == "y":
                    lg_print_amount = int(input("How many large prints? "))
                    sm_print_amount = int(input("How many small prints? "))
                    return lg_print_amount, sm_print_amount

            print_result = buy_print()

            def buy_postcard():
                postcard_prompt_text = "Did you buy any postcards? [Y] or [N] "
                postcard_prompt = input(postcard_prompt_text)
                while postcard_prompt.lower() != "y" and postcard_prompt.lower() != "n":
                    print(error)
                    postcard_prompt = input(postcard_prompt_text)
                if postcard_prompt.lower() == "y":
                    postcard_amount = int(input("How many postcards? "))
                    return postcard_amount

            postcard_result = buy_postcard()

            minor_line_break = "-" * 25
            def receipt_body()
                print(painting_result[0])
                print(painting_result[1])
                print(minor_line_break)
                print(print_result[0])
                print(print_result[1])
                print(minor_line_break)
                print(postcard_result)
                print(minor_line_break)
                print("Total: ")

            line_break = "-" * 50

            print("\n")
            store_info()
            print("\nYour receipt: ")
            print(line_break)
            receipt_body()
            print(line_break)
            print("Thank you for visiting! Stop by again soon. :)")
            print(line_break)
        # else:
        #     print(error)
        #     prompt

    # print("Large Paintings: " + str(lg_painting_amount))
    transaction()


receipt()
