# Document Duplicate Finder

Document Duplicate Finder scans a collection of documents and detects duplicate files.

The demo works with sample document metadata, comparing file sizes and content hashes.

---

## Supported Formats

- PDF
- DOCX
- TXT

---

## Processing

Scan Documents

↓

Calculate Hashes

↓

Compare Sizes

↓

Detect Duplicates

↓

Generate Report

---

## Example

```
Scanning documents...

Documents found : 6

Duplicate groups

contract.pdf
contract_copy.pdf

notes.txt
notes_backup.txt

Summary

Duplicate groups : 2
Unique files : 2
```

Run

```bash
python app.py
```

This demo uses sample data stored in memory.
