"""
PDF Toolkit
-----------
PDFファイルの結合・分割・テキスト抽出を行うコマンドラインツール。

使い方:
    python pdf_toolkit.py merge output.pdf input1.pdf input2.pdf ...
    python pdf_toolkit.py split input.pdf output_dir
    python pdf_toolkit.py extract input.pdf output.txt
"""

import sys
import os
from pypdf import PdfReader, PdfWriter


def merge_pdfs(output_path: str, input_paths: list[str]) -> None:
    """複数のPDFファイルを1つに結合する"""
    writer = PdfWriter()

    for path in input_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"ファイルが見つかりません: {path}")
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"[OK] {len(input_paths)} 個のファイルを結合しました -> {output_path}")


def split_pdf(input_path: str, output_dir: str) -> None:
    """PDFをページ単位で分割する"""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"ファイルが見つかりません: {input_path}")

    os.makedirs(output_dir, exist_ok=True)
    reader = PdfReader(input_path)

    base_name = os.path.splitext(os.path.basename(input_path))[0]

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = os.path.join(output_dir, f"{base_name}_page{i}.pdf")
        with open(out_path, "wb") as f:
            writer.write(f)

    print(f"[OK] {len(reader.pages)} ページに分割しました -> {output_dir}/")


def extract_text(input_path: str, output_path: str) -> None:
    """PDFからテキストを抽出してテキストファイルに保存する"""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"ファイルが見つかりません: {input_path}")

    reader = PdfReader(input_path)
    text_chunks = []

    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text_chunks.append(f"--- Page {i} ---\n{text}\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(text_chunks))

    print(f"[OK] {len(reader.pages)} ページ分のテキストを抽出しました -> {output_path}")


def print_usage() -> None:
    print(__doc__)


def main() -> None:
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "merge":
            if len(sys.argv) < 4:
                print("merge には出力ファイルと2つ以上の入力ファイルが必要です")
                sys.exit(1)
            output_path = sys.argv[2]
            input_paths = sys.argv[3:]
            merge_pdfs(output_path, input_paths)

        elif command == "split":
            if len(sys.argv) != 4:
                print("split には input.pdf と output_dir が必要です")
                sys.exit(1)
            split_pdf(sys.argv[2], sys.argv[3])

        elif command == "extract":
            if len(sys.argv) != 4:
                print("extract には input.pdf と output.txt が必要です")
                sys.exit(1)
            extract_text(sys.argv[2], sys.argv[3])

        else:
            print(f"不明なコマンドです: {command}")
            print_usage()
            sys.exit(1)

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
