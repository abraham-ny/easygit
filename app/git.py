import os
import subprocess
from app.halper import Halper
from app.create import Create
class Git:

    def after_clone(url):
        Create.gitignore()
        Create.readme(url)
        Create.contribution()
        Create.license()
        Create.vscode()
        
    def clone(url):
        from main import main
        try:
            # Add all files to git
            subprocess.run(["git", "clone", url], check=True)

            name = url.split("/")[-1]
            os.chdir(name)  # Change directory to the cloned repository
            Git.after_clone(url)
            return main(f"{url} Successfully cloned.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during cloning: {e}")
            return main(f"'git clone {url}' failed")
        except FileNotFoundError as e:
            print(f"An error occurred while changing directory: {e}")
            return main(f"Failed to change directory to {name}")

    def pull():
        from main import main
        try:
            # Add all files to git
            subprocess.run(["git", "pull"], check=True)
            return main(f"Successfully pulled.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return main(f"'git pull' failed")

    def add():
        try:
            # Add all files to git
            subprocess.run(["git", "add", "."], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def commit(text):
        text = Halper.capitalize_first_letter(text)
        try:
            # Commit changes
            subprocess.run(["git", "commit", "-m", text], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def push():
        try:
            # Push changes to remote
            subprocess.run(["git", "push"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def run(text):
        from main import main
        if Git.add() is False:
            return main("'git add .' failed")
        if Git.commit(text) is False:
            return main(f"'git commit -m {text}' failed")
        if Git.push() is False:
            return main("'git push' failed")

        return main("Successfully added, committed, and pushed changes.")

    def info():

        # Get the current directory path
        directory_path = os.getcwd()

        # Get the current folder name
        directory_name = os.path.basename(directory_path)

        directory_name = Halper.capitalize_words(directory_name)

        # Print the current folder name
        print("Folder  : ", directory_name)

        # Print the current directory path
        print("Path    : ", directory_path)