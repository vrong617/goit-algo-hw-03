import os
import shutil
import sys

def recursive_copy_and_sort(src_dir, dst_dir='dist'):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                recursive_copy_and_sort(src_path, dst_dir)
            else:
                file_ext = os.path.splitext(item)[1][1:].lower()
                if file_ext:
                    ext_dir = os.path.join(dst_dir, file_ext)

                    if not os.path.exists(ext_dir):
                        os.makedirs(ext_dir)

                    shutil.copy2(src_path, ext_dir)
                    print(f"Copied {item} to {ext_dir}")
                else:
                    print(f"Skipping file without extension: {item}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        sys.exit(1)

    recursive_copy_and_sort(src_dir, dst_dir)
    print(f"Files copied and sorted into {dst_dir}")

if __name__ == "__main__":
    main()
