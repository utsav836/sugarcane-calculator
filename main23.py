import streamlit as st
import sqlite3

# Function to create SQLite connection and table
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

# Function to create a table in SQLite
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS Sugarcane (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                net_weight REAL NOT NULL,
                rate1 REAL NOT NULL,
                rate2 REAL NOT NULL,
                cane_rate REAL NOT NULL,
                final_amount REAL NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error creating table: {e}")

# Function to insert data into SQLite
def insert_data(conn, net_weight, rate1, rate2, cane_rate, final_amount):
    try:
        c = conn.cursor()
        c.execute("""
            INSERT INTO Sugarcane (net_weight, rate1, rate2, cane_rate, final_amount)
            VALUES (?, ?, ?, ?, ?)
        """, (net_weight, rate1, rate2, cane_rate, final_amount))
        conn.commit()
        st.success("Data inserted successfully into the database!")
    except sqlite3.Error as e:
        st.error(f"Error inserting data: {e}")

# Function to fetch all data from SQLite
def fetch_data(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Sugarcane")
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        st.error(f"Error fetching data: {e}")
        return []

# Function to display data
def print_data(rows):
    if not rows:
        st.warning("No data found in the database!")
    else:
        st.header("Stored Data")
        for row in rows:
            st.write(f"ID: {row[0]}, Net Weight: {row[1]}, Rate 1: {row[2]}, Rate 2: {row[3]}, Cane Rate: {row[4]}, Final Amount: {row[5]}")

# Function to calculate final amount
def sugarcane_calculator(net_weight, rate1, rate2, cane_rate):
    # Calculate amounts based on provided formulas
    cane_amount = net_weight * cane_rate
    amount1 = net_weight * rate1
    amount2 = net_weight * rate2
  

   
    final_amount = cane_amount - (amount2 - amount1)
    
    return final_amount

# Main function for Streamlit app
def main():
    st.title("Sugarcane Calculator with Database")

    # Create or connect to SQLite database
    conn = create_connection("sugarcane.db")

    if conn is not None:
        # Create table if not exists
        create_table(conn)

        # Language selection
        language = st.selectbox("Select Language / भाषा चुनें", ["English", "हिन्दी"], index=0)

        if language == "English":
            st.header("Enter Details")

            # Input fields
            net_weight = st.number_input("Enter Net Weight (in quintals)", min_value=0.0, step=0.01)
            cane_rate = st.number_input("Enter Cane Rate", min_value=0.0, step=0.01)
            rate1 = st.number_input("Enter Rate 1", min_value=0.0, step=0.01)
            rate2 = st.number_input("Enter Rate 2", min_value=0.0, step=0.01)
           

            calculate_button = st.button("Calculate")

            if calculate_button:
                # Calculate final amount
                final_amount = sugarcane_calculator(net_weight, rate1, rate2, cane_rate)

                # Print final amount
                st.success(f"Final Amount: {final_amount:.2f}")

                # Insert data into SQLite
                insert_data(conn, net_weight, rate1, rate2, cane_rate, final_amount)

                # Print data from SQLite
                rows = fetch_data(conn)
                print_data(rows)

        elif language == "हिन्दी":
            st.header("विवरण दर्ज करें")

            # Input fields
            net_weight = st.number_input("वजन दर्ज करें (क्विंटल में)", min_value=0.0, step=0.01)
            rate1 = st.number_input("दर 1 दर्ज करें", min_value=0.0, step=0.01)
            rate2 = st.number_input("दर 2 दर्ज करें", min_value=0.0, step=0.01)
            cane_rate = st.number_input("गन्ने की दर दर्ज करें", min_value=0.0, step=0.01)

            calculate_button = st.button("गणना करें")

            if calculate_button:
                # Calculate final amount
                final_amount = sugarcane_calculator(net_weight, rate1, rate2, cane_rate)

                # Print final amount
                st.success(f"अंतिम राशि: {final_amount:.2f}")

                # Insert data into SQLite
                insert_data(conn, net_weight, rate1, rate2, cane_rate, final_amount)

                # Print data from SQLite
                rows = fetch_data(conn)
                print_data(rows)

    else:
        st.error("Failed to connect to SQLite database.")

    # Close SQLite connection
    if conn:
        conn.close()

if __name__ == "__main__":
    main()
