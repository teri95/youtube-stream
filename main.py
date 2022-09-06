import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門')

# st.write('DataFrame')
st.write('Display Image')

img = Image.open('sample.png')
st.image(img, caption='myu image', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(df)  #折れ線グラフ
# st.area_chart(df)  #エリアチャート
# st.bar_chart(df)  #棒グラフ

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# 地図表
# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# 画像を表示


# st.dataframe(df.style.highlight_max(axis=0))  #動的な表(ソートを変えられる)
# st.table(df.style.highlight_max(axis=0))  #静的な表(ソートできない)
#
# """
# # 章
# ## 節
# ### 項
#
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
#
# """

