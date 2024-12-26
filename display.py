import streamlit as st
import json
import pandas as pd

def read_json():
    each_run_file_name="./cluster_analysis/"+st.session_state.i_design+"/each_property_info_1hr.json"
    cluster_run_file_name="./cluster_analysis/"+st.session_state.i_design+"/cluster_abc_run_info.json"
    cluster_gain_file_name="./cluster_analysis/"+st.session_state.i_design+"/cluster_gain.json"
    try:
        with open(each_run_file_name,'r') as stream:
            data=json.load(stream)
        stream.close()
        st.write("## EACH PROPERTY RUN 1 HR")
        csv_data=pd.DataFrame(data)
        st.dataframe(csv_data)

        with open(cluster_run_file_name,'r') as stream:
                data=json.load(stream)
        stream.close()
        st.write("## CLUSTER RUN")
        csv_data=pd.DataFrame(data)
        st.dataframe(csv_data)

        with open(cluster_gain_file_name,'r') as stream:
            data=json.load(stream)
        stream.close()
        st.write("## CLUSTER GAIN INFO")
        csv_data=pd.DataFrame(data)
        st.dataframe(csv_data)
    except Exception:
        print ("Unable to open file")
    

design=st.selectbox("Select Design",["6s404","6s138","6s169","6s267","bob12m05m","sm98tcas16tmulti"],index=None,placeholder="Select a design name",on_change=read_json,key='i_design')
