import os

def main():
    target_files = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ('.git', '.lake')]
        for file in files:
            if file.endswith('.md') or file.endswith('.tex') or file.endswith('.py'):
                target_files.append(os.path.join(root, file))

    for filepath in target_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    # Check for lean sorry. Only consider lines that look like code or comments
                    if 'sorry' in line:
                        # Make sure it's not a python string or just a plain word
                        if filepath.endswith('.py') and "sorry" in line and not "print" in line:
                            if "line" in line or "#" in line or "description" in line:
                                continue

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
            print(f"Error processing {filepath}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
