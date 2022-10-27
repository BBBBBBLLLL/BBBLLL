

import streamlit as st
import random


def get_number(length: int) -> int: 
    return random.randint(1, length)


def init(length: int = 100, post_init=False):
    if not post_init:
        st.session_state.input = 0
        st.session_state.win = 0
    st.session_state.number = get_number(length)
    st.session_state.tries = 0
    st.session_state.over = False


