import streamlit as st
import json
import os

DATA_FILE = "private_submissions.json"

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        submissions = json.load(file)
else:
    submissions = []

st.title("🎉 Party Ideas & Menu Submission Form")

with st.form("party_form"):
    name = st.text_input("Student Name")
    roll_number = st.text_input("Roll Number")
    party_type = st.selectbox("Select Party Type", ["Birthday", "Wedding", "Corporate Event", "Casual Gathering", "Other"])
    theme = st.text_input("Party Theme (Optional)")
    menu_items = st.text_area("Suggested Menu (comma-separated items)")
    additional_ideas = st.text_area("Any Additional Suggestions?")
    submit_button = st.form_submit_button("Submit Idea")

    if submit_button:
        if name and roll_number and party_type and menu_items:
            new_entry = {"Name": name, "Roll Number": roll_number, "Party Type": party_type, "Theme": theme, 
                         "Menu": menu_items, "Suggestions": additional_ideas}
            submissions.append(new_entry)

            # Save to JSON file
            with open(DATA_FILE, "w") as file:
                json.dump(submissions, file, indent=4)

            st.success("✅ Submission saved successfully!")
        else:
            st.error("⚠️ Please fill all required fields!")
