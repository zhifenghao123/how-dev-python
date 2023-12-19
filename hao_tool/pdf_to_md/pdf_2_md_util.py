import os
from pathlib import Path

import aspose.words as aw


def convertPdfToMd(source_pdf_name, target_save_md_file):
    print(source_pdf_name)
    doc = aw.Document(source_pdf_name)
    doc.save(target_save_md_file)


if __name__ == '__main__':
    # project_root = Path(__file__).resolve().parent
    # pdf_file = str(project_root.parent) + "/dataset/第01章_Linux下MySQL的安装与使用.pdf"
    # doc.save(str(project_root.parent) + "/dataset/第01章_Linux下MySQL的安装与使用.md")

    pdf_file = "../dataset/pdf2md/第01章_Linux下MySQL的安装与使用.pdf"
    md_file = "../dataset/pdf2md/第01章_Linux下MySQL的安装与使用.md"
    convertPdfToMd(pdf_file, md_file)
