# pdf_toolkit.py
PDF結合・分割・テキスト抽出ツール
# PDF Toolkit

PDFファイルの**結合・分割・テキスト抽出**をコマンドラインから簡単に行えるPythonツールです。

## 機能

| コマンド | 説明 |
|---------|------|
| `merge`   | 複数のPDFファイルを1つのPDFに結合する |
| `split`   | PDFをページ単位で個別ファイルに分割する |
| `extract` | PDF内のテキストを抽出してテキストファイルに保存する |

## 動作環境

- Python 3.10以上
- [pypdf](https://pypi.org/project/pypdf/)

## セットアップ

```bash
pip install pypdf
```

## 使い方

### PDFの結合

```bash
python pdf_toolkit.py merge merged.pdf doc1.pdf doc2.pdf doc3.pdf
```

複数のPDFを指定した順番で1つのファイルにまとめます。

### PDFの分割

```bash
python pdf_toolkit.py split input.pdf output_dir
```

`input.pdf` の各ページを `output_dir/input_page1.pdf`, `input_page2.pdf` ... のように保存します。

### テキスト抽出

```bash
python pdf_toolkit.py extract input.pdf output.txt
```

各ページのテキストをページ番号付きで `output.txt` に書き出します。

## 実行例

```
$ python pdf_toolkit.py merge result.pdf a.pdf b.pdf
[OK] 2 個のファイルを結合しました -> result.pdf

$ python pdf_toolkit.py split result.pdf pages
[OK] 5 ページに分割しました -> pages/

$ python pdf_toolkit.py extract result.pdf result.txt
[OK] 5 ページ分のテキストを抽出しました -> result.txt
```

## 今後の拡張案

- ページの並び替え・回転機能
- パスワード付きPDFへの対応(暗号化・復号)
- GUI版(Tkinter / PyQt)の追加

## ライセンス

MIT License
