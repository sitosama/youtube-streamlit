import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

'Start'
latest_iteration=st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {100-i}')
    bar.progress(i+1)
    time.sleep(0.1)

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
# st.write('Display Image')

# text=st.text_input('あなたの趣味は？')
# condition=st.slider('あなたの調子は？',0,10,50)
# 'あなたの趣味は:',text
# 'あなたの調子は:',condition

# option=st.selectbox('あなたの数字は、',list(['miku','maya']))
# text=st.text_input('あなたの趣味は？')
# 'あなたの好きな人は',text,'です'
# if st.checkbox('show image'):
#     img=Image.open('合格体験談.jpg')
#     st.image(img,caption='Masatoshi Katayama')
# df=pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon']
# )

# st.map(df)
