import mysql.connector

# Initializes the database connection
def createConnection(host, user, password, database):
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Closes the database connection
def shutDownConnection(connection):
    if connection:
        connection.close()

# Inserts data into the database using prepared statements and exception handling
def insertInDataBase(connection, sql, data):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, data)
        connection.commit()
        last_row_id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error inserting into the database: {err}")
        connection.rollback()  # Reverts the transaction in case of an error
        return None
    finally:
        cursor.close()
    return last_row_id

# Lists data from the database with exception handling
def listDataBase(connection, sql, params=None):
    try:
        cursor = connection.cursor(prepared=True)
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error listing from the database: {err}")
        return []
    finally:
        cursor.close()
    return results

# Updates data in the database with exception handling
def updateOnDataBase(connection, sql, data):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, data)
        connection.commit()
        affected_rows = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error updating the database: {err}")
        connection.rollback()  # Reverts the transaction in case of an error
        return 0
    finally:
        cursor.close()
    return affected_rows

# Deletes data from the database with exception handling
def deleteOnDataBase(connection, sql, data):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, data)
        connection.commit()
        affected_rows = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error deleting from the database: {err}")
        connection.rollback()  # Reverts the transaction in case of an error
        return 0
    finally:
        cursor.close()
    return affected_rows