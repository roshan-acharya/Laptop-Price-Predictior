import pickle
import streamlit as st
import pandas as pd
from pathlib import Path
import pickle

model_path = Path.cwd() / "model.pkl"

#create streamlit app with dunction 
def Price(input_data):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    #load data
    input_df= pd.DataFrame(data=[input_data], columns=['Brand', 'Series', 'Processor', 'Ram', 'Storage', 'Graphics'])
    return model.predict(input_df)[0]

def streamlit_app():
    st.title("Laptop Price Prediction")
    st.write("This is a web application to predict laptops Price.")
    #create dropdown select item
    st.write("Select the laptop brand:")
    brand = st.selectbox("Brand", ['ASUS', 'Acer', 'Lenovo', 'ACER', 'HP', 'Apple', 'LENOVO', 'Dell',
       'Hewlett-Packard (HP)', 'DELL', 'MSI'])
    st.write("Select the laptop series:")
    series = st.selectbox("Series", ['TUF Series', 'TUF Gaming A15', 'Predator Series',
       'IdeaPad Series', 'Nitro V 15', 'Aspire Lite Series', 'LOQ Series',
       'Aspire Series', 'Spectre Series', 'Pavilion Series',
       'MacBook Pro', 'ROG Strix Series', 'ThinkPad E14', 'Gaming Series',
       'VivoBook Series', 'MacBook Air', 'Legion Series',
       'Inspiron Series', 'Swift Series', 'VivoBook', 'Victus',
       'LOQ 15IRH8 Series', 'V Series', 'Vostro Series',
       '\xa0TP3402-lZ26W (2-in-1)', 'Gaming Laptop Series', 'INSPIRON',
       'Victus Gaming Series', 'ZenBook Series', 'Notebook',
       'IdeaPad Slim 3 Series', 'XPS Series', 'Nitro V 15 Series',
       'Nitro V Series', 'XPS', 'Extensa Series', 'Nitro Series',
       'GF63 Series', 'M4 Series', 'Cyborg Series', 'ZENBOOK', 'Omen',
       'Nitro 5', 'Alienware', 'Latitude Series', 'ThinkPad L14',
       'Modern 15', 'V Gaming Series', 'Yoga Series', 'TUF Gaming Series',
       'Zenbook UM3402YA', 'Summit Series', 'Victus Series',
       'Predator Triton Series', 'LOQ Gaming Series', 'Envy x360',
       'VivoBook Go Series', 'VIVOBOOK', 'Envy Series',
       'MacBook (M3 Air Chip)', 'V15 G3', 'Delta', 'IdeaPad V15-IGL',
       'Alienware Series', 'MacBook Pro Series (M3 Chip)',
       'Alienware x14', 'MacBook Pro (M3 Pro Chip)', 'ASPIRE 5',
       'Vicuts Series', 'Envy', 'Ideapad Series', 'ZenBook Duo Series',
       'ROG Zephyrus Series', 'Nitro 5 Series', 'Legion Slim 5 Series',
       'IDEAPAD', 'GP66', 'Slim 7 Series', 'IdeaPad Series (14IAU8)',
       'Modern Series', 'GL', 'Predator Helios Neo 16', 'Vivobook K3405V',
       'Pavilion Plus Series', 'Wyse', 'Business Series',
       'Notebook Series', 'ThinkBook Series', 'Pavilion', 'KATANA',
       'MacBook Air\xa0', 'Nitro', 'EliteBook Series'])
    st.write("Select the laptop processor:")
    processor = st.selectbox("Processor", ['i7', 'AMD Ryzen 7', 'Intel Core i5', 'Intel Core i7',
       'Intel Core i9', 'AMD Ryzen 5', 'Intel Core i3', 'Intel Celeron',
       'i5', 'AMD Ryzen', 'AMD Ryzen 3', 'AMD Ryzen 9', 'AMD Ryzen ',
       'Intel core i5'])
    st.write("Select the laptop RAM:")
    ram = st.selectbox("RAM", ["16.",  "8.", "24.", "32.",  "4.", "20.", "12."])
    st.write("Select the laptop storage:")
    storage = st.selectbox("Storage", ["512.", "256."])
    st.write("Select the laptop graphics:")
    graphics = st.selectbox("Graphics", ['No', ' NVIDIA GeForce RTX 4060 8GB ',
       ' NVIDIA GeForce RTX 4050 6GB ', ' Intel UHD ',
       ' NVIDIA RTX 3050 6GB ', ' AMD Radeon ',
       ' NVIDIA GeForce RTX 4070 8GB ', ' NVIDIA RTX 4050 ',
       ' NVIDIA GeForce RTX 3050 4GB ', ' NVIDIA GeForce RTX 2050 4GB ',
       ' AMD Radeon 610M ', ' Intel Arc ', ' NVIDIA RTX 3050Ti ',
       ' AMD Radeon RX 6550M 4GB ', ' Intel Iris Xe ', 'NVIDIA RTX 3050 ',
       ' NVIDIA RTX 2050 4GB ', ' RTX 4050 6GB GDDR6 ',
       ' NVIDIA GeForce RTX 2050 4GB GDDR6 ',
       ' Dedicated NVIDIA GeForce RTX 4060 8GB ', ' NVIDIA RTX 3050 ',
       ' ', ' NVIDIA RTX 4060 8GB ', ' NVIDIA RTX 3060 ',
       ' NVIDIA RTX 3070 ', ' Intel Integrated ', ' NVIDIA RTX 4050 6GB ',
       ' NVIDIA GeForce RTX 3060 6GB GDDR6 ', ' RTX 3050 6GB ',
       ' NVIDIA GeForce RTX 4050 ', ' Intel ',
       ' NVIDIA GeForce RTX 3050 6GB ', ' lntel UHD ',
       ' Integrated Intel UHD ', ' NVIDIA GeForce RTX 4080 12GB ',
       ' AMD RX6700M ', ' NVIDIA GeForce RTX 4070 8GB GDDR6 ',
       ' RTX 4060 8GB ', ' NVIDIA GeForce RTX 4060 8GB GDDR6 ',
       ' Integrated Intel ', ' RTX 2050 4GB ',
       ' NVIDIA GeForce RTX 4080 8GB ', 'NVIDIA RTX 3050Ti ', ' 890M ',
       ' NVIDIA GeForce MX550 2GB ', ' NVIDIA GeForce RTX 2050 ',
       ' NVIDIA RTX 3070Ti 8GB ', ' RTX4060 8GB ', ' RTX 4050 6GB ',
       ' Integrated Intel Iris Xe ', ' GeForce MX550 2GB Dedicated ',
       ' NVIDIA GeForce RTX 4090 16GB '])

#xonvert ram and ssd to float
    ram = float(ram.replace(".", ""))
    storage = float(storage.replace(".", ""))


#buttpn for prediction
    if st.button("Predict Price"):
        input_data = {
         'Brand': brand,
         'Series': series,
         'Processor': processor,
         'Ram': ram,
         'Storage': storage,
         'Graphics': graphics
     }
    #call function
    
    #predict price
        price = Price(input_data)
        st.write(f"The predicted price of the laptop is: {price}")

if __name__ == '__main__':
    streamlit_app()

        

