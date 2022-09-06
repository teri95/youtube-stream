import streamlit as st
import time

st.title('Streamlit 超入門')

# st.write('Display Image')
st.write('プログレスバーの表示')
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!'

# checkbox
# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='myu image', use_column_width=True)

# select box
# numeric
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3内容を書く')
expander4 = st.expander('問い合わせ4')
expander4.write('問い合わせ4内容を書く')



# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# text
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text, 'です。'

# slider
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition