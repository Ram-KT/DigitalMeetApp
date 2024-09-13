# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:06:02 2024

@author: 130793
"""
import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(layout="wide")

# =============================================================================
#components.html(
    """
     <iframe src="https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__628b816e-c580-4cea-a38f-ef711c65e278__19:meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1@thread.v2/join?embed=true" width='1280' height='720' allowfullscreen"></iframe>
     """,height=720, width=1500 )

components.html(
      """
       <iframe src="https://teams.microsoft.com/convene/meetings?url=%2Fl%2Fmeetup-join%2F19%3A meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1%40thread.v2%2F0%3Fcontext%3D%257B%2522Tid%2522%253A%2522 b5ff47a6-f7b4-4abf-a484-a75057bd8139%2522%252C%2522Oid%2522%253A%2522628b816e-c580-4cea-a38f-ef711c65e278%2522%252C%2522IsBroadcastMeeting%2522%253Atrue%252C%2522role%2522%253A%2522a%2522%257D&embed=true" width="1280" height="720" frameborder="0" scrolling="no" allowfullscreen style="border:none;"></iframe>""",height=720, width=1500 )

 #=============================================================================
    
# =============================================================================
#components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__628b816e-c580-4cea-a38f-ef711c65e278__19:meeting_NjlhZmM5ZmYtMDczMy00YTY2LWEyMjQtOTlmY2I5NDlkZDg1@thread.v2/join?embed=true")    
#
# # embed streamlit docs in a streamlit app
# components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__e6de7ade-191f-4b03-96a0-63290e12461e__19:ameeting_ZmE0MzBkOTQtMWJmZS00Yzg3LThmNTMtNmI2MzhlM2Q3ZDhm@thread.v2__0/join?embed=true", height=500)
# 
# =============================================================================

a = st.container(border=True)

a.image("liveEventHasNotStartedFinal.png",width=None, use_column_width=True, channels="RGB", output_format="auto")
