import streamlit as st

# PAGE CONFIG 
st.set_page_config(page_title="EXPLORING APP", page_icon=None, layout="wide")

#  SIDEBAR
st.sidebar.title("Navigation Menu")
page = st.sidebar.radio("Go to:", ["Home", "Widgets", "Gallery", "About"])

st.sidebar.markdown("---")
st.sidebar.success("Enjoy exploring this app!")
st.sidebar.info("Made with Streamlit")

# HOME PAGE 
if page == "Home":
    st.title("Welcome to the Heart-Winning Streamlit WebApp")
    st.subheader("A fun & interactive way to explore Streamlit widgets!")
    st.write("Use the sidebar to switch between different sections.")

    st.success("You are on the Home Page")
    st.balloons()

#  WIDGETS PAGE 
elif page == "Widgets":
    st.header("Try Out the Interactive Widgets")
    st.write("This page is full of fun, interactive options. Play around!")

    # Checkbox
    if st.checkbox("Reveal a secret"):
        st.write("You are amazing, keep shining")

    # Radio Buttons
    mood = st.radio("What's your mood today?", ["Happy", "Excited", "Calm", "Sleepy"])
    st.info(f"Your mood: {mood}")

    # Selectbox
    color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green", "Purple"])
    st.success(f"You chose {color}!")

    # Multiselect
    hobbies = st.multiselect("Select your hobbies:", ["Reading", "Coding", "Gaming", "Traveling", "Music", "Sports"])
    st.write("Your hobbies:", hobbies if hobbies else "None yet!")

    # Text Input
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello {name}! Welcome aboard")

    # Slider
    age = st.slider("Select your age:", 1, 100, 21)
    st.write(f"Wow, you are {age} years young!")

    # Button
    if st.button("Click for Magic"):
        st.snow()
        st.write("Ta-da! Magic just happened")

# Images
elif page == "Gallery":
    st.header("Beautiful Image Gallery")
    st.write("Enjoy some pictures you added")

    st.image("https://media.licdn.com/dms/image/v2/D4D12AQEY9SR-mfAVHg/article-cover_image-shrink_600_2000/B4DZb0GGRBGkAY-/0/1747851963311?e=2147483647&v=beta&t=j8xXjFCyW4av6ZHguq0qYWiC6GNrwVZQom2IonZMhrM", caption="History of AI", use_container_width=True)
    st.image("https://itchronicles.com/wp-content/uploads/2020/11/where-is-ai-used.jpg", caption="AI", use_container_width=True)

#  ABOUT PAGE 
elif page == "About":
    st.header("About This App")
    st.write("""
    This interactive webapp is built with [Streamlit](https://streamlit.io/).  
    It demonstrates how fun, engaging, and user-friendly Streamlit apps can be!  

    Features included:  
    - Title, Header, Subheader  
    - Status messages (success, info, warning, error, exception)  
    - Interactive widgets (checkbox, radio, selectbox, multiselect, text input, slider, button)  
    - Images & animations (balloons, snow)  
    - Sidebar navigation  
    """)

    st.warning("Tip: You can easily extend this app for dashboards, ML apps, or fun projects!")
    st.success("Made to Explore")
