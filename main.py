import streamlit as st
from PIL import Image

# Function to calculate profit percentage
def calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rents):
    # Sum up all the other rents
    total_expenses = tractor_rent + weighing_machine_rent + labour_rent + sum(other_rents)
    total_income = sugarcane_quantity * sugarcane_price
    profit = total_income - total_expenses 
    labour_rent_total = labour_rent * sugarcane_quantity  # Correcting labour rent calculation
    profit_percentage = (profit / total_income) * 100 if total_income != 0 else 0
    return profit, profit_percentage, labour_rent_total

def main():
    # Sidebar for language selection
    st.sidebar.title("Language Selection")
    language = st.sidebar.selectbox("Select Language / भाषा चुनें", ["English", "हिन्दी"])

    # Display the UI in English or Hindi based on the user's selection
    if language == "English":
        st.title("Sugarcane Calculator")
        st.markdown("""
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            </style>
            """, unsafe_allow_html=True)

        st.header("Enter Details")

        # English input fields
        sugarcane_quantity = st.number_input("Enter Sugarcane Quantity (in tonnes)", min_value=0.0, step=0.01)
        sugarcane_price = st.number_input("Enter Sugarcane Price (per tonne)", min_value=0.0, step=0.01)
        tractor_rent = st.number_input("Enter Tractor Rent (₹)", min_value=0.0, step=0.01)
        weighing_machine_rent = st.number_input("Enter Weighing Machine Rent (₹)", min_value=0.0, step=0.01)
        labour_rent = st.number_input("Enter Labour Rent (₹)", min_value=0.0, step=0.01)

        # Handle multiple other rent inputs
        other_rent_count = st.number_input("How many other rents?", min_value=0, step=1)
        other_rents = []
        for i in range(int(other_rent_count)):
            rent = st.number_input(f"Enter Other Rent {i + 1} (₹)", min_value=0.0, step=0.01)
            other_rents.append(rent)

        calculate_button = "Calculate"

    elif language == "हिन्दी":
        st.title("गन्ना कैलकुलेटर")
        st.markdown("""
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            </style>
            """, unsafe_allow_html=True)

        st.header("विवरण दर्ज करें")

        # Hindi input fields
        sugarcane_quantity = st.number_input("गन्ने की मात्रा दर्ज करें (टन में)", min_value=0.0, step=0.01)
        sugarcane_price = st.number_input("गन्ने की कीमत दर्ज करें (प्रति टन)", min_value=0.0, step=0.01)
        tractor_rent = st.number_input("ट्रैक्टर किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        weighing_machine_rent = st.number_input("तौल पंक्ति किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        labour_rent = st.number_input("श्रमिक किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)

        # Handle multiple other rent inputs
        other_rent_count = st.number_input("कितने अन्य किराए हैं?", min_value=0, step=1)
        other_rents = []
        for i in range(int(other_rent_count)):
            rent = st.number_input(f"अन्य किराया {i + 1} (₹ में)", min_value=0.0, step=0.01)
            other_rents.append(rent)

        calculate_button = "गणना करें"

    # Calculation and result display when button is pressed
    if st.button(calculate_button):
        profit, profit_percentage, labour_rent_total = calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rents)

        if language == "English":
            st.success(f"Profit: ₹ {profit:.2f}")
            st.success(f"Profit Percentage: {profit_percentage:.2f} %")
            st.success(f"Total Labour Rent: ₹ {labour_rent_total:.2f}")
        elif language == "हिन्दी":
            st.success(f"लाभ: ₹ {profit:.2f}")
            st.success(f"लाभ प्रतिशत: {profit_percentage:.2f} %")
            st.success(f"कुल श्रमिक किराया: ₹ {labour_rent_total:.2f}")

        # Display image of happy farmers (ensure the image exists or change path)
        try:
            image = Image.open("happy_farmers.jpg")
            st.image(image, caption='Happy Farmers / खुशहाल किसान', use_column_width=True)
        except Exception as e:
            st.error("Image not found: happy_farmers.jpg")

if __name__ == "__main__":
    main()
