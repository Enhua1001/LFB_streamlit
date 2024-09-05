import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #003366;  /* Dark Blue */
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 28px;
        font-weight: bold;
        color: #006699;  /* Medium Blue */
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #333333;  /* Dark Gray */
        margin-bottom: 10px;
    }
    .content {
        font-size: 18px;
        color: #444444;  /* Medium Gray */
    }
    .stSidebar .css-1d391kg {  /* Sidebar background */
        background-color: #f4f4f4;  /* Light Gray */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")

# Top-Level Sections as Radio Buttons
main_section = st.sidebar.radio("Main Sections", [
    "1. Introduction",
    "2. Data Preparation",
    "3. Classifications",
    "4. Modelling",
    "5. Conclusion"
])

# Introduction Section
if main_section == "1. Introduction":
    st.markdown("<div class='main-title'>Introduction</div>", unsafe_allow_html=True)
    
    intro_page = st.sidebar.selectbox("Introduction Topics", [
        "Purpose, Scope, Approach",
        "Initial Data Exploration and Visualizations"
    ])

    if intro_page == "Purpose, Scope, Approach":
        st.markdown("<div class='sub-title'>Purpose, Scope, Approach</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        In this section, we outline the purpose of the project, the scope of the work, and the methodology that will be applied. 
        This foundation ensures clarity and direction throughout the project lifecycle.
        </div>
        """, unsafe_allow_html=True)

    elif intro_page == "Initial Data Exploration and Visualizations":
        st.markdown("<div class='sub-title'>Initial Data Exploration and Visualizations</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        This section provides an initial exploration of the dataset, including descriptive statistics and visualizations 
        that give insights into the underlying trends and patterns.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Show Data Summary"):
            st.write("Data Summary or Descriptive Statistics go here.")
        with st.expander("Show Visualizations"):
            st.write("Graphs and plots go here.")

# Data Preparation Section
elif main_section == "2. Data Preparation":
    st.markdown("<div class='main-title'>Data Preparation</div>", unsafe_allow_html=True)
    
    data_prep_page = st.sidebar.selectbox("Data Preparation Tasks", [
        "Feature Engineering",
        "Data Transformation"
    ])

    if data_prep_page == "Feature Engineering":
        st.markdown("<div class='sub-title'>Feature Engineering</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Feature engineering involves creating new variables that make machine learning algorithms work better. 
        Here we derive meaningful features from raw data.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Feature Engineering Details"):
            st.write("Details about the features created.")

    elif data_prep_page == "Data Transformation":
        st.markdown("<div class='sub-title'>Data Transformation</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Data transformation steps involve scaling, encoding, and normalizing data to prepare it for modeling. 
        These steps are crucial for ensuring that models perform optimally.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Transformation Steps"):
            st.write("Details about data transformation.")

# Classifications Section
elif main_section == "3. Classifications":
    st.markdown("<div class='main-title'>Classifications</div>", unsafe_allow_html=True)
    
    classifications_page = st.sidebar.selectbox("Classifications Tasks", ["Binning"])

    if classifications_page == "Binning":
        st.markdown("<div class='sub-title'>Binning</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Binning involves grouping continuous variables into discrete bins or intervals, 
        which can simplify the analysis and help reveal underlying patterns.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Binning Techniques"):
            st.write("Details about the binning process.")

# Modelling Section
elif main_section == "4. Modelling":
    st.markdown("<div class='main-title'>Modelling</div>", unsafe_allow_html=True)
    
    modelling_page = st.sidebar.selectbox("Modelling Types", [
        "Linear Modelling",
        "Non-linear Modelling",
        "Time Series"
    ])

    if modelling_page == "Linear Modelling":
        st.markdown("<div class='sub-title'>Linear Modelling</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Linear modelling focuses on techniques where the relationship between the input variables and the output is linear. 
        This section explores various linear models applied in the project.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Linear Models Used"):
            st.write("Details and results of linear models.")

    elif modelling_page == "Non-linear Modelling":
        st.markdown("<div class='sub-title'>Non-linear Modelling</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Non-linear models are applied where the relationship between variables is not linear. 
        This section delves into techniques such as Random Forest and XGBoost.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Non-linear Models Used"):
            st.write("Details and results of non-linear models.")

    elif modelling_page == "Time Series":
        st.markdown("<div class='sub-title'>Time Series</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        Time series modelling focuses on analyzing and forecasting data that is observed sequentially over time. 
        Techniques such as SARIMA and LSTM are explored in this section.
        </div>
        """, unsafe_allow_html=True)
        with st.expander("Time Series Models Used"):
            st.write("Details and results of time series models.")

# Conclusion Section
elif main_section == "5. Conclusion":
    st.markdown("<div class='main-title'>Conclusion</div>", unsafe_allow_html=True)
    
    conclusion_page = st.sidebar.selectbox("Conclusion Topics", [
        "Conclusions",
        "Next Steps"
    ])

    if conclusion_page == "Conclusions":
        st.markdown("<div class='sub-title'>Conclusions</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        The conclusions section summarizes the findings of the project, highlighting key insights and learnings.
        </div>
        """, unsafe_allow_html=True)

    elif conclusion_page == "Next Steps":
        st.markdown("<div class='sub-title'>Next Steps</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='content'>
        This section outlines the next steps, including potential future work and recommendations based on the project findings.
        </div>
        """, unsafe_allow_html=True)

