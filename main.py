# import libraries
import sqlite3
import streamlit as st
import requests
import time


# Set API

# API 1
# API_URL_main = "https://www.stack-inference.com/inference/v0/run/54bd58b7-9ffa-4161-91f0-565405a9d32d/659e84427c04c17941237901"
# headers = {'Authorization':
#            'Bearer cfc3f051-23da-4dc6-b3e8-0fce0dabe449',
#            'Content-Type': 'application/json'
#            }


# def query1(payload):
#     response = requests.post(API_URL_main, headers=headers, json=payload)
#     return response.json()

# copy of outputs:
# 'input-2'
# output = query({"user_id": """<USER or Conversation ID>""",
#                "in-1": """Print: Hello: My name is Astro Mind. How can I help you during the ARSSDC?""", "in-2": """tell me this round's mission"""})

# aerospaceexplorersacademy777@gmail.com  -> login with google


####################### API 2 ######################

API_URL_2 = "https://www.stack-inference.com/inference/v0/run/03046bcc-902a-4724-8d95-eb723a0ba57c/6605ffa04b740a0bfde2ac5f"
headers = {'Authorization':
           'Bearer 2ded69a2-a85a-4e09-9ee0-5f53115cb82b',
           'Content-Type': 'application/json'
           }


def query2(payload):
    response = requests.post(API_URL_2, headers=headers, json=payload)
    return response.json()

# output = query({"in-0": """whats your name?""", "user_id": """<USER or Conversation ID>"""})
# output = {"outputs":{"out-0":"My name is Astro Mind."},"run_id":"660601a37cc2962a286d2cd7","metadata":null}


# aerospaceexplorersacademy777+secondfirst@gmail.com
# ASEA777first

######## Set Streamlit page title and icon #######
st.set_page_config(
    page_title="Astro_Mind",
    page_icon="🌌"
)


###### Department ########
st.title("Astro_Mind🌌")

######## Title and introduction #######

st.caption("An AI for every ARSSDC questions!")
st.caption("Now we are in semifinal!")

###### Text Uploader #######

# Database setup
conn = sqlite3.connect("user_final_database.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        role TEXT,
        content TEXT
    )
""")
conn.commit()

st.divider()
# React to user input
prompt = st.text_input("Write down your question about Columbiat here:",
                       max_chars=800, placeholder="Prompt")

# Display user message in chat message container
if st.button("Send"):
    st.divider()
    with st.container():
        st.title("Question:")
        st.text(prompt)

    # Add user message to the database
    cursor.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)", ("user", prompt))
    conn.commit()

    # Process the user prompt and get the response

    # API-1
    # user_prompt = query1({"in-2": prompt})
    # outputs = user_prompt.get('outputs', '')
    # response = outputs.get('out-0', '')

    # API-2
    user_prompt = query2({"in-0": prompt})
    outputs = user_prompt.get('outputs', '')
    response = outputs.get('out-0', '')

    with st.spinner('Wait for it...'):
        time.sleep(3)

    # Display the response in the chat message container
    with st.container():
        st.title("Astro Mind:")
        st.write(response)

    # Add assistant response to the database
    cursor.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)", ("assistant", response))
    conn.commit()


def main():
    st.title("")


if __name__ == "__main__":
    main()
