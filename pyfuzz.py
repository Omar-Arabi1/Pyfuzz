import os
import typer

pyfuzz = typer.Typer()

def ishidden(check_hidden: str, showhidden: bool):
    if showhidden:
        print(check_hidden)
    else:
        if not check_hidden.startswith("."):
            print(check_hidden)

def list_dir(list_to_loop, part_of_name, showhidden):
    for i in list_to_loop:
        if "_" in i:
            file_split = i.split("_")              
            if part_of_name in file_split[0].lower():
                ishidden(i, showhidden)
        else:
            if part_of_name in i.lower():
                ishidden(i, showhidden)

@pyfuzz.command()
def search(file_name: str, current_dir: str = os.getcwd(), folders: bool = False, both: bool = False, show_hidden: bool = False):
    if file_name.startswith(".") and not show_hidden:
        print("Invalid name because it starts with '.' use --hidden to search through hidden directories")
        return
    
    files = []
    directories = []
    all = []
    
    for item in os.listdir(current_dir):
        if both:
            all.append(item)
        elif os.path.isfile(os.path.join(current_dir, item)):
            files.append(os.path.join(current_dir, item))
        elif os.path.isdir(os.path.join(current_dir, item)):
            directories.append(item)

    if not folders and not both:
        list_dir(files, file_name, show_hidden)
    elif folders and not both:
        list_dir(directories, file_name, show_hidden)
    elif both:
        list_dir(all, file_name, show_hidden)

if __name__ == "__main__":
    pyfuzz()