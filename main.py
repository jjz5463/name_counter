import streamlit as st
import re

# Streamlit UI
st.title("每人请假次数清点")
input_text = st.text_area("输入:", height=300)
process_button = st.button("计算")

if process_button and input_text:
    # Process the text
    unique_names = set()
    for line in input_text.split('\n'):
        for name in re.split(r'[，\s、]+', line):
            if name and not name.isdigit():
                unique_names.add(name.strip())

    unique_names_list = sorted(list(unique_names))

    # Assuming you have a way to count names, generating a dummy `name_counts` for demonstration
    name_counts = {name: input_text.count(name) for name in unique_names_list}  # Replace with your actual counting logic

    two_column_format = "\n".join([f"{name}\t{count}" for name, count in name_counts.items()])

    # Displaying the results
    st.write("总次数:", sum(name_counts.values()))
    st.text_area("每个人请假次数:", two_column_format, height=300)

