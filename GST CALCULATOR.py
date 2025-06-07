def gst_calculator():
    while True:
        print("\nGST Calculator")
        print("1. GST Exclusive (Add GST to base price)")
        print("2. GST Inclusive (Extract GST from total price)")
        print("3. Exit")

        choice = input("Choose option (1-3): ")

        if choice == '1':
            try:
                base_price = float(input("Enter base price (excluding GST): ₹"))
                gst_rate = float(input("Enter GST rate (%): "))
                gst_amount = base_price * gst_rate / 100
                final_price = base_price + gst_amount
                print(f"\nGST Amount: ₹{gst_amount:.2f}")
                print(f"Total Price (including GST): ₹{final_price:.2f}")
            except ValueError:
                print("Please enter valid numbers!")

        elif choice == '2':
            try:
                total_price = float(input("Enter total price (including GST): ₹"))
                gst_rate = float(input("Enter GST rate (%): "))
                base_price = total_price * 100 / (100 + gst_rate)
                gst_amount = total_price - base_price
                print(f"\nBase Price (excluding GST): ₹{base_price:.2f}")
                print(f"GST Amount: ₹{gst_amount:.2f}")
            except ValueError:
                print("Please enter valid numbers!")

        elif choice == '3':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# Run the calculator
gst_calculator()