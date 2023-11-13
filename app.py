# import files
import streamlit as st
import pandas as pd
import plotly.express as pe



# Load the data files into a DataFrame

# Create title and table

st.header('Car Advertisement Stats')
car_advertisement_df = pd.read_csv('vehicles_us.csv')
car_advertisement_df 

# Create scatter plot

st.header('Is there a relationship between the number of cylinders and price?')

st.write("""**Scatter plot** """)

fig, ax=plt.subplots()
cylinder = ax.scatter(car_advertisement_df['cylinders'], car_advertisement_df['price'])
ax.set_xlabel('cylinders')
ax.set_ylabel('price')
ax.set_title('Relationship between cylinders and price')
st.pyplot(fig)


# Create histogram of price

st.header('Show distribution of price')

st.write("""**Histogram** """)

fig, ax=plt.subplots()

columns_to_select = ['price','model_year', 'condition','cylinders', 'fuel', 'odometer', 'transmission']

selected_columns = st.selectbox('Select column for histogram', columns_to_select)

include_nan = st.checkbox('Include nan values', value=True)
filtered_data = car_advertisement_df[selected_columns] if include_nan else car_advertisement_df[selected_columns]

histogram = ax.hist(filtered_data, bins=20, color='green', alpha=0.5, edgecolor='k')

ax.set_xlabel(selected_columns)
ax.set_ylabel('Count')
ax.set_title(f'Histogram of {selected_columns}')

st.pyplot(fig)
