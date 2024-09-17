import os
import subprocess
from app.halper import Halper
from app.create import Create

class Git:
    """
    A class for Git operations.
    """

    def after_clone(url):
        """
        Perform actions after cloning a repository.

        Args:
            url (str): The URL of the repository.
        """
        Create.gitignore()
        Create.readme(url)
        Create.contribution()
        Create.license()
        Create.vscode()
        
    def clone(url):
        """
        Clone a Git repository.

        Args:
            url (str): The URL of the repository.

        Returns:
            str: A message indicating the success or failure of the cloning process.
        """
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
        """
        Pull changes from the remote repository.
        """
        from main import main
        try:
            # Add all files to git
            subprocess.run(["git", "pull"], check=True)
            return main(f"Successfully pulled.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return main(f"'git pull' failed")

    def add():
        """
        Add all files to the staging area.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Add all files to git
            subprocess.run(["git", "add", "."], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def addfile(text):
        """
                Add a specified to the staging area.

                Returns:
                    bool: True if successful, False otherwise.
        """
        try:
            # Add all files to git
            subprocess.run(["git", "add", text], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def commit(text):
        """
        Commit changes with a specified message.

        Args:
            text (str): The commit message.

        Returns:
            bool: True if successful, False otherwise.
        """
        text = Halper.capitalize_first_letter(text)
        try:
            # Commit changes
            subprocess.run(["git", "commit", "-m", text], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def addcommit(text):
        """
        The git commit -am function that adds files and commits, eliminating the need for git add then git commit.

        Args:
            text (str): The commit message.

        Returns:
            bool: True if successful, False otherwise.
        """
        text = Halper.capitalize_first_letter(text)
        try:
            # Add files then commit
            subprocess.run(["git", "commit", "-am", text], check=True)
            return True
        except subprocess.CalledProcessError as err:
            print(f"An error occurred: {err}")
            return False

    def push():
        """
        Push committed changes to the remote repository.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Push changes to remote
            subprocess.run(["git", "push"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return False

    def run(text):
        """
        Perform Git add, commit, and push operations in sequence.

        Args:
            text (str): The commit message.

        Returns:
            str: A message indicating the success or failure of the operations.
        """
        from main import main
        if Git.add() is False:
            return main("'git add .' failed")
        if Git.commit(text) is False:
            return main(f"'git commit -m {text}' failed")
        if Git.push() is False:
            return main("'git push' failed")

        return main("Successfully added, committed, and pushed changes.")

    def info():
        """
        Display information about the current Git repository.
        """
        # Get the current directory path
        directory_path = os.getcwd()

        # Get the current folder name
        directory_name = os.path.basename(directory_path)

        directory_name = Halper.capitalize_words(directory_name)

        # Print the current folder name
        print("Folder  : ", directory_name)

        # Print the current directory path
        print("Path    : ", directory_path)