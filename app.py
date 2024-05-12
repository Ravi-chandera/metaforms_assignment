import streamlit as st
import google.generativeai as genai

def main():
    st.title("Survey Question Generator")
    
    user_profile = st.text_area("Enter your profile (e.g. 'Market analyst')", height=100)
            # Process the user's question and generate the response        
        # Display the response using st.markdown()
    user_goal = st.text_area("Enter your goal:", height=100)
    
    if st.button("Get Answer"):
        # Process the user's question and generate the response
        response = generate_response(user_profile,user_goal)
        
        # Display the response using st.markdown()
        st.text(f"Your profile is {user_profile}")
        st.text(f"Your goal is {user_goal}")

        st.markdown(response)

def generate_response(user_profile,user_goal):
    prompt_parts = [
  f" You are a talented and experienced {user_profile}. returns a list of questions for a survey that will help reach the goal. Goal: {user_goal}",
]

    GOOGLE_API_KEY = "AIzaSyCPtSR4Bk7sSIvoOEPiRywsYt2UkJ0Y5oc"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt_parts)
    
    return response.text

if __name__ == "__main__":
    main()
