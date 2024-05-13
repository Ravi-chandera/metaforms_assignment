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
  f '''Your task is to generate a set of 5-10 survey questions based on a given goal or intent related to user research, product management, marketing, customer support, or employee engagement and satisfaction. The questions should be clear, concise, and directly relevant to the provided goal.

When generating the questions, try to cover different aspects and angles related to the goal, such as user behaviors, preferences, pain points, demographics, satisfaction levels, and potential improvements or new features.

For example, if the goal is "Boost employee engagement and satisfaction to increase retention by 10%+ and hence customer satisfaction," you could generate questions like:

1. On a scale of 1-5, how would you rate your overall job satisfaction?
2. What are the top 3 factors that contribute most to your job satisfaction?
3. Do you feel that your work is valued and appreciated by your manager and the company?
4. How would you describe the current level of communication and collaboration within your team?
5. What additional resources, training, or support would help you be more effective in your role?
6. Do you feel that there are sufficient opportunities for professional growth and career advancement within the company?
7. How likely are you to recommend our company as a great place to work to your friends or family?
8. What are the biggest challenges or pain points you face in your day-to-day work?
9. If you could change one thing about your work environment or company culture, what would it be?
10. How would you rate the work-life balance and flexibility provided by the company?
  You are a talented and experienced {user_profile}. returns a list of questions for a survey that will help reach the goal. Goal: {user_goal}''',
]

    GOOGLE_API_KEY = "AIzaSyCPtSR4Bk7sSIvoOEPiRywsYt2UkJ0Y5oc"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt_parts)
    
    return response.text

if __name__ == "__main__":
    main()
