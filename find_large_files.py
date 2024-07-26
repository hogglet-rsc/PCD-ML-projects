import os
import heapq

def find_large_files(base_dir, min_size_mb=1, top_n=20):
    large_files = []
    min_size_bytes = min_size_mb * 1024 * 1024
    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size >= min_size_bytes:
                    heapq.heappush(large_files, (-file_size, file_path))
                    if len(large_files) > top_n:
                        heapq.heappop(large_files)
            except OSError:
                continue
    
    return [(-size, path) for size, path in sorted(large_files)]

base_directory = "/home/shogg/RBHT projects github"

print(f"Files larger than 1MB (up to 20 files):")
for size, path in find_large_files(base_directory):
    print(f"{size/1024/1024:.2f} MB: {path}")