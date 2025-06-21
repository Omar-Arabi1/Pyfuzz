import os
import typer

pyfuzz = typer.Typer()

def list_dir(list_to_loop, part_of_name, showhidden):
    for i in list_to_loop:
        if "_" in i:
            file_split = i.split("_")              
            if part_of_name in file_split[0].lower():
                if showhidden:  
                    print(i)
                else:
                    if not i.startswith("."):
                        print(i)          
        else:
            if part_of_name in i.lower():
                if showhidden:
                    print(i)
                else:
                    if not i.startswith("."):
                        print(i)

@pyfuzz.command()
def search(file_name: str, current_dir: str = os.getcwd(), folders: bool = False, both: bool = False, show_hidden: bool = False):
    if file_name.startswith("."):
        print("Invalid name because it starts with '.' use --hidden to search through hidden directories")
        return
    
    files = []
    directories = []
    all = []
    
    for item in os.listdir(current_dir):
        if os.path.isfile(item) and not both:
            files.append(item)
        elif os.path.isdir(item) and not both:
            directories.append(item)
        elif both:
            all.append(item)
    

    if not folders and not both:
        list_dir(files, file_name, show_hidden)
    elif folders and not both:
        list_dir(directories, file_name, show_hidden)
    elif both:
        list_dir(all, file_name, show_hidden)

if __name__ == "__main__":
    pyfuzz()