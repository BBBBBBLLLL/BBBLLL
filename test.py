import streamlit as st 


st.title("Statistics Calculator") 

st.header("Please input 10 numbers: ") 

NM1 = st.number_input("Please input 1st number: ") 
NM2 = st.number_input("Please input 2nd number: ") 
NM3 = st.number_input("Please input 3rd number: ") 
NM4 = st.number_input("Please input 4th number: ") 
NM5 = st.number_input("Please input 5th number: ") 
NM6 = st.number_input("Please input 6th number: ") 
NM7 = st.number_input("Please input 7th number: ") 
NM8 = st.number_input("Please input 8th number: ") 
NM9 = st.number_input("Please input 9th number: ") 
NM10 = st.number_input("Please input 10th number: ") 

lyst = [NM1, NM2,NM3, NM4, NM5, NM6, NM7, NM8, NM9, NM10] 
if st.button("Calculate Mean"): 
 meanNum = sum(lyst) / len(lyst) 
 st.write("Mean: ", meanNum) 
elif st.button("Calculate Median"): 
 lyst.sort() 
 m1 = lyst[len(lyst) // 2] 
 m2 = lyst[len(lyst) // 2 - 1] 
 medianNum = (m1 + m2) / 2 
 st.write("Median: ", medianNum) 
elif st.button("Calculate Mode"): 
 frequency = {} 
 for i in lyst: 
  frequency.setdefault(i, 0) 
  frequency[i] += 1 
  frequent = max(frequency.values()) 
 for i, j in frequency.items(): 
  if j == frequent: 
   modeNum = i 
   st.write("Mode: ", modeNum) 
reset.button('New game', on_click=restart)

