# 🧾 PDF Merger Tool (Python)

A simple open source Python script that merges all PDF files in a given folder into a single output file. Built using [`pypdf`](https://pypi.org/project/pypdf/), this tool is useful for quick batch merging of PDFs without needing an external GUI application or website.

## 📁 Folder Structure

<pre> project/
├── merge_pdfs.py
├── pdfs/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
└── pdfs/merged/
    └── merged-pdf.pdf
 </pre>


- Place all PDF files you want to merge inside the `pdfs/` folder.
- The output merged PDF will be saved to `pdfs/merged/merged-pdf.pdf`.

## ▶️ How to Use

1. Install the required library:
   
    `pip install pypdf`

3. Run the script:

    `python merge_pdfs.py`

3. Check the output at:

    `pdfs/merged/merged-pdf.pdf`

🔧 Requirements

    Python 3.6+

    pypdf library

💡 Notes

    The script skips non-PDF files automatically.
