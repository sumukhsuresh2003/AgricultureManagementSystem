import streamlit as st
import pymysql

# Database Functionality
def execute_query(query, params=None, fetch=True, multi=False):
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='checkonyoursys',
        database='agriculturedb'
    )

    cursor = db.cursor(pymysql.cursors.DictCursor)
    
    # Use executemany() for multiple statements
    if multi:
        cursor.executemany(query, params)
    else:
        cursor.execute(query, params)

    if query.strip().split()[0].upper() in ('INSERT', 'UPDATE', 'DELETE'):
        db.commit()

    result = cursor.fetchall() if fetch else None
    cursor.close()
    db.close()
    return result

# Stored Procedures
def calculate_total_sales(crop_id):
    query = 'CALL CalculateTotalSales(%s)'
    params = [(crop_id,)]  
    return execute_query(query, params, multi=True)

def calculate_days_to_harvest(crop_id):
    query = 'CALL CalculateDaysToHarvest(%s)'
    params = [(crop_id,)] 
    return execute_query(query, params, multi=True)

def insert_maintenance(maintenance_id, planting_date, harvest_date):
    query = 'INSERT INTO MAINTENANCE (maintenanceSerialNum, plantingDate, harvestDate) VALUES (%s, %s, %s)'
    params = (maintenance_id, planting_date, harvest_date)
    execute_query(query, params)  # Execute the query

def insert_crop(crop_id, crop_name, crop_type, maintenance_id):
    # Check if maintenance_id exists in the MAINTENANCE table
    check_query = 'SELECT COUNT(*) AS count FROM MAINTENANCE WHERE maintenanceSerialNum = %s'
    check_params = (maintenance_id,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        query = 'INSERT INTO CROP (cropId, cropName, cropType, maintenanceId) VALUES (%s, %s, %s, %s)'
        params = (crop_id, crop_name, crop_type, maintenance_id)
        execute_query(query, params) 
        # Log the insertion in the MAINTENANCE_LOG table
        log_query = 'INSERT INTO MAINTENANCE_LOG (maintenanceSerialNum, operation) VALUES (%s, %s)'
        log_params = (maintenance_id, 'INSERT')
        execute_query(log_query, log_params)

        st.success('Crop inserted successfully!')
    else:
        st.error('Error: Maintenance record does not exist. Please insert into MAINTENANCE table first.')

# Streamlit App
def main():
    st.title('Agriculture Management System')

    # Insert Maintenance Section
    st.header('Insert Maintenance (Before Crop Insertion)')
    maintenance_id_insert = st.number_input('Enter Maintenance ID for Insert:', step=1)
    planting_date_insert = st.date_input('Enter Planting Date for Insert:')
    harvest_date_insert = st.date_input('Enter Harvest Date for Insert:')

    if st.button('Insert Maintenance'):
        try:
            insert_maintenance(maintenance_id_insert, planting_date_insert, harvest_date_insert)
            st.success('Maintenance record inserted successfully!')
        except pymysql.err.IntegrityError as e:
            st.error(f'Error: {e}')

    # Insert Crop Section
    st.header('Insert Crop (After Maintenance Insertion)')
    crop_id_insert = st.number_input('Enter Crop ID for Insert:', step=1)
    crop_name_insert = st.text_input('Enter Crop Name for Insert:')
    crop_type_insert = st.text_input('Enter Crop Type for Insert:')

    if st.button('Insert Crop'):
        try:
            insert_crop(crop_id_insert, crop_name_insert, crop_type_insert, maintenance_id_insert)
        except pymysql.err.IntegrityError as e:
            st.error(f'Error: {e}')

    # Calculate Total Sales Section
    st.header('Calculate Total Sales for a Crop')
    crop_id_total_sales = st.number_input('Enter Crop ID for Total Sales:', step=1)
    if st.button('Calculate Total Sales'):
        total_sales_result = calculate_total_sales(crop_id_total_sales)
        st.success(f'Total Sales for Crop {crop_id_total_sales}: {total_sales_result[0]["totalSales"]}' if total_sales_result else 'Error calculating total sales.')

    # Calculate Days to Harvest Section
    st.header('Calculate Days to Harvest for a Crop')
    crop_id_days_to_harvest = st.number_input('Enter Crop ID for Days to Harvest:', step=1)
    if st.button('Calculate Days to Harvest'):
        days_to_harvest_result = calculate_days_to_harvest(crop_id_days_to_harvest)
        st.success(f'Days to Harvest for Crop {crop_id_days_to_harvest}: {days_to_harvest_result[0]["DaysToHarvest"]}' if days_to_harvest_result else 'Error calculating days to harvest.')

if __name__ == '__main__':
    main()
