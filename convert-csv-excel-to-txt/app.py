import streamlit as st
import pandas as pd

# Function to convert CSV or Excel file to TXT
def convert_to_txt(file, separator):
    if file is not None:
        try:
            if file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                df = pd.read_excel(file)
            else:
                df = pd.read_csv(file, sep=separator)
            
            txt_content = df.to_string(index=False, header=False)
            return txt_content
        except Exception as e:
            return str(e)
    else:
        return None

def main():
    st.title("CSV/Excel to TXT Converter")
    
    # Add sidebar with information
    st.sidebar.title("Info")
    st.sidebar.write("This app converts CSV or Excel files to TXT.")
    
    # Buttons for CSV and Excel
    file_type = st.radio("Select File Type", ("CSV", "Excel"))
    
    allowed_types = {"CSV": ["csv"], "Excel": ["xlsx", "xls"]}
    file_extensions = allowed_types[file_type]
    
    st.write("Upload a {} file to convert it into a TXT file.".format(file_type))
    
    file = st.file_uploader("Choose a {} file".format(file_type), type=file_extensions)
    
    if file is not None:
        separator = st.text_input("Separator (for CSV files)", ",")
        converted_txt = convert_to_txt(file, separator)
        
        if converted_txt:
            st.write("Converted TXT content:")
            st.text_area("TXT Content", converted_txt)
            
            # Display button to show the converted content
            if st.button("Display"):
                st.write("Displaying the content below:")
                st.code(converted_txt)
                
            # Download button to save the converted content as .txt
            if st.button("Download"):
                st.download_button(
                    label="Download TXT File",
                    data=converted_txt.encode("utf-8"),
                    file_name="converted.txt",
                    mime="text/plain"
                )
        else:
            st.write("Error converting the file.")

if __name__ == "__main__":
    main()
