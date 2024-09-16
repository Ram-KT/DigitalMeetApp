# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:06:02 2024

@author: 130793
"""
import streamlit.components.v1 as components

import streamlit as st

# page_bg = """
# <style>
# body {
#     background-color: #091238; /* Light blue background */
# }
# </style>
# """

# # Render the CSS in the Streamlit app
# st.markdown(page_bg, unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.logo("./itc-logo-removebg-preview.png", link="https://www.itcpspd.com/")

st.html("""
  <style>
    [alt=Logo] {
      height: 2rem;
    }
  </style>
        """)

st.markdown("<h1 style='text-align: center;font-size: 40px;'>Welcome to Digital Meet (Manufacturing) 2024</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center;font-size: 40px;'>(Manufacturing)</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center;font-size: 40px;'>2024</h1>", unsafe_allow_html=True)

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

# st.markdown("""
#     <div style="text-align: center;">
#         <a href="https://teams.microsoft.com/l/meetup-join/19%3ameeting_Y2IzM2Q4OWQtMmJjNy00ZGI3LTgzN2ItYjA0OWExYThlZDUx%40thread.v2/0?context=%7b%22Tid%22%3a%22b5ff47a6-f7b4-4abf-a484-a75057bd8139%22%2c%22Oid%22%3a%22e6de7ade-191f-4b03-96a0-63290e12461e%22%7d"">
#             Join the Teams Meeting by clicking on me!!
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown(
#      '[Join the Teams Meeting](https://teams.microsoft.com/l/meetup-join/19%3ameeting_Y2IzM2Q4OWQtMmJjNy00ZGI3LTgzN2ItYjA0OWExYThlZDUx%40thread.v2/0?context=%7b%22Tid%22%3a%22b5ff47a6-f7b4-4abf-a484-a75057bd8139%22%2c%22Oid%22%3a%22e6de7ade-191f-4b03-96a0-63290e12461e%22%7d)',
#      unsafe_allow_html=True)

# Custom HTML button centered horizontally and vertically on the screen with bigger size and rounded corners
st.markdown("""
    <style>
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 20vh; /* Adjust height to center vertically */
        }
        .custom-button {
            background-color: #4f42b5; /* Green background */
            color: white; /* White text */
            padding: 20px 25px; /* Increased padding for a larger button */
            font-size: 26px; /* Larger font size */
            font-family: 'Segoe UI', sans-serif; /* Set font to Segoe UI */
            font-weight: bold; /* Make text bold */
            border: 1px solid #109dd9; /* Slightly thick border */
            border-radius: 30px; /* More rounded corners */
            cursor: pointer; /* Pointer on hover */
        }
        .custom-button:hover {
            background-color: #7b83eb; /* Slightly darker green on hover */
        }
    </style>

    <div class="centered-button">
        <a href="https://teams.microsoft.com/l/meetup-join/19%3ameeting_Y2IzM2Q4OWQtMmJjNy00ZGI3LTgzN2ItYjA0OWExYThlZDUx%40thread.v2/0?context=%7b%22Tid%22%3a%22b5ff47a6-f7b4-4abf-a484-a75057bd8139%22%2c%22Oid%22%3a%22e6de7ade-191f-4b03-96a0-63290e12461e%22%7d">
            <button class="custom-button">
                Click here to join the Digital Meet Live! 
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# a = st.container(border=True)

# a.image("liveEventHasNotStartedFinal.png",width=None, use_column_width=True, channels="RGB", output_format="auto")

b = st.columns(2)
b[0].image("Slide1.PNG",use_column_width=True)
b[1].image("Slide2.PNG",use_column_width=True)

c = st.columns(3)
c[0].image("Slide11.PNG",use_column_width=True)
c[1].image("Slide22.PNG",use_column_width=True)
c[2].image("Slide33.PNG",use_column_width=True)


