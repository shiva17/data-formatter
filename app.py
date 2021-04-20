# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:49:17 2021

@author: kolhe
"""

import streamlit as st
import pyperclip

st.title('Data Formatter')

st.markdown('### _Enter Your Code_')
code = st.text_area("Enter code here")
if(st.checkbox('Show Code')==True):
    st.text(code)
    
num_inp = st.text_input("Enter number of input parameters")

num_lists = st.selectbox('Number of lists: ', ['Select Option', 'Single', 'Multiple'])

if(num_lists == 'None'):
    pass

elif(num_lists == 'Single'):
    
    st.markdown('### _Enter List of Values_')
    list_yn = st.selectbox('What is the format of your list of values?', ['List', 'Text Separated by space'])
    values = st.text_area("Enter List of values")
    
    if(list_yn == 'List'):
        if(st.checkbox('Confirm List')==True): 
            values = eval(values)
            st.write(values)
            
        else:
            st.write('')
    elif(list_yn=='Text Separated by space'):
        values = values.split(' ')
        if(st.checkbox('Show Values')==True):
            st.write(values)
        else:
            st.write('')
            
    st.markdown('### _Generate Code_')
    #inp_params = st.text_input("format()")
    
    
    if(st.checkbox('Print Code') == True):
        final = """
for i in values:
    st.text(code.format({}))""".format(('i,'*int(num_inp))[:-1])
        exec(final)
    elif(st.checkbox('Copy To Clipboard') == True):
        final = """
s = ''
for i in values:
    s = s + code.format({})
pyperclip.copy(s)""".format(('i,'*int(num_inp))[:-1])
        exec(final)
        st.text("Code copied to clipboard")
    
        
elif(num_lists == 'Multiple'):
    st.markdown('### _Enter List of Values 1_')
    list_yn = st.selectbox('What is the format of your list of values?', ['List', 'Text Separated by space'])
    values = st.text_area("Enter List of values")
    
    if(list_yn == 'List'):
        if(st.checkbox('Confirm List')==True): 
            values = eval(values)
            st.write(values)
            
        else:
            st.write('')
    elif(list_yn=='Text Separated by space'):
        values = values.split(' ')
        if(st.checkbox('Show Values')==True):
            st.write(values)
        else:
            st.write('')
    
    if(st.checkbox('Add List 2')):
        st.markdown('### _Enter List of Values 2_')
        list_yn2 = st.selectbox('What is the format of your list of values 2?', ['List', 'Text Separated by space'])
        values2 = st.text_area("Enter List of values 2")
        
        if(list_yn2 == 'List'):
            if(st.checkbox('Confirm List 2')==True): 
                values2 = eval(values2)
                st.write(values2)
                
            else:
                st.write('')
        elif(list_yn2=='Text Separated by space'):
            values2 = values2.split(' ')
            if(st.checkbox('Show Values 2')==True):
                st.write(values2)
            else:
                st.write('')

    if(st.checkbox('Add List 3')):
        st.markdown('### _Enter List of Values 3_')
        list_yn = st.selectbox('What is the format of your list of values 3?', ['List', 'Text Separated by space'])
        values3 = st.text_area("Enter List of values 3")
        
        if(list_yn == 'List'):
            if(st.checkbox('Confirm List 3')==True): 
                values3 = eval(values3)
                st.write(values3)
                
            else:
                st.write('')
        elif(list_yn=='Text Separated by space'):
            values3 = values3.split(' ')
            if(st.checkbox('Show Values 3')==True):
                st.write(values3)
            else:
                st.write('')
                
    st.markdown('### _Generate Code_')
    inp_params = st.text_input("format()")
    
    
    if(st.checkbox('Print Code') == True):
        final = """
for i in range(len(values)):
    st.text(code.format({}))""".format(inp_params)
        exec(final)
    elif(st.checkbox('Copy To Clipboard') == True):
        final = """
s = ''
for i in range(len(values)):
    s = s + code.format({})
pyperclip.copy(s)""".format(inp_params)
        exec(final)
        st.text("Code copied to clipboard")