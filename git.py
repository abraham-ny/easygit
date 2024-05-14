import os
import subprocess

class Git:

    def create_gitignore_file():
        gitignore_content = """# Ignore IDE directories
/.idea/
/.vscode/

# Ignore Python bytecode files
__pycache__/

# Ignore executable files
*.exe
    """
        with open(".gitignore", "w") as file:
            file.write(gitignore_content)

    def create_readme(name):

        name = Git.capitalize_words(name)

        content = f"""# {name}

## description

## Getting Help

If you have any questions or need assistance, feel free to [open an issue](https://github.com/pycorer/easypush/issues).

## Support

If you find this project helpful, show your support by starring the repository."""

        # Write content to README.md file
        with open("README.md", "w") as file:
            file.write(content)

    def after_clone(name):
        Git.create_readme(name)
        Git.create_gitignore_file()



    def clone(url):
        from main import main
        try:
            # Add all files to git
            subprocess.run(["git", "clone", url], check=True)

            name = url.split("/")[-1]
            os.chdir(name)  # Change directory to the cloned repository
            Git.after_clone(name)
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

    def capitalize_words(sentence):
        # Split the sentence into words
        words = sentence.split()
        
        # Capitalize the first letter of each word
        capitalized_words = [word.capitalize() for word in words]
        
        # Join the capitalized words back into a sentence
        capitalized_sentence = ' '.join(capitalized_words)
        
        return capitalized_sentence

    def info():

        # Get the current directory path
        directory_path = os.getcwd()

        # Get the current folder name
        directory_name = os.path.basename(directory_path)

        directory_name = Git.capitalize_words(directory_name)

        # Print the current folder name
        print("Project : ", directory_name)

        # Print the current directory path
        print("Path    : ", directory_path)

        print()