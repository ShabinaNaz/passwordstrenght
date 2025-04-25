import re
import streamlit as st


st.set_page_config(page_title="password strenght checker")

st.title("🔏Password strenght checker")

st.markdown(""""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !import; margin:}
    .stButton button {width: 50%; backgroud-colour #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: #45a049;}
</style>
    
 "## welcome to the ultimate Password strenght checker!
            use this simple tool to check the strenght of your password and get suggestion on how to make it strong.
            we will give helpful tips to create a **strong password**           
            """)

password = st.text_input("Enter Your Password", type="password")

Feedback = []

Score = 0

if password:
    if len(password) >= 8:
        Score +=1
    else :
        Feedback.append("🔑password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):  
      Score += 1
    else: 
        Feedback.append("🔑password should contain both upper and lower case charcters.")

    if re.search(r'\d', password):
        Score += 1
    else :
        Feedback.append("🔑 password should contain at least one digit.")
    
    if re.search(r'[!@#$%&]', password):
        Score += 1
    
    else:
        Feedback.append("🔑 password should contain at least one special chracter.")
     
    if Score == 4:
        Feedback.append("✅ your password is strong")
    elif Score == 3:
        Feedback.append("your password is medium strenght. it could be strong.")

    else:
        Feedback.append("your password is weak. please make it strong.")

    if Feedback:
        st.markdown("## improvement suggestion")
        for tip in Feedback:
             st.write(tip)

else:
    st.info("please enter your password to get started.")