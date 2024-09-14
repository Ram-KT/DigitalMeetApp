# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:06:02 2024

@author: 130793
"""
import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;font-size: 40px;'>Welcome to Digital Meet</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;font-size: 40px;'>(Manufacturing)</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;font-size: 40px;'>2024</h1>", unsafe_allow_html=True)

# =============================================================================
#components.html(
    #"""
     #<iframe src="https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__628b816e-c580-4cea-a38f-ef711c65e278__19:meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1@thread.v2/join?embed=true" width='1280' height='720' allowfullscreen"></iframe>

     #""",height=720, width=1500 )

#components.html(
#      """
#       <iframe src="https://teams.microsoft.com/convene/meetings?url=%2Fl%2Fmeetup-join%2F19%3A meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1%40thread.v2%2F0%3Fcontext%3D%257B%2522Tid%2522%253A%2522 b5ff47a6-f7b4-4abf-a484-a75057bd8139%2522%252C%2522Oid%2522%253A%2522628b816e-c580-4cea-a38f-ef711c65e278%2522%252C%2522IsBroadcastMeeting%2522%253Atrue%252C%2522role%2522%253A%2522a%2522%257D&embed=true" width="1280" height="720" frameborder="0" scrolling="no" allowfullscreen style="border:none;"></iframe>""",height=720, width=1500 )

 #=============================================================================
    
# =============================================================================
#components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__628b816e-c580-4cea-a38f-ef711c65e278__19:meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1@thread.v2/join?embed=true")    
#
# # embed streamlit docs in a streamlit app
# components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__e6de7ade-191f-4b03-96a0-63290e12461e__19:ameeting_ZmE0MzBkOTQtMWJmZS00Yzg3LThmNTMtNmI2MzhlM2Q3ZDhm@thread.v2__0/join?embed=true", height=500)
# 

# # =============================================================================
# st.markdown(
#     '[Join the Teams Meeting](https://teams.microsoft.com/l/meetup-join/19:Tbi3IBWomce-Ushp-y8fssPRHbRi2reMdqLV2bRY0zs1@thread.tacv2/1726225860615?context=%7B%22Tid%22:%22b9abe56c-43a7-4e67-a17b-32cfa05c95c8%22,%22Oid%22:%22020a7cb4-5dcb-49f0-8a08-26360032c14d%22%7D)',
#     unsafe_allow_html=True
# )

a = st.container(border=True)

a.image("liveEventHasNotStartedFinal.png",width=None, use_column_width=True, channels="RGB", output_format="auto")

b = st.columns(2)
b[0].image("Slide1.PNG",use_column_width=True)
b[1].image("Slide2.PNG",use_column_width=True)

