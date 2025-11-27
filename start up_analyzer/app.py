import streamlit as st
import ast
from linter import CodeSmellDetector

st.title("🐍 The Code Policeman")
st.write("Paste your Python code below to check for bad practices.")

# 1. Get User Input
code = st.text_area("Paste Python Code Here:", height=200)

if st.button("Lint Code"):
    if not code:
        st.warning("Please paste some code first.")
    else:
        # 2. Parse the code from the text box
        try:
            tree = ast.parse(code)
            
            # 3. Run YOUR Linter
            visitor = CodeSmellDetector("Input Code")
            visitor.visit(tree)
            
            # 4. Show Results
            if visitor.errors:
                st.error("Found Issues!")
                for error in visitor.errors:
                    st.write(error)
            else:
                st.success("✅ Clean Code! Good job.")
                
        except SyntaxError:
            st.error("❌ Syntax Error: This isn't valid Python code.")