import os, time
import validators
from git import Git

def main(text=""):
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

        choice = input("Enter your choice: ")

        if choice == "1":
            url = input("Enter remote repository URL : ")
            if not validators.url(url):
                main("Invalid URL")
            else:
                Git.clone(url)
        elif choice == "2":
            Git.pull()
        elif choice == "3":
            text = input("Enter your commit : ")
            if not text:
                text = "Automated commit"
            Git.run(text)
        elif choice == "0":
            print("Exiting...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid choice. Please choose again.")