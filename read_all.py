def print_file_contents(filename):
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
