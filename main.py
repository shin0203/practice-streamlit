import streamlit as st
import time

st.title('Streamlit 超入門') # アプリケーションのタイトルの設定

# (base)C:\Users\shin001\practice\Streamlit>streamlit run main.py
    # You can now view your Streamlit app in your browser
    # Local URL: http://localhost:8501
    # Network URL http://192.168.100.117:8501

st.write('DataFrame') # テキストの追加 データフレーム(表)を扱いたい

# df= pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.write(df) # 表を表示させる st.dataframe(df)でも可
# st.dataframe(df, width= 100, height= 100) # st.dataframeだと括弧内に引数を入れることができる
# 引数dfをdf.style.highlight_max()に変えると列もしくは行の中で最大のものをhighlightする
    # 列を指定する場合はaxis= 0／行を指定する場合はaxis= 1 ←pandasの機能
# st.dataframe(df.style.highlight_max(axis= 0))
# st.table(df.style.highlight_max(axis= 0)) # st.table(df)でも可 スタティック(静的)な表を表示させたいとき使用
# 表について詳しくは Welcome to Streamlit > REFERENCE GUIDES > API reference > Display data を参照

# マークダウンの挿入
# 詳しくは REFERENCE GUIDES > API reference > Display text
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

# チャートの挿入
# df= pd.DataFrame(
#     np.random.rand(20, 3), # 正規分布を元に生成された乱数で構成された縦20／横3の表
#     columns= ['a', 'b', 'c']
# )
# st.line_chart(df) # 折れ線グラフで表示する
# st.area_chart(df) # 塗りつぶして表示する
# st.bar_chart(df) # 棒グラフで表示する
# 詳しくは REFERENCE GUIDS > API reference > Display charts

# マップの挿入
df= pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+ [35.69, 139.70], # 新宿付近の値
    columns= ['lat', 'lon'] # 緯度と経度
)
st.map(df)
# 詳しくは REFERENCE GUIDS > API reference > Display charts

# 画像の表示
st.write('Display Image')
if st.checkbox('Show Image'): # checkboxにcheckが入っていたら画像を表示させる
    img= Image.open('sample.jpeg') # 同じ階層の画像であれば簡易に表記できる
    st.image(img, caption= 'stag beetle', use_column_width= True) # use_column_width レイアウトの幅に合わせて表示
    # API reference > Display media

option= st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11)) # 1～10までの数字のリスト
)
'あなたの好きな数字は、', option, 'です。'

st.write('Interactive Widgets')
text= st.text_input('あなたの趣味を教えてください。')
'あなたの趣味: ', text

condition= st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション: ', condition
# API reference > Display interactive widgets

left_column, right_column= st.beta_columns(2)
button= left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム') # True(= 押された)

expander= st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration= st.empty()
bar= st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+ 1}')
    bar.progress(i+ 1)
    time.sleep(0.1)
'Done!!'

# Webアプリの公開 Streamlit. > Sharing > New app
# https://www.streamlit.io/sharing-sign-up
# GithubのPrimary emailが必要