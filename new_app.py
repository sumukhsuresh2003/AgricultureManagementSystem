import streamlit as st
import mysql.connector
import pandas as pd

# Function to execute SQL query and fetch data
def execute_query(query, params=None, fetch=True):
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='QueSt20$6*ad#4',
        database='agriculturedb'
    )

    cursor = db.cursor(dictionary=True)
    cursor.execute(query, params)

    # Commit the changes if it's an update, insert, or delete operation
    if query.strip().split()[0].upper() in ('INSERT', 'UPDATE', 'DELETE'):
        db.commit()

    result = cursor.fetchall() if fetch else None
    cursor.close()
    db.close()
    return result

# CRUD Operations for MAINTENANCE table
def add_maintenance(serial_num, planting_date, harvest_date):
    query = 'INSERT INTO MAINTENANCE (maintenanceSerialNum, plantingDate, harvestDate) VALUES (%s, %s, %s)'
    params = (serial_num, planting_date, harvest_date)
    execute_query(query, params)

def update_maintenance(serial_num, planting_date, harvest_date):
    # Check if maintenance record exists before updating
    check_query = 'SELECT COUNT(*) AS count FROM MAINTENANCE WHERE maintenanceSerialNum = %s'
    check_params = (serial_num,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        # If maintenance record exists, proceed with the update
        update_query = 'UPDATE MAINTENANCE SET plantingDate = %s, harvestDate = %s WHERE maintenanceSerialNum = %s'
        update_params = (planting_date, harvest_date, serial_num)
        execute_query(update_query, update_params)
        st.success(f'Maintenance with Serial Number {serial_num} updated successfully!')
    else:
        st.error(f'Error: Maintenance record with Serial Number {serial_num} does not exist.')

def delete_maintenance(serial_num):
    # Check if maintenance record exists before deleting
    check_query = 'SELECT COUNT(*) AS count FROM MAINTENANCE WHERE maintenanceSerialNum = %s'
    check_params = (serial_num,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        # If maintenance record exists, proceed with deletion
        delete_query = 'DELETE FROM MAINTENANCE WHERE maintenanceSerialNum = %s'
        delete_params = (serial_num,)
        execute_query(delete_query, delete_params)
        st.success(f'Maintenance with Serial Number {serial_num} deleted successfully!')
    else:
        st.error(f'Error: Maintenance record with Serial Number {serial_num} does not exist.')

def display_all_maintenance():
    query = 'SELECT * FROM MAINTENANCE'
    maintenance = execute_query(query)
    display_query_results(maintenance)

# CRUD Operations for MAINTENANCE_FERTILISERS table
def add_fertilizer(serial_num, fertiliser_date):
    query = 'INSERT INTO MAINTENANCE_FERTILISERS (maintenanceSerialNo, fertiliserDate) VALUES (%s, %s)'
    params = (serial_num, fertiliser_date)
    execute_query(query, params)

def update_fertilizer(serial_num, new_date):
    # Check if maintenance fertilizer record exists before updating
    check_query = 'SELECT COUNT(*) AS count FROM MAINTENANCE_FERTILISERS WHERE maintenanceSerialNo = %s'
    check_params = (serial_num,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        # If maintenance fertilizer record exists, proceed with the update
        update_query = 'UPDATE MAINTENANCE_FERTILISERS SET fertiliserDate = %s WHERE maintenanceSerialNo = %s'
        update_params = (new_date, serial_num)
        execute_query(update_query, update_params)
        st.success(f'Fertilizer with Serial Number {serial_num} updated successfully!')
    else:
        st.error(f'Error: Fertilizer record with Serial Number {serial_num} does not exist.')

def delete_fertilizer(serial_num):
    # Check if maintenance fertilizer record exists before deleting
    check_query = 'SELECT COUNT(*) AS count FROM MAINTENANCE_FERTILISERS WHERE maintenanceSerialNo = %s'
    check_params = (serial_num,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        # If maintenance fertilizer record exists, proceed with deletion
        delete_query = 'DELETE FROM MAINTENANCE_FERTILISERS WHERE maintenanceSerialNo = %s'
        delete_params = (serial_num,)
        execute_query(delete_query, delete_params)
        st.success(f'Fertilizer with Serial Number {serial_num} deleted successfully!')
    else:
        st.error(f'Error: Fertilizer record with Serial Number {serial_num} does not exist.')

def display_all_fertilizers():
    query = 'SELECT * FROM MAINTENANCE_FERTILISERS'
    fertilizers = execute_query(query)
    display_query_results(fertilizers)

# CRUD Operations for CROP table
def add_crop(crop_id, crop_name, crop_type, maintenance_id):
    # Check if maintenance_id is already associated with another crop
    check_query = 'SELECT COUNT(*) AS count FROM CROP WHERE maintenanceId = %s'
    check_params = (maintenance_id,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] == 0:
        # If maintenance_id is unique, proceed with the crop insertion
        query = 'INSERT INTO CROP (cropId, cropName, cropType, maintenanceId) VALUES (%s, %s, %s, %s)'
        params = (crop_id, crop_name, crop_type, maintenance_id)
        execute_query(query, params)  # Execute the query

        st.success('Crop inserted successfully!')
    else:
        st.error('Error: Maintenance ID is already associated with another crop. Please use a different Maintenance ID.')

# CRUD Operations for CROP table
def update_crop(crop_id, crop_name, crop_type, maintenance_id):
    # Check if the new maintenance_id is already associated with another crop
    check_query = 'SELECT COUNT(*) AS count FROM CROP WHERE maintenanceId = %s AND cropId != %s'
    check_params = (maintenance_id, crop_id)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] == 0:
        # If maintenance_id is unique, proceed with the crop update
        query = 'UPDATE CROP SET cropName = %s, cropType = %s, maintenanceId = %s WHERE cropId = %s'
        params = (crop_name, crop_type, maintenance_id, crop_id)
        execute_query(query, params)  # Execute the query

        st.success(f'Crop with ID {crop_id} updated successfully!')
    else:
        st.error('Error: Maintenance ID is already associated with another crop. Please use a different Maintenance ID.')

def delete_crop(crop_id):
    # Check if crop record with the specified crop_id exists before deleting
    check_query = 'SELECT COUNT(*) AS count FROM CROP WHERE cropId = %s'
    check_params = (crop_id,)
    result = execute_query(check_query, check_params)

    if result and result[0]['count'] > 0:
        # If crop exists, proceed with deletion
        delete_query = 'DELETE FROM CROP WHERE cropId = %s'
        delete_params = (crop_id,)
        execute_query(delete_query, delete_params)
        st.success(f'Crop with ID {crop_id} deleted successfully!')
    else:
        st.error(f'Error: Crop with ID {crop_id} does not exist. Cannot delete non-existent crop.')

def display_all_crops():
    query = 'SELECT * FROM CROP'
    crops = execute_query(query)
    display_query_results(crops)


def display_query_results(results):
    if results:
        df = pd.DataFrame(results)
        st.dataframe(df)
    else:
        st.info('No results found.')


# Streamlit app
def main():
    st.title('Agriculture Management System')

    # CRUD Operations for MAINTENANCE table
    st.header('MAINTENANCE Operations')
    st.subheader('Add Maintenance')
    maintenance_serial = st.number_input('Maintenance Serial Number:', step=1, value=1)
    planting_date = st.date_input('Planting Date:')
    harvest_date = st.date_input('Harvest Date:')
    if st.button('Add Maintenance'):
        add_maintenance(maintenance_serial, planting_date, harvest_date)
        st.success('Maintenance added successfully!')

    st.subheader('Update Maintenance')
    update_maintenance_serial = st.number_input('Maintenance Serial Number to Update:', step=1)
    updated_planting_date = st.date_input('Updated Planting Date:')
    updated_harvest_date = st.date_input('Updated Harvest Date:')
    if st.button('Update Maintenance'):
        update_maintenance(update_maintenance_serial, updated_planting_date, updated_harvest_date)

    st.subheader('Delete Maintenance')
    delete_maintenance_serial = st.number_input('Maintenance Serial Number to Delete:', step=1)
    if st.button('Delete Maintenance'):
        delete_maintenance(delete_maintenance_serial)

    st.subheader('Display All Maintenance')
    if st.button('Show All Maintenance'):
        display_all_maintenance()

    # CRUD Operations for MAINTENANCE_FERTILISERS table
    st.header('MAINTENANCE_FERTILISERS Operations')
    st.subheader('Add Fertilizer')
    add_fertilizer_serial = st.number_input('Maintenance Serial Number for Fertilizer:', step=1, value=1)
    fertiliser_date = st.date_input('Fertilizer Date:')
    if st.button('Add Fertilizer'):
        add_fertilizer(add_fertilizer_serial, fertiliser_date)
        st.success('Fertilizer added successfully!')

    st.subheader('Update Fertilizer')
    update_fertilizer_serial = st.number_input('Maintenance Serial Number for Fertilizer to Update:', step=1)
    updated_fertiliser_date = st.date_input('Updated Fertilizer Date:')
    if st.button('Update Fertilizer'):
        update_fertilizer(update_fertilizer_serial, updated_fertiliser_date)
        #st.success(f'Fertilizer with Serial Number {update_fertilizer_serial} updated successfully!')

    st.subheader('Delete Fertilizer')
    delete_fertilizer_serial = st.number_input('Maintenance Serial Number for Fertilizer to Delete:', step=1)
    if st.button('Delete Fertilizer'):
        delete_fertilizer(delete_fertilizer_serial)
        #st.success(f'Fertilizer with Serial Number {delete_fertilizer_serial} deleted successfully!')

    st.subheader('Display All Fertilizers')
    if st.button('Show All Fertilizers'):
        display_all_fertilizers()

    # CRUD Operations for CROP table
    st.header('CROP Operations')

    # Add Crop
    st.subheader('Add Crop')
    crop_id = st.number_input('Crop ID:', step=1, value=1)
    crop_name = st.text_input('Crop Name:')
    crop_type = st.text_input('Crop Type:')
    maintenance_id = st.number_input('Maintenance ID:', step=1, value=1)
    if st.button('Add Crop'):
        add_crop(crop_id, crop_name, crop_type, maintenance_id)


    # Update Crop
    st.subheader('Update Crop')
    update_crop_id = st.number_input('Crop ID to Update:', step=1)
    updated_crop_name = st.text_input('Updated Crop Name:')
    updated_crop_type = st.text_input('Updated Crop Type:')
    updated_maintenance_id = st.number_input('Updated Maintenance ID:', step=1, value=1)
    if st.button('Update Crop'):
        update_crop(update_crop_id, updated_crop_name, updated_crop_type, updated_maintenance_id)

    # Delete Crop
    st.subheader('Delete Crop')
    delete_crop_id = st.number_input('Crop ID to Delete:', step=1)
    if st.button('Delete Crop'):
        delete_crop(delete_crop_id)

    # Display All Crops
    st.subheader('Display All Crops')
    if st.button('Show All Crops'):
        display_all_crops()

    

if __name__ == '__main__':
    main()
