import os


def rename_result(dir_path: str, new_filename: str) -> list[str]:
    mp4_files = [f for f in os.listdir(dir_path) if (f.lower().endswith('.mp4') and not f.lower().startswith('video_fragment'))]

    if not mp4_files:
        return []

    mp4_files.sort()

    results = []
    for index, filename in enumerate(mp4_files, start=1):
        new_name = f"{new_filename}_{index}.mp4"
        src = os.path.join(dir_path, filename)
        dst = os.path.join(dir_path, new_name)
        os.rename(src, dst)
        results.append(new_name)

    return results
