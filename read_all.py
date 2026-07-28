import os

files_to_read = [
    "inprogress/04-Erdos-Gyarfas/test_generate_erdos_gyarfas_proof.py",
    "inprogress/04-Erdos-Gyarfas/test_generate_proof.py"
]

for file_path in files_to_read:
    file_name = os.path.basename(file_path)
    with open(file_path, "r") as f:
        print(f"--- {file_name} ---")
        print(f.read())
