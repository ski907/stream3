

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

st.title('My first app')

st.write("Here's our second attempt at using data to create a table:")

'Starting a long computation....'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    chart_data


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
