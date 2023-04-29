import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
st.title('Streamlit超入門')

st.write('プログレスバーの表示')

current_iteration = st.empty()
bar = st.progress(0)

'Start!!'
for i in range(100):
    current_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!!!!!'
# インタラクティブなウィジェット：チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('2139884_s.jpg')
#     st.image(img, caption='KARATE', use_column_width=True)

# options = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', options, 'です。'

# サイドバーに表示
# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text

# condition = st.sidebar.slider('あなたのコンディションは?', 0, 100, 50)
# 'コンディション：', condition


# ２カラムレイアウト
left_culumn, right_culumn = st.columns(2)
btn = left_culumn.button('右カラムを表示')
if btn:
    right_culumn.write('右カラムだよーん')

# expander
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')

df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
df = pd.DataFrame(
    np.random.rand(100, 2)/[50.50]+[35.69, 139.70],
    columns=['lat', 'lon']
)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
st.map(df)

# マジックコマンド
# マークダウンを適用できる
"""
# 章
## 節
### 項
```
import streamlit as st
import pandas as pd
import numpy as np
```
"""
