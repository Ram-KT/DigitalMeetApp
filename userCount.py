# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:06:02 2024

@author: 130793
"""
#import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(layout="wide")

# =============================================================================
# components.html(
#     """
#     <iframe src="https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__e6de7ade-191f-4b03-96a0-63290e12461e__19:ameeting_ZDlkYjIwNDAtYThiNy00ZDNjLWFkZjItODlhOTkwYjg4ZDQ3@thread.v2/join?embed=true" width='1280' height='720' allowfullscreen"></iframe>
# 
#     """,height=720, width=1500 )
# =============================================================================
    
# =============================================================================
# components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__e6de7ade-191f-4b03-96a0-63290e12461e__19:ameeting_ZDlkYjIwNDAtYThiNy00ZDNjLWFkZjItODlhOTkwYjg4ZDQ3@thread.v2/join?embed=true")    
# 
# # embed streamlit docs in a streamlit app
# components.iframe("https://teams.microsoft.com/convene/meetings/b5ff47a6-f7b4-4abf-a484-a75057bd8139__e6de7ade-191f-4b03-96a0-63290e12461e__19:ameeting_ZmE0MzBkOTQtMWJmZS00Yzg3LThmNTMtNmI2MzhlM2Q3ZDhm@thread.v2__0/join?embed=true", height=500)
# 
# =============================================================================

a = st.container(border=True)

a.image("liveEventHasNotStartedFinal.png",width=None, use_column_width=None, channels="RGB", output_format="auto")
