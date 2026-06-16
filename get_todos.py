import os
import json

def get_todos():
    target_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md') or file.endswith('.tex') or file.endswith('.py'):
                target_files.append(os.path.join(root, file))

    todos = []
    for filepath in target_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                for i, line in enumerate(lines):
                    # Check for lean sorry. Only consider lines that look like code or comments
                    if 'sorry' in line:
                        # Skip if it's in the get_todos.py script itself or python string literals
                        if "if 'sorry' in line:" in line or "if \"sorry\" in line" in line or "if filepath.endswith('.py') and \"sorry\" in line:" in line:
                            continue

                        # Only consider lines that look like code or comments
                        # Exclude cases where sorry is part of a markdown text or normal prose (unless it's a code block)
                        # We specifically want Lean code where `sorry` indicates a proof stub.

                        # Context
                        start = max(0, i - 10)
                        end = min(len(lines), i + 11)
                        context = "".join(lines[start:end])

                        description = "Not inferrable"
                        if '--' in line:
                            parts = line.split('--', 1)
                            if len(parts) > 1:
                                desc = parts[1].strip()
                                if desc:
                                    description = desc

                        todos.append({
                            'file': f"{filepath}:{i+1}",
                            'description': description,
                            'context': context
                        })
        except Exception as e:
            pass

    return todos

if __name__ == '__main__':
    todos = get_todos()
    print(json.dumps(todos, indent=2))
