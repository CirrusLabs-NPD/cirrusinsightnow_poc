import streamlit as st
import langchain_helper as lch

# Create a Streamlit UI
st.title("Problem Statement to EPIC -> Capabilities -> Features-> User Stories-> Scenarios, and BDD Test Cases")

# User input for the problem statement
problem_statement = st.text_area("Problem Statement", "")


if st.button("Submit"):
    epic_description =  lch.generate_epic(problem_statement)
    
    st.subheader("Generated Epic:")
    st.write(epic_description)
    
    if epic_description:
        capabilities_description =  lch.generate_capabilities(epic_description)
        st.subheader("Generated Capabilities/Enablers:")
        st.write(capabilities_description)
        
    if capabilities_description:
        features_description =  lch.generate_features(capabilities_description)
        st.subheader("Generated Features:")
        st.write(features_description)
    
    if features_description:
        user_stories_description =  lch.generate_user_stories_scenarios(features_description)
        st.subheader("Generated User Stories, Scenarios & Tasks:")
        st.write(user_stories_description)
    

# Display information about the app and how to use it
st.sidebar.markdown("### Instructions")
st.sidebar.markdown(
    "1. Enter a problem statement in the text area above."
)
st.sidebar.markdown(
    "2. Click the 'Submit' button to generate a list EPIC, Capabilities, Features, User stories, Scenarios, Acceptance Criteria, and BDD test cases based on the problem statement."
)
