import streamlit as st
import google.generativeai as genai
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Placement Copilot", page_icon="🚀", layout="wide")
st.title("🚀 The Intelligent Placement Copilot")
st.write("Using 100% Free Google Gemini Models")

# --- Get API Key ---
try:
    # Get the API key from Streamlit secrets
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
except KeyError:
    st.error("Google API key not found. Please add it to your .streamlit/secrets.toml file.")
    st.stop()
except Exception as e:
    st.error(f"Error configuring API: {e}")
    st.stop()

# --- The Core Prompt ---
# This is the "brain" of your app. It's great as-is.
SYSTEM_PROMPT = """
You are an expert career coach and professional CV writer.
You will be given a 'Master CV' and a 'Job Description'.
Your task is to perform two actions:
1.  **Re-write the 'Projects' or 'Experience' section of the CV** to perfectly match the keywords and requirements in the Job Description. Only use information from the original CV. Make the user sound like the ideal candidate.
2.  **Write a 100-word cover letter paragraph** (for an email body) explaining *why* the user's specific experience (from their CV) makes them a perfect fit for this *specific role* (from the Job Description). Be professional, concise, and persuasive.

Format your entire response using Markdown.
Use a heading for '🎯 Tailored CV Section' and '✉️ Cover Letter Snippet'.
"""

# --- Load Models from CSV ---
# Caching this function means it only runs once (or if the file changes)
@st.cache_data
def load_models(csv_path):
    try:
        df = pd.read_csv(csv_path)
        # Assuming the column with model names is 'value'
        return df['value'].tolist()
    except FileNotFoundError:
        # Silently fall back to a default if the file isn't found.
        # This removes the red st.error() message.
        return ["models/gemini-2.5-flash"]
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        return ["models/gemini-2.5-flash"]

# Load the model list from your provided CSV
model_list = load_models("placement project ai models.csv")

# Find the index of 'gemini-2.5-flash' to set it as default, or default to 0
try:
    default_index = model_list.index("models/gemini-2.5-flash")
except ValueError:
    default_index = 0

# --- The UI ---
st.subheader("1. Configure Your Copilot")
selected_model = st.selectbox(
    "Select the AI Model (from your CSV):",
    model_list,
    index=default_index
)

st.subheader("2. Provide Your Documents")
col1, col2 = st.columns(2)
with col1:
    master_cv = st.text_area("Paste Your Master CV", height=400, placeholder="Paste your full CV here...")
with col2:
    job_desc = st.text_area("Paste the Job Description", height=400, placeholder="Paste the full job description here...")

if st.button("Generate My Application (Free)", type="primary"):
    if not master_cv or not job_desc:
        st.warning("Please paste both your CV and the job description.")
    else:
        try:
            # --- THIS IS THE ROBUST METHOD ---
            # 1. Initialize the model with the selected name and system prompt
            model = genai.GenerativeModel(
                model_name=selected_model,
                system_instruction=SYSTEM_PROMPT
            )
            
            # 2. Start a new, clean chat session
            chat = model.start_chat()
            
            # 3. Create the final prompt for the model
            final_user_prompt = f"Master CV:\n{master_cv}\n\nJob Description:\n{job_desc}"
            
            with st.spinner(f"Your copilot is writing using {selected_model}..."):
                # --- The API Call ---
                # 4. Send the user's content as a new message
                response = chat.send_message(final_user_prompt)
                
                # --- Display the Output ---
                st.divider()
                st.subheader("✨ Your Tailored Application Materials")
                st.markdown(response.text)

        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
            st.exception(e) # This will print the full traceback for debugging

st.sidebar.header("About")
st.sidebar.info("This app uses Google's Gemini models to help you tailor your job application materials quickly and effectively.")



