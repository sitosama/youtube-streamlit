import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit超入門')

# インタラクティブなウィジェット：チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('2139884_s.jpg')
    st.image(img, caption='KARATE', use_column_width=True)

st.selectbox(
    'あなたが好きな数字を教えてください、'
)
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
