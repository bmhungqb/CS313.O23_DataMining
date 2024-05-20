import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
import helpers
from Data_analysis.utils import *

st.set_page_config(layout="wide")


def reset():
    st.session_state.selection = 'Choose a language'


st.title('PHÂN LOẠI HÌNH ẢNH CÁC ĐỊA ĐIỂM DU LỊCH VIỆT NAM VÀ THÔNG TIN VỀ ĐỊA ĐIỂM ĐÓ')
col1, col2 = st.columns([0.4, 0.6])
with col1:
    st.header('Hình ảnh')

    img_file = st.file_uploader(label='Tải hình ảnh lên', type=['png', 'jpg'])
    if img_file:

        img = Image.open(img_file)
        option = st.selectbox(label='Chỉnh sửa',options=('Ảnh gốc', 'Cắt ảnh'))
        if option == 'Ảnh gốc':
            st.image(img)
        elif option == 'Cắt ảnh':
            # Get a cropped image from the frontend
            img = st_cropper(img, realtime_update=True, box_color='#FF0004')

            # Manipulate cropped image at will
            st.write("Ảnh cắt")
            _ = img.thumbnail((400, 400))
            st.image(img)
with col2:
    st.header('Kết quả dự đoán')
    if img_file:
        check_des = 0
        check_list = 0
        label = helpers.predict(img)
        st.write(f'Đây là: **{label}**')

        st.subheader(f'Phân tích địa điểm **{label}**')
        response = analysis(label)
        for res in response:
            st.write('*', res)




