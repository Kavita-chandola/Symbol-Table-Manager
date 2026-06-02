import streamlit as st
import re
import pandas as pd

# Page setup for a professional look
st.set_page_config(layout="wide", page_title="Advanced Symbol Table Pro")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextArea textarea { 
        font-family: 'Courier New', Courier, monospace; 
        background-color: #1e1e1e; 
        color: #d4d4d4; 
    }
    .main { 
        background-color: #0e1117; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Symbol Table Manager")
st.subheader("Compiler Design Lab")

col1, col2 = st.columns([1, 1], gap="large")

def analyze_code_pro(code):
    symbols = []
    seen = set()
    scope_level = 0

    # Keywords
    keywords = [
        'int', 'float', 'char', 'double', 'void',
        'if', 'else', 'for', 'while', 'return',
        'break', 'continue'
    ]

    # Operators
    operators = ['=', '+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=']

    # Punctuators
    punctuators = [';', ',', '(', ')', '{', '}', '[', ']']

    # Identifier declaration pattern
    pattern = r'\b(int|float|char|double|void)\b\s+([a-zA-Z_][a-zA-Z0-9_]*)'

    lines = code.split('\n')

    for i, line in enumerate(lines, 1):

        # Scope tracking
        if '{' in line:
            scope_level += 1
        if '}' in line:
            scope_level -= 1

        # ---------------- KEYWORDS ----------------
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', line):
                symbols.append({
                    "Line": i,
                    "Name": keyword,
                    "Type": "Keyword",
                    "Scope": "-",
                    "Address": "-",
                    "Status": "Success"
                })

        # ---------------- IDENTIFIERS ----------------
        matches = re.findall(pattern, line)

        for match in matches:
            name = match[1]
            data_type = match[0]

            key = (name, scope_level)

            status = "Success"

            if key in seen:
                status = "⚠️ Duplicate Error"

            seen.add(key)

            mem_address = hex(id(name))[:8].upper()

            symbols.append({
                "Line": i,
                "Name": name,
                "Type": f"Identifier ({data_type})",
                "Scope": "Global" if scope_level == 0 else f"Local (Level {scope_level})",
                "Address": f"0x{mem_address}",
                "Status": status
            })

        # ---------------- INTEGER CONSTANTS ----------------
        int_constants = re.findall(r'\b\d+\b', line)

        for const in int_constants:
            symbols.append({
                "Line": i,
                "Name": const,
                "Type": "Integer Constant",
                "Scope": "-",
                "Address": "-",
                "Status": "Success"
            })

        # ---------------- CHARACTER CONSTANTS ----------------
        char_constants = re.findall(r"'.'", line)

        for char_const in char_constants:
            symbols.append({
                "Line": i,
                "Name": char_const,
                "Type": "Character Constant",
                "Scope": "-",
                "Address": "-",
                "Status": "Success"
            })

        # ---------------- OPERATORS ----------------
        for op in operators:
            if op in line:
                symbols.append({
                    "Line": i,
                    "Name": op,
                    "Type": "Operator",
                    "Scope": "-",
                    "Address": "-",
                    "Status": "Success"
                })

        # ---------------- PUNCTUATORS ----------------
        for p in punctuators:
            if p in line:
                symbols.append({
                    "Line": i,
                    "Name": p,
                    "Type": "Punctuator",
                    "Scope": "-",
                    "Address": "-",
                    "Status": "Success"
                })

    return symbols

with col1:
    st.header("🖮 Source Code Editor")
    
    # NEW FEATURE: File Upload
    uploaded_file = st.file_uploader(
        "📂 Upload C File",
        type=["c", "txt"]
    )

    # Default code
    default_code = """int global_var;

void main() {
    int a;
    float b;
    int a; // This is a duplicate
}"""

    # Read uploaded file
    if uploaded_file is not None:
        code_input = uploaded_file.read().decode("utf-8")
        st.success("✅ File uploaded successfully!")
    else:
        code_input = default_code

    # Text Area
    code_input = st.text_area(
        "C-Style Code:",
        value=code_input,
        height=450
    )

with col2:
    st.header("📊 Symbol Table Output")
    
    if st.button("▶ Run Analysis"):
        symbol_data = analyze_code_pro(code_input)
        
        if symbol_data:
            # Using DataFrame for a polished table look
            df = pd.DataFrame(symbol_data)
            
            # Highlighting errors in the table
            def highlight_errors(val):
                color = 'red' if 'Error' in str(val) else 'white'
                return f'color: {color}'

            st.dataframe(df)
            
            # Quick Stats Sidebar
            st.sidebar.metric("Total Symbols", len(symbol_data))
            st.sidebar.metric(
                "Duplicate Errors",
                sum(1 for s in symbol_data if "Error" in s['Status'])
            )
        else:
            st.info("Write declarations like 'int x;' to see magic!")

st.sidebar.markdown("---")
st.sidebar.info("""
**Pro Features Active:**
1. Scope Tracking
2. Duplicate Checking
3. Memory Simulation
4. Line Numbering
5. File Upload Support
""")