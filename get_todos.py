import os
import re

def get_git_info():
    try:
        account = 'flouzzy'
        project = 'erdos-problems'
        return account, project, 'HEAD'
    except:
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
            if file.endswith('.tex') or file.endswith('.py') or file.endswith('.md'):
                target_files.append(os.path.join(root, file))

    for filepath in target_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if lean_sorry_pattern.search(line):
                    # We print them directly
                    print(f"{filepath}:{i+1}: {line.strip()}")
        except Exception as e:
            pass

if __name__ == '__main__':
    main()
