import os
import re

def get_git_info():
    return 'flouzzy', 'erdos-problems', 'HEAD'

def main():
    account, project, hash_val = get_git_info()

    todos = []

    # We found `sorry` in lean code blocks in these files.
    # We will report them as TODOs since they function exactly like them in this context.
    # The lean 4 code has `-- sorry -- Preuve par ...` which are comments and markers.
    # Even `sorry` on its own in lean means "this is unfinished, a TODO".

    lean_sorry_pattern = re.compile(r'sorry\b')

    # Files to parse for lean `sorry` markers
    target_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.md') or file.endswith('.tex') or file.endswith('.py'):
                if file == 'get_todos.py':
                    continue
                file_path = os.path.join(root, file)

                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f):
                        if lean_sorry_pattern.search(line):
                            path = os.path.relpath(file_path, '.')
                            # GitHub URL format: https://github.com/account/project/blob/hash_val/path#Lline
                            url = f"https://github.com/{account}/{project}/blob/{hash_val}/{path}#L{i+1}"
                            todos.append(f"{path}:{i+1} - {line.strip()} - {url}")

    for todo in todos:
        print(todo)

if __name__ == '__main__':
    main()
