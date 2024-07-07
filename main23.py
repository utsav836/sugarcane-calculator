import streamlit as st
import sqlite3

# Function to calculate sugarcane amounts
def sugarcane_calculator(net_weight, rate1, rate2, cane_rate):
    cane_amount = net_weight * cane_rate
    amount1 = net_weight * rate1
    amount2 = net_weight * rate2
    amount = amount2 + amount1
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
    # Define text elements for both languages
    english_text = {
        'title': "Sugarcane Calculator for Farmers",
        'subheader': "Sugarcane Calculator for Farmers",
        'prompt': "Please enter the necessary values (expected units: quintals and rupees):",
        'labels': {
            'net_weight': "Net Weight of Sugarcane (in quintals)",
            'rate1': "Tractor Rent ( in ₹)",
            'rate2': "Labour Rent ( in ₹)",
            'cane_rate': "Cane Rate ( in ₹)"
        },
        'calculate_button': "Calculate",
        'print_button': "Print",
        'result_stored': "Result stored in database."
    }

    hindi_text = {
        'title': "गन्ना कैलकुलेटर किसानों के लिए",
        'subheader': "गन्ना कैलकुलेटर किसानों के लिए",
        'prompt': "कृपया आवश्यक आंकड़े दर्ज करें (एक्सेप्टेड यूनिट्स क्विंटल और रुपये):",
        'labels': {
            'net_weight': "गन्ने का नेट वजन (क्विंटल में)",
            'rate1': "ट्रैक्टर किराया (₹ में)",
            'rate2': "श्रमिक किराया (₹ में)",
            'cane_rate': "गन्ने की दर (₹ में)"
        },
        'calculate_button': "गणना करें",
        'print_button': "प्रिंट करें",
        'result_stored': "परिणाम डेटाबेस में सहेजा गया।"
    }

    # Language selection
    language = st.selectbox("Select Language / भाषा चुनें", ["English", "Hindi"])

    if language == "English":
        text = english_text
    else:
        text = hindi_text

    st.title(text['title'])
    st.subheader(text['subheader'])
    st.write(text['prompt'])

    # Input fields
    net_weight = st.number_input(text['labels']['net_weight'])
    rate1 = st.number_input(text['labels']['rate1'])
    rate2 = st.number_input(text['labels']['rate2'])
    cane_rate = st.number_input(text['labels']['cane_rate'])

    # Calculate final amount
    if st.button(text['calculate_button']):
        amount1, amount2, amount, cane_amount, final_amount = sugarcane_calculator(net_weight, rate1, rate2, cane_rate)
        st.write(f"Amount 1: {amount1:.2f} ₹")
        st.write(f"Amount 2: {amount2:.2f} ₹")
        st.write(f"Net Amount: {amount:.2f} ₹")
        st.write(f"Cane Amount: {cane_amount:.2f} ₹")
        st.write(f"Final Amount: {final_amount:.2f} ₹")

        # Store results in SQLite database
        store_result(net_weight, rate1, rate2, cane_rate, amount1, amount2, amount, cane_amount, final_amount)
        st.write(text['result_stored'])

    # Print option (placeholder)
    if st.button(text['print_button']):
        st.write("Printing functionality would go here.")

if __name__ == "__main__":
    main()
