# Symbol-Table-Manager

An interactive, dark-themed web application simulating the **Lexical Analysis Phase** of a compiler. Built using Python, Streamlit, and Pandas, this tool processes C-style source code to extract tokens, manage active scopes, generate mock physical memory pointers, and flags compilation semantic errors (like variable redeclarations) on the fly.

Developed as part of the **Compiler Design Lab (TCS 601)** curriculum.

---

## 🌟 Key Features

* **🖮 Dual Input Methods:** Write/edit C-style code directly in a real-time dark-mode text editor, or drag-and-drop structural `.c` or `.txt` source files.
* **🧠 Dynamic Scope Tracking:** Implements an algorithmic tracking engine that deep-scans structural curly braces `{ }` to differentiate between `Global` and `Local (Level X)` token lifespans.
* **🎫 Duplication & Shadowing Validation:** Identifies duplicate variable declarations within the same scope block and flags them instantly with high-visibility warnings, while properly allowing legal variable shadowing across nested scopes.
* **✂️ Tokenizer Engine:** Scans, strips out code comments (`//`), and tokenizes input into Keywords, Identifiers, Operators, Punctuators, and Constants using strict regular expression (`re`) boundary parsing rules.
* **⚡ Memory Pointer Emulation:** Simulates hardware slot allocations by transforming Python internal object references into truncated 8-character Hexadecimal pointers (`0x1A2B3C`).
* **📊 Analytics Sidebar:** Tracks project runtime metrics including total extracted symbols and high-priority duplicate errors.

---

## 🛠️ Tech Stack

* **Frontend Dashboard:** [Streamlit](https://streamlit.io/) (Python Web Application Framework)
* **Data Structuring:** [Pandas](https://pandas.pydata.org/) (DataFrames & Tabular Visualization)
* **Token Extraction Engine:** Python Native `re` Module (Regular Expressions)

---

## 🚀 Quick Start & Installation

Ensure you have Python 3.10+ installed on your local machine, then follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/symbol-table-manager.git](https://github.com/YOUR_USERNAME/symbol-table-manager.git)
cd symbol-table-manager
