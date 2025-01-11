import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    # Incidents Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            severity INTEGER
        )
    """)
    # Stolen Vehicles Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stolen_vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT UNIQUE,
            make TEXT,
            model TEXT,
            color TEXT
        )
    """)
    conn.commit()
    conn.close()

# Incident Management
def add_incident():
    description = input("Enter incident description: ")
    print("Rate the severity of the incident (1-5):")
    print("☆☆☆☆☆")
    while True:
        try:
            rating = int(input("Choose a number between 1 and 5: "))
            if 1 <= rating <= 5:
                print("You selected:", "★" * rating + "☆" * (5 - rating))
                break
            else:
                print("Please enter a valid number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("INSERT INTO incidents (description, severity) VALUES (?, ?)", (description, rating))
    conn.commit()
    conn.close()
    print("Incident added successfully!")

def search_incidents():
    keyword = input("Enter a keyword to search incidents: ").lower()
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents WHERE LOWER(description) LIKE ?", (f"%{keyword}%",))
    results = cursor.fetchall()
    conn.close()

    if results:
        print("Search Results:")
        for incident in results:
            print(f"ID: {incident[0]}, Description: {incident[1]}, Severity: {'★' * incident[2] + '☆' * (5 - incident[2])}")
    else:
        print("No incidents found matching your keyword.")

def view_incidents():
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    incidents = cursor.fetchall()
    conn.close()

    if not incidents:
        print("No incidents found.")
        return

    print("\nIncidents:")
    for incident in incidents:
        print(f"ID: {incident[0]}, Description: {incident[1]}, Severity: {'★' * incident[2] + '☆' * (5 - incident[2])}")
    print()

def delete_incident():
    view_incidents()
    incident_id = input("Enter the ID of the incident to delete: ")
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incidents WHERE id = ?", (incident_id,))
    conn.commit()
    conn.close()
    print("Incident deleted successfully!")

# Stolen Vehicle Management
def add_stolen_vehicle():
    license_plate = input("Enter license plate: ").upper()
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")

    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO stolen_vehicles (license_plate, make, model, color)
            VALUES (?, ?, ?, ?)
        """, (license_plate, make, model, color))
        conn.commit()
        print("Stolen vehicle added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Vehicle with this license plate already exists.")
    conn.close()

def search_stolen_vehicle():
    search_term = input("Enter license plate or make/model to search: ").lower()
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM stolen_vehicles 
        WHERE LOWER(license_plate) LIKE ? OR LOWER(make) LIKE ? OR LOWER(model) LIKE ?
    """, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
    results = cursor.fetchall()
    conn.close()

    if results:
        print("Search Results:")
        for vehicle in results:
            print(f"ID: {vehicle[0]}, License Plate: {vehicle[1]}, Make: {vehicle[2]}, Model: {vehicle[3]}, Color: {vehicle[4]}")
    else:
        print("No vehicles found matching your search.")

def view_stolen_vehicles():
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stolen_vehicles")
    vehicles = cursor.fetchall()
    conn.close()

    if not vehicles:
        print("No stolen vehicles found.")
        return

    print("\nStolen Vehicles:")
    for vehicle in vehicles:
        print(f"ID: {vehicle[0]}, License Plate: {vehicle[1]}, Make: {vehicle[2]}, Model: {vehicle[3]}, Color: {vehicle[4]}")
    print()

def remove_stolen_vehicle():
    view_stolen_vehicles()
    vehicle_id = input("Enter the ID of the stolen vehicle to remove: ")
    conn = sqlite3.connect("db.sl3")  # Changed to db.sl3
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stolen_vehicles WHERE id = ?", (vehicle_id,))
    conn.commit()
    conn.close()
    print("Stolen vehicle removed successfully!")

# Main program loop
def main():
    setup_database()
    while True:
        print("\nWelcome to the Incident and Vehicle Management System!")
        print("Please choose an option:")
        print("1. Add a new incident")
        print("2. Search incidents")
        print("3. View all incidents")
        print("4. Delete an incident")
        print("5. Add a stolen vehicle")
        print("6. Search for a stolen vehicle")
        print("7. View all stolen vehicles")
        print("8. Remove a stolen vehicle")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_incident()
        elif choice == "2":
            search_incidents()
        elif choice == "3":
            view_incidents()
        elif choice == "4":
            delete_incident()
        elif choice == "5":
            add_stolen_vehicle()
        elif choice == "6":
            search_stolen_vehicle()
        elif choice == "7":
            view_stolen_vehicles()
        elif choice == "8":
            remove_stolen_vehicle()
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
