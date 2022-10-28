import streamlit as st 
import numpy as np
st.title("Statistics Calculator") 

st.header("Find your results by putting numbers in") 

NM1 = st.number_input("Enter the 1st number: ")
#request number input

NM2 = st.number_input("Enter the 2nd number: ") 
#request number input

NM3 = st.number_input("Enter the 3rd number: ") 
#request number input

NM4 = st.number_input("Enter the 4th number: ") 
#request number input

NM5 = st.number_input("Enter the 5th number: ") 
#request number input

NM6 = st.number_input("Enter the 6th number: ") 
#request number input

NM7 = st.number_input("Enter the 7th number: ")
#request number input

NM8 = st.number_input("Enter the 8th number: ") 
#request number input

NM9 = st.number_input("Enter the 9th number: ") 
#request number input

NM10 = st.number_input("Enter the 10th number: ") 
#request number input
Numbers = [NM1, NM2,NM3, 
        NM4, NM5, NM6, 
        NM7, NM8, NM9, NM10]
#Create the number list

if st.button("Calculate Mean"): #set button
 meanNum = sum(Numbers) / len(Numbers) 
 st.write("Mean: ", meanNum) 
#Find the mean
        
elif st.button("Calculate Median"): #set button
 Numbers.sort() 
 m1 = Numbers[len(Numbers) // 2] 
 m2 = Numbers[len(Numbers) // 2 - 1] 
 medianNum = (m1 + m2) / 2 
 st.write("Median: ", medianNum) 
#Find the meadina

elif st.button("Calculate Mode"): #set button
 frequency = {} 
 for i in Numbers: 
  frequency.setdefault(i, 0) 
  frequency[i] += 1 
  frequent = max(frequency.values()) 
 for i, j in frequency.items(): 
  if j == frequent: 
   modeNum = i 
   st.write("Mode: ", modeNum) 
#Find the mode

if st.button("Back"):# Clears all singleton caches: #set button
  st.experimental_singleton.clear()
