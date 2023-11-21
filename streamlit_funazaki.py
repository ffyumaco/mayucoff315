import linecache
import time
from altair import AreaConfig
import numpy as np
import streamlit as st

st.title('長崎県西海市崎戸町ってどこ？')
st.write('船崎です')

text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は'+text+'です')

condition = st.slider('あなたの今の調子は？',0,50,100)

option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
('あなたが選択したのは、',option,'です')




st.sidebar.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'lteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
        right_column.write('ここは右カラムです')

from PIL import Image
img = Image.open('はーい村松.jpg')
st.image(img,caption='生活場面',use_column_width=True)

#import pandas as pd
df = pd.DataFrame(
      np.random.rand[E129°34'14.97" N33°1'2.759"]
      columns = ['lat','lon']  #lat(latitude)=緯度　#lon(longitude)=経度
)
st.map(df)

import numpy as np
df = pd.DataFrame(
      np.random.rand(20,3),
      columns = ['a','b','c']
)

st.table(df.style.highlight_max(axis=0))

st.bar_chart(df)