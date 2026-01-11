import os
from PIL import Image


def extract_first_frames_numbered(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".png")]

    files.sort()

    for i, filename in enumerate(files, start=1):
        input_path = os.path.join(input_folder, filename)

        output_filename = f"{i:03d}.png"
        output_path = os.path.join(output_folder, output_filename)

        try:
            with Image.open(input_path) as img:
                img.save(output_path)
            print(f"[완료] {filename} -> {output_filename}")

        except Exception as e:
            print(f"[실패] {filename}: {e}")


input_dir = "./apng_files"
output_dir = "./output_frames"

extract_first_frames_numbered(input_dir, output_dir)
