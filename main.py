import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df) #ぴったりのサイズで出てくる
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200) #表の大きさ長さハイライトなどを設定可能
st.table(df.style.highlight_max(axis=0)) #テーブルは固定

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df_1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df_1)

st.area_chart(df_1)

st.bar_chart(df_1)

df_2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69,139.70],
    columns=['lat', 'lon']
)
st.map(df_2)

st.write('Display Image')


# if st.checkbox('Show Image'):
#     img = Image.open('oka.jpg')
#     st.image(img, caption='t oka', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 10))
)

'あなたの好きな数字は、', option, 'です。' 



st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション：', condition

left_column, right_column = st.columns(2)
button = left_column.button('ボタンを押すとメッセージが登場')
if button:
    right_column.write('文字登場！！！')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1回答')
expander2 =st.expander('問い合わせ2')
expander2.write('問い合わせ2回答')
expander3 =st.expander('問い合わせ3')
expander3.write('問い合わせ3回答')
expander4 =st.expander('問い合わせ4')
expander4.write('問い合わせ4回答')

st.write('プログレスバーの表示')
'Start!!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Dome!!!'