members = []
events = []

def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")

    member = {
        "id": member_id,
        "name": name,
        "branch": branch,
        "year": year
    }

    members.append(member)
    print("Member added successfully!")


def view_members():
    if len(members) == 0:
        print("No members registered.")
    else:
        print("\n--- Club Members ---")
        for member in members:
            print("ID:", member["id"])
            print("Name:", member["name"])
            print("Branch:", member["branch"])
            print("Year:", member["year"])
            print("-------------------")


def search_member():
    search_id = input("Enter Member ID to search: ")

    for member in members:
        if member["id"] == search_id:
            print("\nMember Found!")
            print("Name:", member["name"])
            print("Branch:", member["branch"])
            print("Year:", member["year"])
            return

    print("Member not found.")


def delete_member():
    delete_id = input("Enter Member ID to delete: ")

    for member in members:
        if member["id"] == delete_id:
            members.remove(member)
            print("Member deleted successfully!")
            return

    print("Member not found.")


def add_event():
    event_name = input("Enter Event Name: ")
    date = input("Enter Event Date: ")
    venue = input("Enter Venue: ")

    event = {
        "name": event_name,
        "date": date,
        "venue": venue
    }

    events.append(event)
    print("Event added successfully!")


def view_events():
    if len(events) == 0:
        print("No events available.")
    else:
        print("\n--- Club Events ---")
        for event in events:
            print("Event:", event["name"])
            print("Date:", event["date"])
            print("Venue:", event["venue"])
            print("-------------------")


while True:

    print("\n===== CLUB MANAGEMENT SYSTEM =====")
    print("1. Add Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. Delete Member")
    print("5. Add Event")
    print("6. View Events")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_member()

    elif choice == "2":
        view_members()

    elif choice == "3":
        search_member()

    elif choice == "4":
        delete_member()

    elif choice == "5":
        add_event()

    elif choice == "6":
        view_events()

    elif choice == "7":
        print("Thank you for using Club Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
