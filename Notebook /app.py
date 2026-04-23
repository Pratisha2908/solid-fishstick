import pickle
import pandas as pd
import numpy as np
import streamlit as st
def predict_species(sep_len,sep_width,prt_len,pet_wild,scaler_path,model_path):
    try:
        with open(scaler_path,'rb')as file1:
            scaler = pickle.load(file1)

        with open(model_path,'rb')as file2:
            model = pickle.load(file2)
            
