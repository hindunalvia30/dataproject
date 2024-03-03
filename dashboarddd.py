import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.set_option('deprecation.showPyplotGlobalUse', False)

csv_url = "https://raw.githubusercontent.com/hindunalvia30/dataproject/main/orderpayment2.csv"
order_payment_df = pd.read_csv(csv_url)

csv_url2 = "https://raw.githubusercontent.com/hindunalvia30/dataproject/main/orderreview2.csv"
order_review_df = pd.read_csv(csv_url2)

csv_url3 = "https://raw.githubusercontent.com/hindunalvia30/dataproject/main/customers2.csv"
customers_df = pd.read_csv(csv_url3)


# Menambahkan logo
with st.sidebar:
    st.title("Dashboard Analysis E-commerce Dataset")
    st.write("Welcome to our e-commerce dashboard!")
    st.image("https://github.com/hindunalvia30/dataproject/raw/12a569bc8f5faa7b3f044726c6f123d19f4fffb3/ecommerce.jpeg")

    


# Fungsi untuk membuat histogram Jumlah Pembayaran
def create_histogram(data):
    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=range(0, 1000), color='black', edgecolor='blue')
    plt.title('Amount Payment by Number of Purchases')
    plt.xlabel('Amount Payment')
    plt.ylabel('Number of Purchases')
    plt.grid(True)
    st.pyplot()

    st.markdown("<p>Berdasarkan hasil visualisasi, terlihat bahwa range jumlah pembayaran yang sering dibayarkan customer adalah 0-200 dollar.</p>", 
                unsafe_allow_html=True)

# Fungsi untuk membuat bar chart review scores
def create_review_score_plot(data):
    review_scores = data['review_score'].value_counts().sort_values(ascending=False)
    most_score = review_scores.idxmax()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=review_scores.index, 
                y=review_scores.values, 
                order=review_scores.index,
                hue=review_scores.index,
                palette=["blue" if score == most_score else "blue" for score in review_scores.index]
                )

    plt.title("Customer Satisfaction Based on Review Score", fontsize=20)
    plt.xlabel("Review Score")
    plt.ylabel("Customer Count")
    plt.xticks(fontsize=15)
    st.pyplot()
    st.markdown("<p>Berdasarkan hasil visualisasi dapat dilihat bahwa tingkat kepuasan customers adalah memuaskan karena customers yang memberikan review score 5 sangat banyak, disusul dengan review score 4 pada posisi kedua.</p>", 
                unsafe_allow_html=True)

# Fungsi untuk membuat bar chart customer states
def create_customer_state_plot(data):
    state_customer = data['customer_state'].value_counts().sort_values(ascending=False)
    most_common_state = state_customer.idxmax()

    plt.figure(figsize=(10, 5))
    colors_ = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"]
    sns.barplot(
        x=state_customer.values,  
        y=state_customer.index,
        hue=state_customer.index,  
        palette=colors_,
        legend=False   
    )
    plt.title("Number of Customer by States", loc="center", fontsize=15)
    plt.ylabel("Customer State")  
    plt.xlabel("Number of Customers")  
    plt.xticks(fontsize=12, rotation=45)  
    plt.yticks(fontsize=8)
    st.pyplot()
    st.markdown("<p>Berdasarkan hasil visualisasi, terlihat bahwa negara bagian yang memiliki jumlah customers tertinggi adalah SP dan negara bagian yang memiliki jumlah customers terendah adalah AC, AP dan RR. </p>", 
                unsafe_allow_html=True)


# Main Streamlit app
def main():
    st.title('Dashboard Analysis E-commerce Dataset')

    # Menampilkan histogran payment amount
    st.subheader('Histogram of Payment Amounts')
    create_histogram(order_payment_df['payment_value'])

    # Menampilkan bar chart review scores
    st.subheader('Customer Satisfaction Based on Review Score')
    create_review_score_plot(order_review_df)

    # Menampilkan bar chart customer states
    st.subheader('Number of Customers by States')
    create_customer_state_plot(customers_df)

if __name__ == '__main__':
    main()

st.caption('Dashboard by Hindun Alvia Rosyaada')
