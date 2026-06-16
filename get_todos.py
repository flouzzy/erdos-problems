import os
import sys

def main():
    target_files = []
    for root, _, files in os.walk('.'):
        if '.git' in root or '.lake' in root:
            continue
        for file in files:
            if file.endswith('.md') or file.endswith('.tex') or file.endswith('.py'):
                target_files.append(os.path.join(root, file))

    for filepath in target_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                for i, line in enumerate(lines):
                    # Check for lean sorry. Only consider lines that look like code or comments
                    if 'sorry' in line:
                        # Make sure it's not a python string or just a plain word
                        if filepath.endswith('.py') and "sorry" in line and not "print" in line:
                            if "line" in line or "#" in line or "description" in line:
                                continue
                            # Context
                            start = max(0, i - 10)
                            end = min(len(lines), i + 11)
                            context = "".join(lines[start:end])

                            description = "Not inferrable"
                            if '--' in line:
                                description = line.split('--')[-1].strip()
                            print(f"{filepath}:{i+1}: {description}")
                        elif not filepath.endswith('.py'):
                            description = "Not inferrable"
                            if '--' in line:
                                description = line.split('--')[-1].strip()
                            print(f"{filepath}:{i+1}: {description}")
        except Exception as e:
            pass

if __name__ == "__main__":
    main()
