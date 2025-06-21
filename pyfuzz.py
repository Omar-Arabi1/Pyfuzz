import os
import typer

pyfuzz = typer.Typer()

def list_dir(list_to_loop, part_of_name):
    for i in list_to_loop:
        if "_" in i:
            file_split = i.split("_")
            if part_of_name in file_split[0].lower():
                print(i)
        else:
            if part_of_name in i.lower():
                print(i)

@pyfuzz.command()
def search(file_name: str, current_dir: str = os.getcwd(), folders: bool = False, both: bool = False):
    if file_name.startswith("."):
        print("Invalid name because it starts with '.' use --hidden to search through hidden directories")
        return
    
    files = []
    directories = []
    
    for item in os.listdir(current_dir):
        if os.path.isfile(item):
            files.append(item)
        elif os.path.isdir(item):
            directories.append(item)
    

    if not folders and not both:
        list_dir(files, file_name)
    elif folders and not both:
        list_dir(directories, file_name)
    elif both:
        for i in os.listdir(current_dir):
            if "_" in i:
                file_split = i.split("_")
                if file_name in file_split[0].lower():
                    print(i)
            else:
                if file_name in i.lower():
                    print(i)


if __name__ == "__main__":
    pyfuzz()