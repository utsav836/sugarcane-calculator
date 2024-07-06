import streamlit as st


def sugarcane_calculator(net_weight, rate1, rate2, cane_rate):
    # Calculate amounts based on provided formulas
    amount1 = net_weight * rate1
    amount2 = net_weight * rate2
    amount = amount1 - amount2
    cane_amount = net_weight * cane_rate
    final_amount = cane_amount - amount
    
    return final_amount


def calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rent):
    # Calculate total revenue and total expenses
    total_revenue = sugarcane_quantity * sugarcane_price
    total_expenses = tractor_rent + weighing_machine_rent + labour_rent + other_rent
    
    # Calculate profit and profit percentage
    profit = total_revenue - total_expenses
    profit_percentage = (profit / total_revenue) * 100 if total_revenue != 0 else 0
    
    return profit, profit_percentage


def main():
    st.title("Sugarcane Calculator / गन्ना कैलकुलेटर")
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

    # Language Selection
    language = st.selectbox("Select Language / भाषा चुनें", ["English", "हिन्दी"])

    if language == "English":
        st.header("Enter Details")

        # Number inputs with min_value and step parameters
        sugarcane_quantity = st.number_input("Enter Sugarcane Quantity (in tonnes)", min_value=0.0, step=0.01, format='%f')
        sugarcane_price = st.number_input("Enter Sugarcane Price (per tonne)", min_value=0.0, step=0.01, format='%f')
        tractor_rent = st.number_input("Enter Tractor Rent (₹)", min_value=0.0, step=0.01, format='%f')
        weighing_machine_rent = st.number_input("Enter Weighing Machine Rent (₹)", min_value=0.0, step=0.01, format='%f')
        labour_rent = st.number_input("Enter Labour Rent (₹)", min_value=0.0, step=0.01, format='%f')
        other_rent = st.number_input("Enter Other Rent (₹)", min_value=0.0, step=0.01, format='%f')
        calculate_button = "Calculate"

    elif language == "हिन्दी":
        st.header("विवरण दर्ज करें")

        # Number inputs with min_value and step parameters
        sugarcane_quantity = st.number_input("गन्ने की मात्रा दर्ज करें (टन में)", min_value=0.0, step=0.01, format='%f')
        sugarcane_price = st.number_input("गन्ने की कीमत दर्ज करें (प्रति टन)", min_value=0.0, step=0.01, format='%f')
        tractor_rent = st.number_input("ट्रैक्टर किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01, format='%f')
        weighing_machine_rent = st.number_input("तौल पंक्ति किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01, format='%f')
        labour_rent = st.number_input("श्रमिक किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01, format='%f')
        other_rent = st.number_input("अन्य किराया दर्ज करें (₹ में)", min_value=0.0, step=0.01, format='%f')
        calculate_button = "गणना करें"

    if st.button(calculate_button):
        profit, profit_percentage = calculate_profit(sugarcane_quantity, sugarcane_price, tractor_rent, weighing_machine_rent, labour_rent, other_rent)
        if language == "English":
            st.success(f"Profit: ₹ {profit:.2f}")
            st.success(f"Profit Percentage: {profit_percentage:.2f} %")
        elif language == "हिन्दी":
            st.success(f"लाभ: ₹ {profit:.2f}")
            st.success(f"लाभ प्रतिशत: {profit_percentage:.2f} %")


if __name__ == "__main__":
    main()
