import os
import sys
import concurrent.futures

def process_file(filepath):
    results = []
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                # Check for lean sorry. Only consider lines that look like code or comments
                if 'sorry' in line:
                    # If it's a python file, filter out common python usages of the word "sorry"
                    if filepath.endswith('.py'):
                        if "print" in line or "line" in line or "#" in line or "description" in line:
                            continue

                    description = "Not inferrable"
                    if '--' in line:
                        description = line.split('--')[-1].strip()
                    results.append(f"{filepath}:{i+1}: {description}")
    except Exception as e:
        errors.append(f"Error processing {filepath}: {e}")
    return results, errors

def main():
    target_files = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in {'.git', '.lake'}]
        for file in files:
            if file.endswith('.md') or file.endswith('.tex') or file.endswith('.py'):
                target_files.append(os.path.join(root, file))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for results, errors in executor.map(process_file, target_files):
            for result in results:
                print(result)
            for error in errors:
                print(error, file=sys.stderr)

if __name__ == "__main__":
    main()
