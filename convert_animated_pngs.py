from pathlib import Path

from PIL import Image, ImageSequence


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "animated_png"
OUTPUT_DIR = ROOT / "images"


def convert_png_to_gif(source_path: Path, output_path: Path) -> None:
    with Image.open(source_path) as image:
        frames = []
        durations = []

        for frame in ImageSequence.Iterator(image):
            frames.append(frame.convert("RGBA"))
            durations.append(
                frame.info.get("duration", image.info.get("duration", 100))
            )

        frames[0].save(
            output_path,
            format="GIF",
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=image.info.get("loop", 0),
            disposal=2,
        )


def main() -> None:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    png_paths = sorted(
        path
        for path in SOURCE_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() == ".png"
    )

    if not png_paths:
        print(f"No PNG files found in {SOURCE_DIR.relative_to(ROOT)}.")
        return

    for source_path in png_paths:
        relative_path = source_path.relative_to(SOURCE_DIR)
        output_path = (OUTPUT_DIR / relative_path).with_suffix(".gif")

        if output_path.exists():
            print(f"Skipping {relative_path}: GIF already exists.")
            continue

        output_path.parent.mkdir(parents=True, exist_ok=True)
        convert_png_to_gif(source_path, output_path)
        print(f"Converted {relative_path} to {output_path.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
