import streamlit as st
from PIL import Image

# Function to calculate profit percentage
def calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rent):
    total_expenses = tractor_rent + weighing_machine_rent + labour_rent + other_rent
    total_income = sugarcane_quantity * sugarcane_price
    profit = total_income - total_expenses
    profit_percentage = (profit / total_income) * 100 if total_income != 0 else 0
    return profit, profit_percentage

def main():
    st.sidebar.title("Language Selection")
    language = st.sidebar.selectbox("Select Language / भाषा चुनें", ["English", "हिन्दी"])

    if language == "English":
        st.title("Sugarcane Calculator")
        st.markdown(
            """
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.header("Enter Details")

        sugarcane_quantity = st.number_input("Enter Sugarcane Quantity (in tonnes)", min_value=0.0, step=0.01)
        sugarcane_price = st.number_input("Enter Sugarcane Price (per tonne)", min_value=0.0, step=0.01)
        tractor_rent = st.number_input("Enter Tractor Rent (₹)", min_value=0.0, step=0.01)
        weighing_machine_rent = st.number_input("Enter Weighing Machine Rent (₹)", min_value=0.0, step=0.01)
        labour_rent = st.number_input("Enter Labour Rent (₹)", min_value=0.0, step=0.01)
        other_rent = st.number_input("Enter Other Rent (₹)", min_value=0.0, step=0.01)
        calculate_button = "Calculate"

    elif language == "हिन्दी":
        st.title("गन्ना कैलकुलेटर")
        st.markdown(
            """
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.header("विवरण दर्ज करें")

        sugarcane_quantity = st.number_input("गन्ने की मात्रा दर्ज करें (टन में)", min_value=0.0, step=0.01)
        sugarcane_price = st.number_input("गन्ने की कीमत दर्ज करें (प्रति टन)", min_value=0.0, step=0.01)
        tractor_rent = st.number_input("ट्रैक्टर किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        weighing_machine_rent = st.number_input("तौल पंक्ति किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        labour_rent = st.number_input("श्रमिक किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        other_rent = st.number_input("अन्य किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01)
        calculate_button = "गणना करें"

    if st.button(calculate_button):
        profit, profit_percentage = calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rent)
        if language == "English":
            st.success(f"Profit: ₹ {profit:.2f}")
            st.success(f"Profit Percentage: {profit_percentage:.2f} %")
        elif language == "हिन्दी":
            st.success(f"लाभ: ₹ {profit:.2f}")
            st.success(f"लाभ प्रतिशत: {profit_percentage:.2f} %")

        # Display image of happy farmers
        try:
            image = Image.open("happy_farmers.jpg")
            st.image(image, caption='Happy Farmers / खुशहाल किसान', use_column_width=True)
        except Exception as e:
            st.error("Image not found: happy_farmers.jpg")

if __name__ == "__main__":
    main()
