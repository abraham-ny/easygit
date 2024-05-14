import os
class Explorer:

    def display_folders():
        folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
        for i, folder in enumerate(folders, 1):
            print(f"[{i}] {folder}")
        return folders

    def change_directory(selected_folder, folders):
        from main import main
        try:
            folder_index = int(selected_folder)
            if 1 <= folder_index <= len(folders):
                os.chdir(folders[folder_index - 1])
                main(f"Changed directory to '{folders[folder_index - 1]}'")
            else:
                main("Invalid selection. Please choose a valid number.")
        except ValueError:
            main("Invalid input. Please enter a number.")

    def back():
        os.system('cls' if os.name == 'nt' else 'clear')
        from main import main
        current_dir = os.path.abspath(os.curdir)
        parent_dir = os.path.dirname(current_dir)
        os.chdir(parent_dir)
        main(f"Returned to '{parent_dir}'")

    def next():
        os.system('cls' if os.name == 'nt' else 'clear')
        folders = Explorer.display_folders()
        print()
        selected_folder = input("Enter the folder number  : ")

        # Change directory based on user input
        Explorer.change_directory(selected_folder, folders)