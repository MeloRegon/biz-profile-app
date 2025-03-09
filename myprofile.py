"""
MyProfile Business App
A console application for storing and managing business profile information, including tax and banking details.
"""

# Separator for UI formatting
SEPARATOR = '------------------------------------------'

# Dictionary to store user data (personal and business details)
user_data = {}

def main() -> None:
    """
    Main function that runs the menu loop for MyProfile Business APP.
    Allows the user to enter or update information, display saved data, or exit the program.
    """
    while True:
        try:
            print('\nMyProfile Business APP')
            print('Save information about yourself and output it in different formats')
            print(SEPARATOR)
            print('1 - Enter or update information')
            print('2 - Display information')
            print('0 - Exit')

            # Get user choice
            option = int(input('Enter menu option (0, 1 or 2): '))

            # Handle menu selection
            if option == 0:
                print("Exiting the application...")
                break # Exit the loop and terminate the program
            elif option == 1:
                enter_or_update_info() # Call function to input/update information
            elif option == 2:
                display_info() # Call function to display stored information
            else:
                print("Invalid menu option. Please try again.")  # Handle invalid numbers
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")  # Handle non-numeric input


def enter_or_update_info() -> None:
    """
        Handles user input for entering or updating personal and business information.
        Saves validated user data into the global `user_data` dictionary.
    """

    print(SEPARATOR)
    print('1 -Enter or update Personal information')
    print('2 -Enter or update Business Information')
    print('0 - Exit')

    while True:
        try:
            option_enter_or_update = int(input('Enter menu option (0, 1 or 2): '))
            if option_enter_or_update in [0, 1, 2]:
                break
            print("Invalid menu option. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

    data_saved = False # Tracks if any data was successfully entered

    if option_enter_or_update == 0:
        return # Exit the function if the user chooses option 0

    elif option_enter_or_update == 1:
        """Handles input for personal information"""

        # Get user's name (only letters, spaces, or hyphens allowed)
        while True:
            name = input('Enter a name: ')
            if name.replace(" ", "").replace("-", "").isalpha():
                user_data['name'] = name
                break
            else:
                print('The name must contain only letters')

        # Get user's age (must be a number between 1 and 99)
        while True:
            try:
                age = int(input('Enter the age: '))
                if 0 < age < 99:
                    user_data['age'] = age
                    break
                else:
                    print('The age must be positive and less than 100')
            except ValueError:
                print('Invalid input. Please enter a number.')

        # Get user's phone number (must follow the +39XXXXXXXXXX format)
        while True:
            user_number = input('Enter the phone number (+39XXXXXXXXXX): ').strip()
            user_phone_number = ''.join(ch for ch in user_number if ch == '+' or ch.isdigit())

            if user_phone_number.startswith("+39") and len(user_phone_number) == 13:
                user_data['phone_number'] = user_phone_number
                break
            else:
                print("Invalid phone number. Please enter in the format +39XXXXXXXXXX.")

        # Get user's email (basic format validation)
        while True:
            email_adr = input("Enter your email address: ").strip()

            if "@" in email_adr and "." in email_adr and " " not in email_adr and email_adr.index(
                    "@") < email_adr.rindex("."):
                user_data['email'] = email_adr
                break
            else:
                print("Invalid email format. Please enter a valid email (example@mail.com).")

        # Get user's ZIP code (4-10 characters, numbers and spaces allowed)
        while True:
            zip_code = input("Enter your zip code: ").strip()

            if 4 <= len(zip_code) <= 10 and all(ch.isalnum() or ch == " " for ch in zip_code):
                user_data['zip_code'] = zip_code
                break
            else:
                print("Invalid zip code. Please enter only numbers (4-10 digits).")

        # Get user's mailing address (letters, numbers, spaces, commas, and dots allowed)
        while True:
            mail_address = input("Enter your mailing address (without zip code): ").strip()

            if len(mail_address) > 5 and all(ch.isalnum() or ch in " ,." for ch in mail_address):
                user_data['mail_address'] = mail_address
                break
            else:
                print("Invalid mailing address. Use letters, numbers, spaces, commas, and dots.")

        # Get user's additional information (optional field)
        user_information = input("Enter additional information (optional): ").strip()
        if len(user_information) < 3:
            user_information = "N/A"
        user_data['user_info'] = user_information

        data_saved = True # Mark data as saved

    elif option_enter_or_update == 2:
        """Handles input for business information"""

        # Get user's VAT Number (must be exactly 15 digits)
        while True:
            vat_number = input('Enter your VAT Number (15 digits): ').strip()
            if len(vat_number) == 15 and vat_number.replace(" ", "").isalnum():
                user_data['vat_number'] = vat_number
                break
            else:
                print("Invalid VAT Number. It must contain exactly 15 digits.")

        # Get user's Tax Identification Number (Codice Fiscale / TIN)
        tax_number = input("Enter your Tax Identification Number (Codice Fiscale / TIN): ").strip()
        user_data['tax_number'] = tax_number

        # Get user's IBAN (must be exactly 20 alphanumeric characters)
        while True:
            iban = input("Enter your IBAN (20 characters): ").strip()
            if len(iban) == 20 and iban.isalnum():
                user_data['iban'] = iban
                break
            else:
                print("Invalid IBAN. It must contain exactly 20 alphanumeric characters.")

        # Get user's bank name
        bank_name = input("Enter your Bank Name: ").strip()
        user_data['bank_name'] = bank_name

        # Get user's SWIFT/BIC code (must be 8 or 11 alphanumeric characters)
        while True:
            swift = input("Enter your SWIFT/BIC code (8-11 characters): ").strip()
            if len(swift) in [8, 11] and swift.isalnum():
                user_data['swift'] = swift
                break
            else:
                print("Invalid SWIFT/BIC code. It must be either 8 or 11 alphanumeric characters.")

        data_saved = True # Mark data as saved

    if data_saved:
        print('Saves completed!')


def display_info() -> None:
    """
       Displays stored user information.
       Allows the user to choose between viewing:
       - Personal Information
       - Business Information (along with Personal Information)
       - Exit the menu
    """

    print(SEPARATOR)
    print('1 - Display Personal Information: ')
    print('2 - Display Business and personal Information: ')
    print('0 - Exit')

    # Loop to get valid menu input
    while True:
        try:
            option_display_info = int(input('Enter menu option (0, 1 or 2): '))
            if option_display_info in [0, 1, 2]:
                break
            print("Invalid menu option. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

    # Check if there is any stored data
    if not user_data:
        print("No information available. Please enter data first.")
        return # Exit if no data is available

    # Dictionary for personal information
    personal_info: dict[str, str] = {
        "Name": user_data.get("name", "Not provided"),
        "Age": user_data.get("age", "Not provided"),
        "Phone number": user_data.get("phone_number", "Not provided"),
        "E-mail": user_data.get("email", "Not provided"),
        "ZIP code": user_data.get("zip_code", "Not provided"),
        "Address": user_data.get("mail_address", "Not provided"),
        "Additional information": user_data.get("user_info", "Not provided"),
    }

    # Dictionary for business information
    business_info: dict[str, str] = {
        "VAT Number": user_data.get("vat_number", "Not provided"),
        "Tax Number": user_data.get("tax_number", "Not provided"),
        "IBAN": user_data.get("iban", "Not provided"),
        "Bank Name": user_data.get("bank_name", "Not provided"),
        "SWIFT/BIC": user_data.get("swift", "Not provided"),
    }

    # Exit condition
    if option_display_info == 0:
        return

    # Display personal information
    elif option_display_info == 1:
        for key, value in personal_info.items():
            print(f'{key}: {value}')
        print(f'\n {SEPARATOR}')

    # Display business information if option 2 is selected
    elif option_display_info == 2:
        for key, value in personal_info.items():
            print(f'{key}: {value}')
        for key, value in business_info.items():
            print(f'{key}: {value}')

        print(f'\n {SEPARATOR}')


if __name__ == '__main__':
    main()