import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Page configuration
st.set_page_config(
    page_title="SPA Global Restaurant Franchise",
    page_icon="🍽️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 0rem 0rem;
    }
    .st-emotion-cache-18ni7ap {
        background-color: #000000;
    }
    .st-emotion-cache-6qob1r {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .restaurant-card {
        background-color: #2E2E2E;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
    }
    h1, h2, h3 {
        color: #FFD700;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Homepage", "About Us", "Our Brands", "Contact"],
    icons=["house", "info-circle", "shop", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "#FFD700", "font-size": "25px"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#333333",
        },
        "nav-link-selected": {"background-color": "#2E2E2E"},
    }
)

def show_homepage():
    st.title("Welcome to SPA Global")
    st.markdown("### Your Gateway to Culinary Excellence")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://via.placeholder.com/800x400.png?text=Featured+Restaurant", use_column_width=True)
    
    st.markdown("### Our Featured Brands")
    brand_col1, brand_col2, brand_col3 = st.columns(3)
    
    with brand_col1:
        st.markdown("""
        <div class="restaurant-card">
            <h3>The Ponnusamy Elite</h3>
            <p>Traditional flavors with a modern twist</p>
        </div>
        """, unsafe_allow_html=True)
    
    with brand_col2:
        st.markdown("""
        <div class="restaurant-card">
            <h3>Slam Fitness Studio</h3>
            <p>Where fitness meets nutrition</p>
        </div>
        """, unsafe_allow_html=True)
    
    with brand_col3:
        st.markdown("""
        <div class="restaurant-card">
            <h3>Jonah's Bistro</h3>
            <p>Contemporary dining experience</p>
        </div>
        """, unsafe_allow_html=True)

def show_about():
    st.title("About Us")
    st.markdown("""
    ### Our Story
    
    SPA Global is a leading restaurant franchise company dedicated to bringing exceptional dining experiences
    to food enthusiasts worldwide. With a diverse portfolio of brands, we combine traditional flavors with
    modern innovation to create unforgettable culinary journeys.
    
    ### Our Mission
    
    To create extraordinary dining experiences that celebrate diverse cuisines while maintaining the highest
    standards of quality and service.
    """)

def show_brands():
    st.title("Our Brands")
    
    for i in range(4):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(f"https://via.placeholder.com/400x300.png?text=Restaurant+{i+1}")
        with col2:
            st.markdown(f"""
            ### Restaurant {i+1}
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt
            ut labore et dolore magna aliqua.
            
            [Learn More](#) | [Menu](#) | [Locations](#)
            """)
        st.markdown("---")

def show_contact():
    st.title("Contact Us")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Send us a message")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        st.button("Send Message")
    
    with col2:
        st.markdown("""
        ### Visit Us
        
        **Head Office:**  
        123 Business Street  
        Chennai, Tamil Nadu  
        India
        
        **Email:**  
        info@spaglobal.com
        
        **Phone:**  
        +91 123 456 7890
        """)

# Route to appropriate page based on selection
if selected == "Homepage":
    show_homepage()
elif selected == "About Us":
    show_about()
elif selected == "Our Brands":
    show_brands()
elif selected == "Contact":
    show_contact() 