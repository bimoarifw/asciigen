import pyfiglet
from termcolor import colored


def create_ascii_logo(color):
    ascii_logo = pyfiglet.figlet_format("ASCIIGEN")
    colored_logo = colored(ascii_logo, color=color)
    return colored_logo


def get_user_input():
    user_text = input("Enter your text: ")
    return user_text


def get_user_color():
    print("Choose a color for the text:")
    print("1. Red")
    print("2. Green")
    print("3. Yellow")
    print("4. Blue")
    print("5. Magenta")
    print("6. Cyan")

    color_choice = input("Enter the number of your chosen color: ")

    colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]

    if color_choice.isdigit() and 1 <= int(color_choice) <= len(colors):
        return colors[int(color_choice) - 1]
    else:
        print("Invalid color choice. Using default color (white).")
        return "white"


def main():
    print(create_ascii_logo("red"))
    print("Created by: bimoarifw")
    print("GitHub: bimoarifw")
    print("\nWelcome to ASCII Art Generator")

    while True:
        user_text = get_user_input()
        user_color = get_user_color()

        ascii_logo = pyfiglet.figlet_format(user_text)
        colored_ascii_logo = colored(ascii_logo, color=user_color)

        print("\nASCII Art:")
        print(colored_ascii_logo)

        continue_prompt = input("Generate another ASCII art? (y/n): ")
        if continue_prompt.lower() != "y":
            break


if __name__ == "__main__":
    main()
