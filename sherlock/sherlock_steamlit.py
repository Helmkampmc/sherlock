import streamlit as st
from sherlock import sherlock

# Function to perform the search using Sherlock
def perform_search(username):
    # Placeholder for actual search logic
    # You might need to call Sherlock's functions directly or modify this part
    # depending on how Sherlock is structured.
    # For example, if you have a function in Sherlock that takes a username
    # and returns a list of found profiles, you would call it here.
    found_accounts = {}
    # Simulate finding accounts for demonstration purposes
    found_accounts['Twitter'] = f'https://twitter.com/{username}'
    found_accounts['Instagram'] = f'https://instagram.com/{username}'
    return found_accounts

# Streamlit UI
st.title('Social Media Username Search with Sherlock')

username = st.text_input("Enter a username to search for across social networks:")

if st.button('Search'):
    if username:
        with st.spinner(f'Searching for {username} across social networks...'):
            # Call the search function
            results = perform_search(username)
            
            if results:
                st.success(f"Found profiles for username '{username}':")
                for platform, url in results.items():
                    st.write(f"[{platform}]({url})", unsafe_allow_html=True)
            else:
                st.warning(f"No profiles found for username '{username}'.")
    else:
        st.error("Please enter a username to start the search.")
