import os

def get_git_repo_name():
    current_path = os.path.abspath(os.getcwd())
    while current_path != os.path.dirname(current_path):
        if '.git' in os.listdir(current_path):
            return os.path.basename(current_path)
        current_path = os.path.dirname(current_path)
    return "Git repo not found"

def list_all_files(root_dir):
    files_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            files_list.append(os.path.relpath(os.path.join(root, file), root_dir))
    return files_list

if __name__ == "__main__":
    repo_name = get_git_repo_name()
    print(f"Hello, Nata! The git repo name is: {repo_name}")
    print("Files in the project:")
    project_root = os.path.abspath(os.getcwd())
    while project_root != os.path.dirname(project_root):
        if '.git' in os.listdir(project_root):
            break
        project_root = os.path.dirname(project_root)
    for file in list_all_files(project_root):
        print(file)