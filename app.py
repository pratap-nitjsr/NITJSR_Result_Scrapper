import numpy as np
import pandas as pd
import streamlit as st
from StudentPortal import StudentPortal

portal = StudentPortal()

st.title('Student Results')

username = st.text_input('Enter your username')
semester = st.selectbox('Select Semester', options=['1', '2', '3', '4', '5', '6', '7', '8'])
no_of_sub = st.selectbox('No Of Subjects', options=['1', '2', '3', '4', '5', '6', '7', '8','9','10'])

if st.button('Get Results'):
    with st.spinner('Fetching results...'):
        result = portal.get_result(username, semester)
        if result:
            df = pd.DataFrame(result[1:])
            student_details = pd.DataFrame(np.array(df[df.columns[1:11]].iloc[1]).reshape(5,2), index=None, )
            student_details.columns = ['','']
            st.write(student_details.to_html(index=False, escape=False), unsafe_allow_html=True)
            index_sub = [(6+i*2) for i in range(int(no_of_sub))]
            col_idx = [0,1,2,3,7,8,9]
            marks = df[col_idx].iloc[index_sub]
            marks.columns = ['Subject Code', 'Subject', 'Mid Sem', 'Internal','End Sem','Total', 'Grade']
            st.markdown('<h2> Grade Card </h2>', unsafe_allow_html=True)
            st.write(marks.to_html(index=False, escape=False), unsafe_allow_html=True)
            summary = pd.DataFrame(np.array(df[df.columns[0:6]].iloc[index_sub[-1]+4]).reshape(3,2), index=None)
            st.markdown('<br><br>', unsafe_allow_html=True)
            summary.columns = ['','']
            st.write(summary.to_html(index=False, escape=False), unsafe_allow_html=True)
        else:
            st.error('No results found or there was an error processing your request.')
