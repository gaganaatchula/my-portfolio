import streamlit as st
from streamlit_option_menu import option_menu
import base64
import pandas as pd
import sqlite3

# Set up the page title and favicon
st.set_page_config(page_title="Portfolio", page_icon=":briefcase:")

with st.sidebar:
    selected = option_menu(
        "",
        ["About Me", "Education", "Skills", "Projects", "Certifications", "Internships", "Activities", "Contact Me"],
        icons=["person", "briefcase", "list-task", "gear", "award", "briefcase", "trophy", "envelope"],
        menu_icon="cast",
        default_index=0
    )


# Custom CSS for the page
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }
        .main-title {
            color: red;
            font-size: 2.5em;
            margin-top: 0;
        }
        .sub-title {
            color: #555;
            font-size: 1.5em;
        }
        .content-text {
            font-size: 1.1em;
            line-height: 1.6;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: white;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('contact_form.db')
    return conn

# Function to insert contact form data into SQLite database
def insert_message(name, email, message):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contact_messages (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

# Pages
def about_me():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 class='main-title'>Gagana Atchula</h1>", unsafe_allow_html=True)
        st.image("image/gagana.jpg", width=325)
        
    with col2:
        st.write("")
        st.write("")  # You can add more st.write("") for additional spacing

    # Add a title using the h3 tag
        st.markdown("""
        <h3>About Me</h3>
        <ul class="content-text">
            <li>I'm Gagana Atchula, passionate about technology and innovation, particularly in Data Science, Machine Learning, and Artificial Intelligence. 
            I have been actively working on several projects. My experience with Streamlit has allowed me to create intuitive and user-friendly interfaces, which I continually refine to enhance user experience.</li>
        </ul>
    """, unsafe_allow_html=True)



        
        with open("files/GAGANA RESUME.pdf", "rb") as resume_file:
            resume_bytes = resume_file.read()
            st.download_button(
                label="📄 Download Resume",
                data=resume_bytes,
                file_name="Gagana_Atchula_Resume.pdf",
                mime="application/pdf",
            )


def education_page():
    st.markdown("<h1 class='main-title'>Education</h1>", unsafe_allow_html=True)
    
    education_data = {
        "S.No": [1, 2, 3],
        "Qualification": [
            "Bachelor of Technology in Computer Science and Engineering [Data Science]",
            "Intermediate MPC",
            "10th Standard"
        ],
        "Institution": [
            "Hyderabad Institute of Technology and Management",
            "Narayana Group of Institute",
            "Narayana Group of Schools"
        ],
        "Years": [
            "2021-2025",
            "2019-2021",
            "2018-2019"
        ]
    }
    
    df_education = pd.DataFrame(education_data)
    st.dataframe(df_education, hide_index=True)

def skills_page():
    st.markdown("<h1 class='main-title'>Skills</h1>", unsafe_allow_html=True)

    st.markdown("<h2 class='sub-title'>Technical Skills</h2>", unsafe_allow_html=True)
    st.markdown("""
        <ul class="content-text">
            <li><strong>Programming Languages:</strong> C, Python, HTML, CSS, JavaScript, PHP, SQL</li>
            <li><strong>Data Analysis:</strong> Pandas, NumPy, Matplotlib, Seaborn</li>
            <li><strong>Machine Learning:</strong> Scikit-learn</li>
            <li><strong>Tools:</strong> Power BI, Tableau</li>
        </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h2 class='sub-title'>Soft Skills</h2>", unsafe_allow_html=True)
    st.markdown("""
        <ul class="content-text">
            <li>Communication</li>
            <li>Teamwork</li>
            <li>Problem-solving</li>
            <li>Adaptability</li>
        </ul>
    """, unsafe_allow_html=True)


def projects_page():
    st.markdown("<h1 class='main-title'>Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>Here are some of the projects I've worked on:</p>", unsafe_allow_html=True)

    project_details = [
        ("Email Spam Detection using Machine Learning", 
         "Implemented a machine learning model to detect and filter email spam, showcasing proficiency in data analysis and algorithm development.",
         "https://github.com/gaganaatchula/Gagana-Atchula-OIBSIP/tree/main/Email_Spam_Detection_Task4"),
        ("Car Price Prediction with Machine Learning", 
         "Utilized machine learning algorithms to predict car prices, demonstrating strong analytical and problem-solving skills.",
         "https://github.com/gaganaatchula/Gagana-Atchula-OIBSIP/tree/main/Car_Price_Prediction_Task3"),
        ("Unemployment Analysis with Python", 
         "Conducted a comprehensive analysis of unemployment trends using Python, showcasing data analysis and interpretation capabilities.",
         "https://github.com/gaganaatchula/Gagana-Atchula-OIBSIP/tree/main/Unemployment_Analysis_Task2"),
        ("Emotion Detection", 
         "Implemented an Emotion Detection project utilizing advanced machine learning techniques to accurately analyze and interpret emotional states from various inputs."),
        ("Patient Summary Dashboard", 
         "A patient summary dashboard in Power BI provides a comprehensive and visually intuitive view of key health metrics, enabling healthcare professionals to quickly assess patient status and track critical trends for informed decision-making."),
        ("Finsculpt Dashboard", 
         "A Financial and Banking Learning Dashboard is a web-based platform designed to offer interactive tools, resources, and analytics for users to understand financial concepts, track personal or business finances, and enhance banking knowledge.")
    ]

    for title, description, *github_link in project_details:
        st.markdown(f"<h3 class='sub-title'>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='content-text'>{description}</p>", unsafe_allow_html=True)
        if github_link:
            st.markdown(f"<a href='{github_link[0]}' target='_blank'>View on GitHub</a>", unsafe_allow_html=True)


def certifications_page():
    st.markdown("<h1 class='main-title'>Certifications</h1>", unsafe_allow_html=True)

    certifications = [
        ("Python for Data Science - NPTEL", "image/image1.jpg"),
        ("Programming in Java - NPTEL", "image/image2.jpg"),
        ("Full Stack Web Development Certification - Internshala", "image/image3.jpg"),
        ("Python for Machine Learning Certification - Great Learning", "image/image4.jpg"),
        ("Data Science Certification - Oasis Infobyte", "image/image5.jpg"),
        ("Web Development Certification - Oasis Infobyte", "image/image6.jpg"),
        ("Python for Machine Learning and Data Science - Udemy", "image/image7.jpg"),
        ("Data Visualization with PowerBI - Great Learning", "image/image8.jpg")
    ]

    for cert, img_path in certifications:
        with st.expander(cert):
            st.image(img_path, use_column_width=True)


def Internships_page():
    # Define styles and scripts
    st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: bold;
            color: red;
            text-align: center;
            margin-bottom: 1em;
        }
        .sub-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #555;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        .content-text {
            font-size: 1em;
            color: #666;
            line-height: 1.6;
        }
        .collapsible-header {
            font-weight: bold;
            cursor: pointer;
            padding: 0.5em;
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-top: 0.5em;
        }
        .collapsible-content {
            display: none;
            padding: 0.5em;
            border: 1px solid #ddd;
            border-top: none;
            border-radius: 0 0 5px 5px;
            background-color: #fafafa;
        }
        .collapsible-content ul {
            list-style-type: disc;
            margin-left: 1em;
        }
    </style>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            var headers = document.querySelectorAll(".collapsible-header");
            headers.forEach(function(header) {
                header.addEventListener("click", function() {
                    var content = this.nextElementSibling;
                    if (content.style.display === "none") {
                        content.style.display = "block";
                    } else {
                        content.style.display = "none";
                    }
                });
            });
        });
    </script>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>Internships</h1>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>Here is a summary of my professional experience:</p>", unsafe_allow_html=True)
    
    Internship_details = [
        ("IIIT Hyderabad Internship", "January 2024 - Present", [
            "Expertise in Natural Language Processing (NLP) and Speech Recognition, showcasing proficiency in understanding and processing spoken language. Successfully executed a project on Emotion Detection, leveraging advanced techniques to analyze and interpret human emotions from speech signals.",
            "Spearheaded the creation of a sophisticated multilingual chatbot, employing NLP algorithms for natural language understanding and integrating speech recognition capabilities, enhancing user engagement and fostering seamless cross-language communication."
        ]),
        ("Oasis Infobyte - Web Development Internship", "September 2023 - October 2023", [
            "Led the redesign and development of a dynamic e-commerce platform, implementing responsive design and optimizing user experience, resulting in a 30% increase in site engagement.",
            "Developed a personalized portfolio website showcasing diverse web projects, integrating interactive elements and emphasizing clean design principles to highlight technical skills and creativity.",
            "Orchestrated collaboration between design and development teams to ensure a cohesive user interface and smooth functionality, achieving a harmonious balance between aesthetics and functionality in the e-commerce platform."
        ]),
        ("Internshala - Web Development Internship", "June 2023 - July 2023", [
            "Participated in an immersive web development internship, honing practical expertise in HTML, CSS, and JavaScript. Demonstrated proficiency by successfully delivering the 'Financial and Banking Learning Dashboard' project.",
            "Implemented user feedback loops and conducted usability tests, refining the Learning Dashboard based on insights, resulting in an intuitive interface and heightened user satisfaction."
        ]),
        ("Oasis Infobyte - Data Science Internship", "September 2023 - October 2023", [
            "Led initiatives in machine learning and data visualization, driving the advancement and application of sophisticated data science techniques. Pioneered projects, showcasing expertise in cutting-edge analytics and visualization methodologies."
        ])
    ]

    for title, period, responsibilities in Internship_details:
        st.markdown(f"<div class='collapsible-header'>{title} ({period})</div>", unsafe_allow_html=True)
        st.markdown("<div class='collapsible-content'>", unsafe_allow_html=True)
        st.markdown("<ul class='content-text'>", unsafe_allow_html=True)
        for responsibility in responsibilities:
            st.markdown(f"<li>{responsibility}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def Activities_page():
    # Set the main title of the page
    st.markdown("<h1 class='main-title'>Activities</h1>", unsafe_allow_html=True)

    # List of activities with details
    Activities = [
        ("For a Cause [NGO Organization] Volunteer", 
         "image/foracause.jpg", 
         "Actively volunteered in community service projects, organizing events, and participating in outreach programs that benefitted local communities. "
         "<a href='https://foracause.ngo/' target='_blank'>For a Cause NGO</a>"),
        ("IUCEE Organization Member", 
         "image/iucee.jpg", 
         "Organized and managed college technical fests, coordinating with teams and ensuring the smooth execution of events.")
    ]

    # Create three columns, with the middle one acting as the spacer
    col1, spacer, col2 = st.columns([1, 0.2, 1])  # Adjust the 0.2 for more/less spacing

    # Display the first activity in the first column
    with col1:
        activity, image, description = Activities[0]
        st.markdown(f"<h2 class='sub-title'>{activity}</h2>", unsafe_allow_html=True)
        if image:
            st.image(image)
        st.markdown(f"<p class='content-text'>{description}</p>", unsafe_allow_html=True)

    # Display the second activity in the second column
    with col2:
        activity, image, description = Activities[1]
        st.markdown(f"<h2 class='sub-title'>{activity}</h2>", unsafe_allow_html=True)
        if image:
            st.image(image)
        st.markdown(f"<p class='content-text'>{description}</p>", unsafe_allow_html=True)



import streamlit as st

# Initialize session state for contact form visibility
if 'show_contact_form' not in st.session_state:
    st.session_state.show_contact_form = False

import streamlit as st

# Initialize session state to control the form visibility
if 'show_contact_form' not in st.session_state:
    st.session_state.show_contact_form = False

import streamlit as st

# Initialize session state to control the form visibility
if 'show_contact_form' not in st.session_state:
    st.session_state.show_contact_form = False

def contact_me_page():
    st.markdown("<h1 class='main-title'>Contact Me</h1>", unsafe_allow_html=True)

    # Add LinkedIn and GitHub links above the button
    st.markdown("""
    
    <ul>
        <li><a href="https://www.linkedin.com/in/gagana-atchula-9260a0244" target="_blank">LinkedIn</a></li>
        <li><a href="https://github.com/gaganaatchula" target="_blank">GitHub</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # Display link (styled as a button) to show the contact form
    if st.button("open contact form"):
        st.session_state.show_contact_form = True

    # Display the contact form if the user clicked the link/button
    if st.session_state.show_contact_form:
        st.write("Please fill out the form below to get in touch.")
        with st.form(key='contact_form'):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")

            submit_button = st.form_submit_button("Send")

            if submit_button:
                try:
                    insert_message(name, email, message)  # Save the data to the SQLite database
                    st.write(f"Thank you, {name}! Your message has been sent.")
                    st.session_state.show_contact_form = False  # Hide the form after submission
                except Exception as e:
                    st.error(f"An error occurred: {e}")


# Page selection
if selected == "About Me":
    about_me()
elif selected == "Education":
    education_page()
elif selected == "Skills":
    skills_page()
elif selected == "Projects":
    projects_page()
elif selected == "Certifications":
    certifications_page()
elif selected == "Internships":
    Internships_page()
elif selected == "Activities":
    Activities_page()
elif selected == "Contact Me":
    contact_me_page()

