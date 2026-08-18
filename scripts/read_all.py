import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def print_file_contents(filename):
    resolved_path = os.path.realpath(filename)
    if os.path.commonpath([BASE_DIR, resolved_path]) != BASE_DIR:
        print("Access denied")
        return False

    try:
        with open(filename, "r") as f:
            print(f"--- {filename.split('/')[-1]} ---")
            print(f.read())
            return True
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False

def main():
    print_file_contents("inprogress/04-Erdos-Gyarfas/test_generate_erdos_gyarfas_proof.py")
    print_file_contents("inprogress/04-Erdos-Gyarfas/test_generate_proof.py")

if __name__ == "__main__":
    main()
