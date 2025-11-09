import argparse  # NEW: Import the library
from openai import OpenAI

# It's good practice to put your main code in a function
def main():
    # --- NEW: Step 5 - Setup argparse ---
    parser = argparse.ArgumentParser(
        description="Generate a README.md file for a given code file using AI."
    )
    # This adds a "positional argument". It's the filename we want to read.
    parser.add_argument("filename", help="The path to the code file to analyze")
    
    # This reads the arguments from the command line
    args = parser.parse_args()
    # --- END OF NEW CODE ---

    client = OpenAI()

    # --- MODIFIED: Use the filename from the command line ---
    file_path = args.filename  # Replaced the hard-coded "sample_code.py"
    try:
        with open(file_path, "r") as file:
            code_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit()
    # --- END OF MODIFIED CODE ---

    # --- Prompts are the same ---
    system_prompt = "You are an expert technical writer specializing in creating high-quality, professional README.md files for software projects."
    user_prompt = f"""
Please analyze the following Python code and generate a complete README.md file for it.

The README should be in Markdown format and include the following sections:
1.  **Project Title:** A suitable title for the project.
2.  **Description:** A brief one or two-sentence summary of what the code does.
3.  **How to Use:** A simple example of how to run or use this code.

Here is the code:
---
{code_content}
---
"""

    # --- API call is the same ---
    print(f"Generating README for {file_path}...")
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
      ]
    )
    
    readme_content = completion.choices[0].message.content

    # --- Writing to file is the same ---
    output_filename = "README.md"
    with open(output_filename, "w") as file:
        file.write(readme_content)

    print(f"Successfully generated '{output_filename}' for '{file_path}'!")


# --- NEW: This line runs the 'main' function when you execute the script ---
if __name__ == "__main__":
    main()

















