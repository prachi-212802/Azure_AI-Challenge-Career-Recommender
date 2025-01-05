import streamlit as st

def home_page(go_to_page):
    # Set the title of the page
    st.title("Career Recommender")

    # Apply custom styling with st.markdown (CSS)
    st.markdown("""
    <style>
        .header {
            color: #0d47a1;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .description {
            color: #424242;
            font-size: 1.2rem;
            line-height: 1.6;
        }
        .cta {
            color: #ffffff;
            background-color: #0288d1;
            font-size: 1.2rem;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
        }
        .cta:hover {
            background-color: #0277bd;
        }
        .icon {
            font-size: 3rem;
            color: #0288d1;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the header with a custom style
    st.markdown('<h2 class="header">Discover Your Ideal Career Path</h2>', unsafe_allow_html=True)

    # Display the description text with a custom style
    st.markdown("""
    <p class="description">
    Welcome to the <strong>Career Recommender</strong> platform, where you can explore a variety of career options suited to your skills, interests, and personality.
    <br><br>
    Our goal is to help you find the right career by providing personalized recommendations based on a brief survey. Whether you're just starting out or considering a career change, we're here to guide you through the process.
    <br><br>
    <strong>Why use Career Recommender?</strong>
    <ul>
        <li>Get tailored career suggestions based on your unique traits.</li>
        <li>Discover industries and roles that match your interests.</li>
        <li>Understand your strengths and how they align with potential careers.</li>
    </ul>
    Take the survey to get started, and let us help you discover a career that fits your aspirations!
    </p>
    """, unsafe_allow_html=True)

    # Display a large, eye-catching emoji and text for the call to action
    st.markdown('<div class="icon">🚀</div>', unsafe_allow_html=True)

    # Add a stylish "Start the Survey" button
    if st.button("Start the Survey", key="start_survey", help="Click to begin your career survey!"):
        st.write("Redirecting to the survey page...")
        import streamlit as st

def home_page(go_to_page):
    # Set the title of the page
    st.title("Career Recommender")

    # Apply custom styling with st.markdown (CSS)
    st.markdown("""
    <style>
        .header {
            color: #0d47a1;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .description {
            color: #424242;
            font-size: 1.2rem;
            line-height: 1.6;
        }
        .cta {
            color: #ffffff;
            background-color: #0288d1;
            font-size: 1.2rem;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
        }
        .cta:hover {
            background-color: #0277bd;
        }
        .icon {
            font-size: 3rem;
            color: #0288d1;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the header with a custom style
    st.markdown('<h2 class="header">Discover Your Ideal Career Path</h2>', unsafe_allow_html=True)

    # Display the description text with a custom style
    st.markdown("""
    <p class="description">
    Welcome to the <strong>Career Recommender</strong> platform, where you can explore a variety of career options suited to your skills, interests, and personality.
    <br><br>
    Our goal is to help you find the right career by providing personalized recommendations based on a brief survey. Whether you're just starting out or considering a career change, we're here to guide you through the process.
    <br><br>
    <strong>Why use Career Recommender?</strong>
    <ul>
        <li>Get tailored career suggestions based on your unique traits.</li>
        <li>Discover industries and roles that match your interests.</li>
        <li>Understand your strengths and how they align with potential careers.</li>
    </ul>
    Take the survey to get started, and let us help you discover a career that fits your aspirations!
    </p>
    """, unsafe_allow_html=True)

    # Display a large, eye-catching emoji and text for the call to action
    st.markdown('<div class="icon">🚀</div>', unsafe_allow_html=True)

    # Add a stylish "Start the Survey" button
    if st.button("Start the Survey", key="start_survey", help="Click to begin your career survey!"):
        st.write("Redirecting to the survey page...")
        go_to_page("info_page")
