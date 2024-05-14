import os, msvcrt

class Explorer:
    """
    A class for navigating and interacting with folders in the file system.
    """

    def display_folders():
        """
        Display the list of folders in the current directory.

        Returns:
            list: A list of folder names.
        """
        folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
        for i, folder in enumerate(folders, 1):
            print(f"[{i}] {folder}")
        return folders

    def change_directory(selected_folder, folders):
        """
        Change the current working directory to the selected folder.

        Args:
            selected_folder (str): The index of the selected folder.
            folders (list): A list of folder names.

        Returns:
            None
        """
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
        """
        Navigate to the parent directory.

        Returns:
            None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        from main import main
        current_dir = os.path.abspath(os.curdir)
        parent_dir = os.path.dirname(current_dir)
        os.chdir(parent_dir)
        main(f"Returned to '{parent_dir}'")

    def next():
        """
        Display the next level of folders or navigate to a selected folder.

        Returns:
            None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        folders = Explorer.display_folders()
        print()
        if len(folders) == 1:  # If there's only one folder, change to it directly
            Explorer.change_directory("1", folders)
        else:
            print("Enter the folder number or press '0' to return to main:")
            selected_folder = None
            while True:
                char = msvcrt.getch()
                if char == b'0':  # Left arrow key
                    from main import main
                    main()
                    break
                elif char.isdigit():
                    selected_folder = char.decode('utf-8')
                    break
                else:
                    print("Invalid input. Please enter a number or '0'.")
            
            if selected_folder is not None:
                Explorer.change_directory(selected_folder, folders)