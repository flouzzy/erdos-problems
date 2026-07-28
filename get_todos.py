import os
import sys
import concurrent.futures


def process_file(filepath):
    results = []
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if 'sorry' not in line:
                    continue
                if filepath.endswith('.py') and any(
                    word in line for word in ["print", "line",
                                              "#", "description"]
                ):
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
            if file.endswith(('.md', '.tex', '.py')):
                target_files.append(os.path.join(root, file))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for results, errors in executor.map(process_file, target_files):
            for result in results:
                print(result)
            for error in errors:
                print(error, file=sys.stderr)


if __name__ == "__main__":
    main()
