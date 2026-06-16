import os
import re

def get_todos():
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
                target_files.append(os.path.join(root, file))

    for filepath in target_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            in_lean_block = False
            for line_num, line in enumerate(lines, 1):
                stripped = line.strip()

                # Check block start/end
                if filepath.endswith('.md'):
                    if stripped.startswith('```lean'):
                        in_lean_block = True
                    elif stripped.startswith('```') and in_lean_block:
                        in_lean_block = False
                elif filepath.endswith('.tex'):
                    if stripped == r'\begin{verbatim}':
                        in_lean_block = True
                    elif stripped == r'\end{verbatim}':
                        in_lean_block = False
                elif filepath.endswith('.py'):
                    # Python scripts generating lean blocks
                    if r'\begin{verbatim}' in stripped or '```lean' in stripped:
                        in_lean_block = True
                    elif r'\end{verbatim}' in stripped or ('```' in stripped and '```lean' not in stripped and in_lean_block):
                        in_lean_block = False

                if in_lean_block:
                    if lean_sorry_pattern.search(line):
                        todos.append(f"{filepath}:{line_num}: {line.strip()}")
        except Exception as e:
            pass

    return todos

if __name__ == '__main__':
    todos = get_todos()
    for todo in todos:
        print(todo)
