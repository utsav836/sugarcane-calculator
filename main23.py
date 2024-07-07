import streamlit as st
import sqlite3

# Function to calculate sugarcane amounts
def sugarcane_calculator(net_weight, rate1, rate2, cane_rate):
    cane_amount = net_weight * cane_rate
    amount1 = net_weight * rate1
    amount2 = net_weight * rate2
    amount = amount2 - amount1
    final_amount = cane_amount - amount
    return amount1, amount2, amount, cane_amount, final_amount

# Function to create SQLite connection and store results
def store_result(net_weight, rate1, rate2, cane_rate, amount1, amount2, amount, cane_amount, final_amount):
    conn = sqlite3.connect('sugarcane_results.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (net_weight REAL, rate1 REAL, rate2 REAL, cane_rate REAL,
                 amount1 REAL, amount2 REAL, amount REAL, cane_amount REAL, final_amount REAL)''')
    c.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (net_weight, rate1, rate2, cane_rate, amount1, amount2, amount, cane_amount, final_amount))
    conn.commit()
    conn.close()

# Main function to run the Streamlit app
def main():
    st.title("Sugarcane Calculator for Farmers")

    # Language selection
    language = st.selectbox("Select Language / भाषा चुनें", ["English", "Hindi"])

    if language == "Hindi":
        st.subheader("गन्ना कैलकुलेटर किसानों के लिए")
        st.write("कृपया आवश्यक आंकड़े दर्ज करें (एक्सेप्टेड यूनिट्स क्विंटल और रुपये):")
    else:
        st.subheader("Sugarcane Calculator for Farmers")
        st.write("Please enter the necessary values (expected units: quintals and rupees):")

    # Input fields
    net_weight = st.number_input("Net Weight of Sugarcane (in quintals)")
    rate1 = st.number_input("Rate 1 ( in ₹)")
    rate2 = st.number_input("Rate 2 ( in ₹)")
    cane_rate = st.number_input("Cane Rate ( in ₹)")

    # Calculate final amount
    if st.button("Calculate / गणना करें"):
        amount1, amount2, amount, cane_amount, final_amount = sugarcane_calculator(net_weight, rate1, rate2, cane_rate)
        st.write(f"Amount 1: {amount1:.2f} ₹")
        st.write(f"Amount 2: {amount2:.2f} ₹")
        st.write(f"Net Amount: {amount:.2f} ₹")
        st.write(f"Cane Amount: {cane_amount:.2f} ₹")
        st.write(f"Final Amount: {final_amount:.2f} ₹")

        # Store results in SQLite database
        store_result(net_weight, rate1, rate2, cane_rate, amount1, amount2, amount, cane_amount, final_amount)
        st.write("Result stored in database.")

    # Print option
    if st.button("Print / प्रिंट करें"):
        st.write("Printing functionality would go here.")

if __name__ == "__main__":
    main()
