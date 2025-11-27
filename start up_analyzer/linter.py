import ast
import sys
import os

# ---------------------------------------------------------
# THE DETECTOR CLASS (The "Health Inspector")
# ---------------------------------------------------------
class CodeSmellDetector(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.errors = []

    # PART 3: CATCHING PRINT()
    # This runs every time the inspector sees a function call.
    def visit_Call(self, node):
        # 1. THE CHECK: Is the function name simple? (e.g. print(), not logging.info())
        is_simple_name = isinstance(node.func, ast.Name)

        # 2. THE MATCH: Is the function name 'print'?
        # We initialize it to False, and only check if it is a simple name.
        is_print = False
        if is_simple_name:
            if node.func.id == 'print':
                is_print = True

        # 3. THE PENALTY: If it is a simple 'print' call, record an error.
        if is_simple_name and is_print:
            self.errors.append(
                f"{self.filename}:{node.lineno} -> 🚫 FOUND PRINT: Use logging instead"
            )

        # 4. KEEP WALKING: Look inside the arguments (e.g. print(sum(x)))
        self.generic_visit(node)

    # PART 4: CATCHING BAD NAMES
    # This runs every time the inspector sees a function definition (def name():).
    def visit_FunctionDef(self, node):
        # Check 1: Snake Case
        # Logic: If the name is NOT all lowercase, it is bad.
        if not node.name.islower():
            self.errors.append(
                f"{self.filename}:{node.lineno} -> ⚠️  NAMING: '{node.name}' must be snake_case"
            )
        
        # Check 2: Length (YOUR HOMEWORK)
        # Logic: If the name is shorter than 3 characters, it is bad.
        if len(node.name) < 3:
            self.errors.append(
                f"{self.filename}:{node.lineno} -> ⚠️  NAMING: '{node.name}' is too short!"
            )

        # Keep walking to check code inside the function
        self.generic_visit(node)


# ---------------------------------------------------------
# THE PLUMBING (File Reading & CLI)
# ---------------------------------------------------------
def lint_file(filepath):
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    # Open the file and read the text
    with open(filepath, "r") as source:
        # MAGIC STEP: Parse the text into an Abstract Syntax Tree (AST)
        try:
            tree = ast.parse(source.read())
        except SyntaxError:
            print(f"❌ Syntax Error in {filepath}. Cannot lint.")
            return

    # Create our inspector and start the visit
    visitor = CodeSmellDetector(filepath)
    visitor.visit(tree)

    # Print the report
    if visitor.errors:
        for error in visitor.errors:
            print(error)
    else:
        print(f"✅ {filepath} is clean!")

if __name__ == "__main__":
    # Ensure the user provided a filename argument
    if len(sys.argv) < 2:
        print("Usage: python linter_worksheet.py <filename>")
    else:
        lint_file(sys.argv[1])