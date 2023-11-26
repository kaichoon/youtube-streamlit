import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Stremlit超入門')
#st.write('Display Image')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ２の回答')



# option=st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
    
# )
# 'あなたの好きな数字は',option,'です'

# text=st.text_input('あなたの趣味を教えてください')
# condition=st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの好きな趣味：',text,'です'
# 'コンディション：',condition

# if st.checkbox('Show Image'):
#     img=Image.open('keeth.jpg')
#     st.image(img,caption='santa',use_column_width=True)

