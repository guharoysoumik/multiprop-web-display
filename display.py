import streamlit as st
import json
import pandas as pd

# Function to load and display JSON data
def read_json():
    # File paths
    each_run_file_name = f"./cluster_analysis/{st.session_state.i_design}/each_property_info_1hr.json"
    cluster_run_file_name = f"./cluster_analysis/{st.session_state.i_design}/cluster_abc_run_info.json"
    cluster_gain_file_name = f"./cluster_analysis/{st.session_state.i_design}/cluster_gain.json"

    # Create sections to organize data
    st.write(f"### 📂 Data Overview for Design: `{st.session_state.i_design}`")
    st.markdown("---")

    try:
        # Display "Each Property Run" data
        with open(each_run_file_name, 'r') as stream:
            data = json.load(stream)
        st.subheader("🏠 Each Property Run (1 Hour)")
        csv_data = pd.DataFrame(data)
        st.dataframe(csv_data, use_container_width=True)
        st.markdown("---")

        # Display "Cluster Run" data
        with open(cluster_run_file_name, 'r') as stream:
            data = json.load(stream)
        st.subheader("🔗 Cluster Run Information")
        csv_data = pd.DataFrame(data)
        st.dataframe(csv_data, use_container_width=True)
        st.markdown("---")

        # Display "Cluster Gain Info" data
        with open(cluster_gain_file_name, 'r') as stream:
            data = json.load(stream)
        st.subheader("📈 Details of Cluster Gain Information ")
        csv_data = pd.DataFrame(data)
        st.dataframe(csv_data, use_container_width=True)
        st.markdown("---")

    except FileNotFoundError:
        st.error("❌ Unable to open file. Please check the file paths or the selected design.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

# Sidebar to select design
st.sidebar.header("🎨 Select Design")
design_options = ["6s404", "6s138", "6s169", "6s267", "bob12m05m", "sm98tcas16tmulti"]
st.sidebar.selectbox(
    "Choose a design name:",
    design_options,
    index=0,
    on_change=read_json,
    key='i_design'
)
