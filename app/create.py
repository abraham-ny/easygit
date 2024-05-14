from app.halper import Halper
import os



class Create:

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

    def vscode():
        # Define folder and file names
        folder_name = ".vscode"
        file_name = "settings.json"
        content = '{\n    "git.enabled": false\n}'

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Create the file and write content into it
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            file.write(content)

        return True

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

    def gitignore():
        gitignore_content = """# Ignore IDE directories
/.idea/
/.vscode/

# Ignore Python bytecode files
__pycache__/

# Building
/dist/
/build/

# Ignore another folders & files
/my_data/
/mydata/
*.exe
test.py
test2.py"""
        with open(".gitignore", "w") as file:
            file.write(gitignore_content)

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

    def readme(url):

        name = url.split("/")[-1]
        name = Halper.capitalize_words(name)

        organization = url.split("/")[-2]
        repository = url.split("/")[-1]
        

        content = f"""# {name}

This repository helps you ..

![](image.gif)

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

1. Clone the repository or download it:

   ```shell
   git clone https://github.com/{organization}/{repository}
   ```

2. Navigate to the project directory:

   ```shell
   cd {repository}
   ```

3. Run `main.py`

   ```shell
   python main.py
   ```

## How to Use:

### 1. First instruction

Lorem Ipsum is simply **dummy** text of the printing and typesetting industry.

### 2. Second instruction

It is a long established fact that a reader will be distracted. [Here's a simple explanation](https://www.youtube.com).

### 3. Maximize Your Productivity

## Getting Help

If you have any questions or need assistance, feel free to [open an issue](https://github.com/{organization}/{repository}/issues).

## Contributing

If you have an idea for a new feature or want to improve existing ones, check out [contributing.md](CONTRIBUTING.md) for more information.

## Support

If you find this project helpful, show your support by starring the repository.

## Sources

- [source_name](source_url).
- [source_name](source_url)."""

        # Write content to README.md file
        with open("README.md", "w") as file:
            file.write(content)

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

    def contribution():
        gitignore_content = """# Contribution Guidelines

Before contributing to this repository, please ensure you are adhering to the following general guidelines. Further, if you are submitting a new feature to the repository, be sure you are also following the feature-specific guidelines. These checks will ensure that your contributions can be easily integrated into the main repository, without any headache for the owners.

## General Guidelines

The following guidelines should be followed when making any open-source contributions:

- [ ] Contributions should be made via a pull request to the main repository from a personal fork.
- [ ] Pull requests should be accompanied by a descriptive title and detailed explanation.
- [ ] Submit all pull requests to the repository's main branch.
- [ ] Before submitting a pull request, ensure additions/edits are aligned with the overall repo organization.
- [ ] Be sure changes are compatible with the repository's license.
- [ ] In case of conflicts, provide helpful explanations regarding your proposed changes so that they can be approved by repo owners."""

        with open("CONTRIBUTING.md", "w") as file:
            file.write(gitignore_content)

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

    def license():
        gitignore_content = """Copyright (c) 2012-2024 Scott Chacon and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

        with open("LICENSE", "w") as file:
            file.write(gitignore_content)