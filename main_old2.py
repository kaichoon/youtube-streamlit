import streamlit as st
import numpy as np
import pandas as pd

st.title('Stremlit超入門')
st.write('DataFrame')

# df=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
st.map(df)