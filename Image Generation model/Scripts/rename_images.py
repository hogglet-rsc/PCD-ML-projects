import os

def rename_files(folder, prefix):
    for i, filename in enumerate(os.listdir(folder), 1):
        old_path = os.path.join(folder, filename)
        new_filename = f"{prefix}_{i:04d}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(folder, new_filename)
        os.rename(old_path, new_path)

# Paths
normal_path = "/home/hogglet/Python Projects/RBHT/Images/Disarranged_vs_Normal/Normal"
disarranged_path = "/home/hogglet/Python Projects/RBHT/Images/Disarranged_vs_Normal/Disarranged"

# Rename files
rename_files(normal_path, "Normal")
rename_files(disarranged_path, "Disarranged")

print("Renaming complete.")