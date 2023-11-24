
################
import streamlit as st
import mysql.connector
import pandas as pd

# Function to execute SQL query and fetch data
def execute_query(query, params=None):
    # Connect to your MySQL database
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='checkonyoursys',
        database='agriculturedb'
    )

    cursor = db.cursor(dictionary=True)  # Use dictionary cursor to get column names
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    db.close()  # Close the database connection
    return result

# Streamlit app
def main():
    st.title('Agriculture Database')

    # Button to display all crops
    if st.button('Display All Crops'):
        st.header('All Crops')
        query_all_crops = 'SELECT * FROM CROP'
        crops = execute_query(query_all_crops)
        display_query_results(crops)

    # Selectbox for condition-based search (Crops by Type)
    selected_crop_type = st.selectbox('Select Crop Type:', get_all_crop_types(), key='crops_by_type')
    st.header(f'Crops by Type: {selected_crop_type}')

    # Perform the query based on the selected crop type
    results = get_crops_by_type(selected_crop_type)
    display_query_results(results)

    # Selectbox for condition-based search (Equipment for Crops with Type)
    selected_crop_type_equipment = st.selectbox('Select Crop Type for Equipment:', get_all_crop_types(), key='equipment_by_type')
    st.header(f'Equipment for Crops with Type: {selected_crop_type_equipment}')

    # Perform the query based on the selected crop type for equipment
    results_equipment = get_equipment_for_crops_with_type(selected_crop_type_equipment)
    display_query_results(results_equipment)

    # Button for correlated query (Crops with Total Sales)
    if st.button('Crops with Total Sales'):
        st.header('Crops with Total Sales')
        results = get_crops_with_total_sales()
        display_query_results(results)

    # Button for aggregated query (Total Salary for Labourers)
    if st.button('Total Salary for Labourers'):
        st.header('Total Salary for Labourers')
        results = get_total_salary_for_laborers()
        display_query_results(results)

     # Button for the new query (Crops without Sales)
    if st.button('Crops without Sales'):
        st.header('Crops without Sales')
        results = get_crops_without_sales()
        display_query_results(results)

    # Nested Query Section
    st.header('Nested Query: Crops with Sales Quantity Greater Than Threshold')
    sales_threshold = st.number_input('Enter Sales Quantity Threshold:', min_value=0, step=1, value=100)
    if st.button('Find Crops'):
        nested_query_results = get_crops_with_sales_greater_than_threshold(sales_threshold)
        display_query_results(nested_query_results)

def get_crops_with_sales_greater_than_threshold(threshold):
    query = '''
    SELECT c.cropId, c.cropName, c.cropType, m.plantingDate, m.harvestDate
    FROM CROP c
    JOIN MAINTENANCE m ON c.maintenanceId = m.maintenanceSerialNum
    WHERE c.cropId IN (
        SELECT s.cropId
        FROM SALES s
        WHERE s.quantity > %s
    )
    '''
    return execute_query(query, (threshold,))

def get_all_crop_types():
    query = 'SELECT DISTINCT cropType FROM CROP'
    result = execute_query(query)
    return [row['cropType'] for row in result]

def get_crops_by_type(crop_type):
    query = '''
    SELECT c.cropId, c.cropName, c.cropType, m.plantingDate, m.harvestDate
    FROM CROP c
    JOIN MAINTENANCE m ON c.maintenanceId = m.maintenanceSerialNum
    WHERE c.cropType = %s
    '''
    return execute_query(query, (crop_type,))

def get_equipment_for_crops_with_type(crop_type):
    query = '''
    SELECT e.equipmentId, e.model, e.versionNum, e.equipmentCost, e.deviceId
    FROM EQUIPMENT e
    JOIN CROP c ON e.deviceId = c.cropId
    WHERE c.cropType = %s
    '''
    return execute_query(query, (crop_type,))

def get_crops_with_total_sales():
    query = '''
    SELECT c.cropId, c.cropName, c.cropType, SUM(s.quantity) as totalSales
    FROM CROP c
    LEFT JOIN SALES s ON c.cropId = s.cropId
    GROUP BY c.cropId, c.cropName, c.cropType
    '''
    return execute_query(query)

def get_total_salary_for_laborers():
    query = '''
    SELECT SUM(salaryPerWeek) as totalSalary
    FROM LABOURER
    '''
    return execute_query(query)

def get_crops_without_sales():
    query = '''
    SELECT c.cropId, c.cropName, c.cropType, m.plantingDate, m.harvestDate
    FROM CROP c
    JOIN MAINTENANCE m ON c.maintenanceId = m.maintenanceSerialNum
    WHERE NOT EXISTS (
        SELECT 1
        FROM SALES s
        WHERE s.cropId = c.cropId
    )
    '''
    return execute_query(query)

def display_query_results(results):
    if results:
        # Display results in a dataframe with column headings
        if 'totalSalary' in results[0]:
            st.write(f'Total Salary for Labourers: {results[0]["totalSalary"]}')
        else:
            df = pd.DataFrame(results)
            st.dataframe(df)
    else:
        st.info('No results found.')


if __name__ == '__main__':
    main()
