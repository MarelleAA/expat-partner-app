import streamlit as st
import openai
# Exemple de configuration ou d'appel API :
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # ou "gpt-4"
    messages=[
        {"role": "system", "content": "Vous êtes un assistant utile."},
        {"role": "user", "content": "Quelle est la capitale de la France ?"}
    ]
)

# Affichage du résultat (par exemple dans Streamlit)
st.write(response['choices'][0]['message']['content'])

# Set OpenAI API Key
openai.api_key = "your_openai_api_key_here"

# Application Title
st.set_page_config(page_title="Absolutely AI - Expat Partner Mobility 🌍", layout="wide")
st.title("Absolutely AI - Expat Partner Mobility 🌍")

# Sidebar for language selection and settings
with st.sidebar:
    st.header("Settings")
    language = st.selectbox("Select Language:", ["English", "French", "Spanish", "German", "Chinese"])
    st.info("Switch languages to personalize your experience.")
    
    st.subheader("About")
    st.write("This app is your personal AI assistant for expat mobility, providing answers on job search, visas, housing, cultural adaptation, and more.")

# Main input field
st.subheader("Ask your question below")
user_query = st.text_input("Enter your question here (e.g., 'What are the visa requirements for France?')")

# Function to fetch GPT-4 response
def get_response(prompt, language):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a multilingual expat mobility assistant. Answer the questions professionally in {language}."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Dynamic Query Handling
if st.button("Submit") and user_query:
    with st.spinner("Fetching response..."):
        response = get_response(user_query, language)
    st.markdown("### Response:")
    st.write(response)

# Optional Features
with st.expander("💾 Save Query & Response"):
    if st.button("Save"):
        try:
            with open("saved_queries.txt", "a") as file:
                file.write(f"Language: {language}\nQuery: {user_query}\nResponse: {response}\n---\n")
            st.success("Query and response saved successfully!")
        except Exception as e:
            st.error(f"Error saving the query: {e}")

# Tips Section
with st.expander("💡 Tips & Suggestions"):
    st.write(
        "- For visa questions, include the destination country and purpose of travel.\n"
        "- For job searches, mention your profession and any specific preferences.\n"
        "- Use clear and concise language for best results."
    )

# Error Handling Demonstration
if not user_query:
    st.warning("Please enter a question to get started.")
