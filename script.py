import os
from PIL import Image


def extract_target_frames_numbered(input_folder, output_folder, target_index):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"[정보] 출력 폴더를 생성했습니다: {output_folder}")

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".png")]
    files.sort()

    if not files:
        print(f"[주의] '{input_folder}' 폴더에 PNG 파일이 없습니다.")
        return

    print(f"\n총 {len(files)}개의 파일 처리를 시작합니다...\n")

    success_count = 0

    for i, filename in enumerate(files, start=1):
        input_path = os.path.join(input_folder, filename)

        output_filename = f"{i:03d}.png"
        output_path = os.path.join(output_folder, output_filename)

        try:
            with Image.open(input_path) as img:
                extracted_frame = target_index

                try:
                    if target_index > 0:
                        img.seek(target_index)
                except EOFError:
                    img.seek(0)
                    extracted_frame = 0

                img.save(output_path)

                status = (
                    "지정 프레임"
                    if extracted_frame == target_index
                    else "첫번째 프레임(Fallback)"
                )
                print(
                    f"[완료] {filename} -> {output_filename} ({status}, Index: {extracted_frame})"
                )
                success_count += 1

        except Exception as e:
            print(f"[실패] {filename}: {e}")

    print(f"\n작업 종료. 총 {success_count}/{len(files)}개 변환 완료.")


INPUT_DIR = "./apng_files"
OUTPUT_DIR = "./output_frames"

if __name__ == "__main__":
    try:
        user_input = input("추출할 프레임 번호를 입력하세요 (0부터 시작, 예: 2): ")
        target_frame_idx = int(user_input)

        if target_frame_idx < 0:
            print("0 이상의 정수를 입력해야 합니다.")
        else:
            extract_target_frames_numbered(INPUT_DIR, OUTPUT_DIR, target_frame_idx)

    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
