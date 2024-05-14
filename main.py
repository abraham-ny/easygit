import os, time, msvcrt
import validators
from app.explorer import Explorer
from app.git import Git

def main(text="Welcome to your EasyGit"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    Git.info()
    print()
    if text != "":
        print(text)
        print()
    print("[1] Git clone")
    print("[2] Git pull")
    print("[3] Git push")
    print("[0] Exit")
    print()

if __name__ == "__main__":
    main()
    while True:
        choice = msvcrt.getch()

        if choice == b'1':
            url = input("Enter remote repository URL : ")
            if not validators.url(url):
                main("Invalid URL")
            else:
                Git.clone(url)
        elif choice == b'2':
            Git.pull()
        elif choice == b'3':
            print("Enter your commit :")
            text = msvcrt.getch()
            if choice == b'0':
                main()
            elif not text:
                text = "Automated commit"
            Git.run(text)

        elif choice == b' ':  # Space key
            main()
        elif choice == b'M':  # Right arrow key
            Explorer.next()
        elif choice == b'K':  # Left arrow key
            Explorer.back()

        elif choice == b'0':
            print("Exiting...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid choice. Please choose again.")