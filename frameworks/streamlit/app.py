import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit!")

# Display a text element
st.write("This is a simple Streamlit app.")


# Create a simple DataFrame and display it
df = pd.DataFrame(
    {
        'first column' : [1,2,3,4],
        'second column': [10, 20, 30, 40]
    }
)

# Display the DataFrame in the app
st.write("Here is the dataframe:")
st.write(df)

#Create a line chart using the DataFrame
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)
st.line_chart(df)