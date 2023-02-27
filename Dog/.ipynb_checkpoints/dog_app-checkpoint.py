import streamlit as st 
from PIL import Image
import requests
import pandas as pd
from io import BytesIO
import json

# Set page title
st.title("Dog Pictures")

st.set_page_config(page_title="Dog Pictures")

# Load the list of dogs from the CSV file
dogs_df = pd.read_csv("dog_list.csv")

# Define the Streamlit form
selected_dog = st.selectbox("Select a dog:", dogs_df["Breed names"])
submit_button = st.button("Submit")

#Create function to get desired URL
def generate_url(selected_dog: str)-> str:
    return f"https://dog.ceo/api/breed/{selected_dog}/images/random"
my_url=generate_url(selected_dog)


#Create a function to get image URL
def get_dog_image(my_url: str)-> str:
    response = requests.get(my_url)
    print(response)
    return response.content 
image_bytes = get_dog_image(my_url)
print(image_bytes)

data = image_bytes

# Convert bytes to string
data_str = data.decode('utf-8')

# Parse JSON string
data_json = json.loads(data_str)

# Fetch value of "message" key
message_value = data_json['message']

print(message_value)

# Display the image
if submit_button and image_bytes:
    st.image(message_value)