import streamlit as st
from streamlit_option_menu import option_menu
from config import IMAGES

# Page configuration
st.set_page_config(
    page_title="SPA Global Restaurant Franchise",
    page_icon="🍽️",
    layout="wide"
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_restaurant' not in st.session_state:
    st.session_state.selected_restaurant = None
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'menu'

# Custom CSS with dark theme and golden accents
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
        margin: 10px 0;
        transition: transform 0.3s;
        cursor: pointer;
        height: 100%;
        display: flex;
        flex-direction: column;
        position: relative;
    }
    .restaurant-card:hover {
        transform: scale(1.02);
    }
    .restaurant-card .image-container {
        width: 100%;
        height: 200px;
        position: relative;
        margin-bottom: 15px;
    }
    .restaurant-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 8px;
    }
    .restaurant-card .content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        z-index: 2;
    }
    .restaurant-card .button-container {
        margin-top: 15px;
    }
    h1, h2, h3 {
        color: #FFD700;
        margin-bottom: 20px;
    }
    .profile-section {
        text-align: center;
        padding: 40px;
        background-color: #2E2E2E;
        border-radius: 15px;
        margin: 40px auto;
        max-width: 600px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .profile-name {
        color: #FFD700;
        font-size: 32px;
        font-weight: bold;
        margin: 30px 0;
        letter-spacing: 2px;
    }
    .profile-title {
        color: #FFFFFF;
        font-size: 24px;
        margin: 20px 0;
        letter-spacing: 1px;
    }
    .profile-institution {
        color: #CCCCCC;
        font-size: 20px;
        margin: 20px 0 35px 0;
    }
    .linkedin-link {
        display: inline-block;
        margin-top: 25px;
        padding: 15px 40px;
        background-color: #0077B5;
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-size: 18px;
        transition: all 0.3s ease;
        border: none;
        letter-spacing: 1px;
    }
    .linkedin-link:hover {
        background-color: #005582;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,119,181,0.3);
    }
    .menu-item {
        background-color: #2E2E2E;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .menu-image {
        width: 150px;
        height: 150px;
        object-fit: cover;
        border-radius: 10px;
    }
    .menu-content {
        flex: 1;
        padding: 10px;
    }
    .menu-price {
        color: #FFD700;
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    .menu-desc {
        color: #CCCCCC;
        font-size: 16px;
        line-height: 1.5;
    }
    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        padding: 20px 0;
    }
    .gallery-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        transition: transform 0.3s;
    }
    .gallery-image:hover {
        transform: scale(1.05);
    }
    .location-card {
        background-color: #2E2E2E;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .banner-container {
        width: 100%;
        height: 300px;
        margin-bottom: 30px;
        position: relative;
    }
    .banner-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 10px;
    }
    .view-menu-btn {
        width: 100%;
        background-color: #FFD700;
        color: black;
        padding: 10px 20px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        margin-top: 10px;
    }
    .view-menu-btn:hover {
        background-color: #E5C100;
        transform: translateY(-2px);
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #E5C100;
        transform: translateY(-2px);
    }
    .menu-section {
        margin-top: 30px;
    }
    .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding: 20px 0;
    }
    .team-image {
        width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .detail-image {
        width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .brand-card {
        background-color: #2E2E2E;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .brand-content {
        padding: 20px;
    }
    .about-section {
        display: flex;
        gap: 30px;
        align-items: flex-start;
        margin: 20px 0;
    }
    .about-image {
        flex: 1;
        max-width: 50%;
    }
    .about-content {
        flex: 1;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Restaurant data
RESTAURANTS = {
    "ponnusamy": {
        "name": "The Ponnusamy Elite",
        "desc": "Traditional South Indian flavors with a modern twist",
        "full_desc": "Experience the authentic flavors of South India with our signature dishes and modern ambiance.",
        "menu": [
            {"name": "Chettinad Chicken", "price": "₹350", "desc": "Spicy chicken curry with aromatic spices", "image_index": 0},
            {"name": "Malabar Fish Curry", "price": "₹450", "desc": "Fresh fish in coconut curry", "image_index": 1},
            {"name": "Mutton Biryani", "price": "₹400", "desc": "Fragrant rice with tender mutton", "image_index": 2},
            {"name": "Thali Special", "price": "₹300", "desc": "Complete meal with variety of dishes", "image_index": 3}
        ],
        "locations": [
            {"area": "T. Nagar", "address": "123 South Street, T. Nagar, Chennai", "phone": "+91 44 2345 6789"},
            {"area": "Anna Nagar", "address": "45 2nd Avenue, Anna Nagar, Chennai", "phone": "+91 44 2345 6790"}
        ]
    },
    "slam_fitness": {
        "name": "Slam Fitness Studio",
        "desc": "Where fitness meets nutrition",
        "full_desc": "A unique blend of fitness center and healthy cuisine restaurant.",
        "menu": [
            {"name": "Protein Bowl", "price": "₹280", "desc": "Quinoa, grilled chicken, avocado", "image_index": 0},
            {"name": "Green Smoothie", "price": "₹180", "desc": "Spinach, banana, almond milk", "image_index": 1},
            {"name": "Power Salad", "price": "₹250", "desc": "Mixed greens, nuts, grilled tofu", "image_index": 2},
            {"name": "Energy Wrap", "price": "₹220", "desc": "Whole wheat wrap with hummus", "image_index": 3}
        ],
        "locations": [
            {"area": "OMR", "address": "Tech Park, OMR Road, Chennai", "phone": "+91 44 2345 6791"},
            {"area": "Velachery", "address": "Phoenix Mall, Velachery, Chennai", "phone": "+91 44 2345 6792"}
        ]
    },
    "jonahs": {
        "name": "Jonah's Bistro",
        "desc": "Contemporary dining experience",
        "full_desc": "Modern European cuisine with an Asian twist in an elegant setting.",
        "menu": [
            {"name": "Truffle Pasta", "price": "₹550", "desc": "Fresh pasta with black truffle", "image_index": 0},
            {"name": "Wagyu Burger", "price": "₹650", "desc": "Premium beef with artisanal cheese", "image_index": 1},
            {"name": "Sea Bass", "price": "₹750", "desc": "Pan-seared with herb butter", "image_index": 2},
            {"name": "Duck Confit", "price": "₹850", "desc": "Slow-cooked duck leg", "image_index": 3}
        ],
        "locations": [
            {"area": "Nungambakkam", "address": "High Road, Nungambakkam, Chennai", "phone": "+91 44 2345 6793"},
            {"area": "ECR", "address": "Beach Road, ECR, Chennai", "phone": "+91 44 2345 6794"}
        ]
    },
    "sulthans": {
        "name": "Sulthan's Biriyani",
        "desc": "Home of the legendary Hyderabadi Biriyani",
        "full_desc": "Home of the legendary Hyderabadi Biriyani and authentic Mughlai cuisine.",
        "menu": [
            {"name": "Hyderabadi Mutton Biryani", "price": "₹400", "desc": "Long-grain rice with tender mutton", "image_index": 0},
            {"name": "Chicken 65 Biryani", "price": "₹350", "desc": "Spicy chicken 65 with fragrant rice", "image_index": 1},
            {"name": "Mughlai Chicken", "price": "₹380", "desc": "Rich and creamy chicken curry", "image_index": 2},
            {"name": "Special Kebab Platter", "price": "₹600", "desc": "Assorted kebabs with mint chutney", "image_index": 3}
        ],
        "locations": [
            {"area": "Royapettah", "address": "100 Whites Road, Royapettah, Chennai", "phone": "+91 44 2345 6795"},
            {"area": "Adyar", "address": "Gandhi Nagar, Adyar, Chennai", "phone": "+91 44 2345 6796"}
        ]
    }
}

def show_restaurant_detail(restaurant_id):
    restaurant = RESTAURANTS[restaurant_id]
    images = IMAGES[restaurant_id]
    
    # Banner image with proper spacing
    st.markdown(f"""
    <div class="banner-container">
        <img src="{images['banner']}" class="banner-image">
    </div>
    """, unsafe_allow_html=True)
    
    # Restaurant name and description
    st.title(restaurant["name"])
    st.markdown(f"### {restaurant['full_desc']}")
    
    # Native Streamlit tabs with better spacing
    tab1, tab2, tab3 = st.tabs(["Menu", "Gallery", "Locations"])
    
    # Menu Tab with grid layout
    with tab1:
        st.markdown("## Our Menu")
        st.markdown('<div class="menu-grid">', unsafe_allow_html=True)
        for item in restaurant["menu"]:
            st.markdown(f"""
            <div class="menu-item">
                <img src="{images['menu_items'][item['image_index']]}" class="menu-image">
                <div class="menu-content">
                    <h3>{item['name']}</h3>
                    <div class="menu-price">{item['price']}</div>
                    <div class="menu-desc">{item['desc']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("Book a Table", key=f"book_{restaurant_id}"):
                st.session_state.page = 'contact'
                st.rerun()
    
    # Gallery Tab with grid layout
    with tab2:
        st.markdown("## Restaurant Gallery")
        st.markdown('<div class="gallery">', unsafe_allow_html=True)
        for img in images['menu_items'] + images['ambiance']:
            st.markdown(f'<img src="{img}" class="gallery-image">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Locations Tab with better spacing
    with tab3:
        st.markdown("## Our Locations")
        for location in restaurant["locations"]:
            st.markdown(f"""
            <div class="location-card">
                <h3>{location['area']}</h3>
                <p>{location['address']}</p>
                <p>Phone: {location['phone']}</p>
            </div>
            """, unsafe_allow_html=True)

def show_homepage():
    st.title("Welcome to SPA Global")
    st.markdown("### Your Gateway to Culinary Excellence")
    
    # Hero Section with proper spacing
    st.markdown("""
    <div class="banner-container">
        <img src="{}" class="banner-image">
    </div>
    """.format(IMAGES["hero"]), unsafe_allow_html=True)
    
    st.markdown("### Our Featured Brands")
    
    # Create two rows with two columns each
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    
    # First row
    with row1_col1:
        key = "ponnusamy"
        restaurant = RESTAURANTS[key]
        st.markdown(f"""
        <div class="restaurant-card">
            <div class="image-container">
                <img src="{IMAGES[key]['logo']}">
            </div>
            <div class="content">
                <div>
                    <h3>{restaurant['name']}</h3>
                    <p class="description">{restaurant['desc']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Menu", key=f"view_{key}"):
            st.session_state.page = 'restaurant'
            st.session_state.selected_restaurant = key
            st.rerun()
    
    with row1_col2:
        key = "slam_fitness"
        restaurant = RESTAURANTS[key]
        st.markdown(f"""
        <div class="restaurant-card">
            <div class="image-container">
                <img src="{IMAGES[key]['logo']}">
            </div>
            <div class="content">
                <div>
                    <h3>{restaurant['name']}</h3>
                    <p class="description">{restaurant['desc']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Menu", key=f"view_{key}"):
            st.session_state.page = 'restaurant'
            st.session_state.selected_restaurant = key
            st.rerun()
    
    # Second row
    with row2_col1:
        key = "jonahs"
        restaurant = RESTAURANTS[key]
        st.markdown(f"""
        <div class="restaurant-card">
            <div class="image-container">
                <img src="{IMAGES[key]['logo']}">
            </div>
            <div class="content">
                <div>
                    <h3>{restaurant['name']}</h3>
                    <p class="description">{restaurant['desc']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Menu", key=f"view_{key}"):
            st.session_state.page = 'restaurant'
            st.session_state.selected_restaurant = key
            st.rerun()
    
    with row2_col2:
        key = "sulthans"
        restaurant = RESTAURANTS[key]
        st.markdown(f"""
        <div class="restaurant-card">
            <div class="image-container">
                <img src="{IMAGES[key]['logo']}">
            </div>
            <div class="content">
                <div>
                    <h3>{restaurant['name']}</h3>
                    <p class="description">{restaurant['desc']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Menu", key=f"view_{key}"):
            st.session_state.page = 'restaurant'
            st.session_state.selected_restaurant = key
            st.rerun()

def show_about():
    st.title("About Us")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f'<img src="{IMAGES["team"]}" class="team-image">', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### Our Story
        
        SPA Global is a leading restaurant franchise company with a rich heritage in bringing exceptional 
        dining experiences to food enthusiasts worldwide. Founded with a vision to revolutionize the 
        culinary landscape, we've grown from a single restaurant to a diverse portfolio of brands.

        ### Our Mission

        To create extraordinary dining experiences that celebrate diverse cuisines while maintaining 
        the highest standards of quality and service.
        
        ### Our Values
        - Excellence in every dish
        - Innovation in cuisine
        - Customer satisfaction
        - Sustainable practices
        """)

def show_brands():
    st.title("Our Restaurant Portfolio")
    
    for key, restaurant in RESTAURANTS.items():
        # Create a flex container for each brand
        st.markdown(f"""
        <div class="about-section brand-card">
            <div class="about-image">
                <img src="{IMAGES[key]["logo"]}" class="detail-image">
            </div>
            <div class="about-content">
                <h3>{restaurant['name']}</h3>
                <p>{restaurant['full_desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("View Menu", key=f"view_{key}"):
                st.session_state.page = 'restaurant'
                st.session_state.selected_restaurant = key
                st.rerun()
        st.markdown("---")

def show_contact():
    st.title("Contact Us")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Send us a message")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            if st.session_state.selected_restaurant:
                restaurant = RESTAURANTS[st.session_state.selected_restaurant]["name"]
                st.text_input("Restaurant", value=restaurant, disabled=True)
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            
            if submit and name and email and message:
                st.success("Thank you for your message! We'll get back to you soon.")
    
    with col2:
        st.markdown("""
        ### Visit Us
        
        **Corporate Headquarters:**  
        SPA Global
        123 Anna Salai
        Chennai, Tamil Nadu 600002
        India
        
        **Email:**  
        info@spaglobal.com
        
        **Phone:**  
        +91 44 2345 6789
        
        **Business Hours:**  
        Monday - Friday: 9:00 AM - 6:00 PM  
        Saturday: 9:00 AM - 2:00 PM  
        Sunday: Closed
        """)

def show_profile():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="profile-section">
            <div class="profile-name">RASHMI G</div>
            <div class="profile-title">M.Sc DATA SCIENCE</div>
            <div class="profile-institution">COIMBATORE INSTITUTE OF TECHNOLOGY</div>
            <a href="https://www.linkedin.com/in/rashmi-g-5048a8298/?originalSubdomain=in" target="_blank" class="linkedin-link">
                Connect on LinkedIn
            </a>
        </div>
        """, unsafe_allow_html=True)

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=["Homepage", "About Us", "Our Brands", "Contact", "Profile"],
    icons=["house", "info-circle", "shop", "envelope", "person"],
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

# Update session state based on navigation
if selected == "Homepage":
    st.session_state.page = 'home'
elif selected == "About Us":
    st.session_state.page = 'about'
elif selected == "Our Brands":
    st.session_state.page = 'brands'
elif selected == "Contact":
    st.session_state.page = 'contact'
elif selected == "Profile":
    st.session_state.page = 'profile'

# Main content based on session state
if st.session_state.page == 'home':
    show_homepage()
elif st.session_state.page == 'about':
    show_about()
elif st.session_state.page == 'brands':
    show_brands()
elif st.session_state.page == 'contact':
    show_contact()
elif st.session_state.page == 'profile':
    show_profile()
elif st.session_state.page == 'restaurant' and st.session_state.selected_restaurant:
    show_restaurant_detail(st.session_state.selected_restaurant) 