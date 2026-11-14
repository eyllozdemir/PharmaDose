
# ==========================================
# PHARMADOSE - Medication Schedule Planner
# Educational project - Not medical advice
# ==========================================

# List to store medications
medications = []


# FUNCTION 1: Get valid text input
def get_text(message):
    while True:
        answer = input(message).strip()

        if answer != "":
            return answer
        else:
            print("This field cannot be empty. Please try again.")


# FUNCTION 2: Get valid number input
def get_positive_number(message, maximum):
    while True:
        try:
            number = int(input(message))

            if 1 <= number <= maximum:
                return number
            else:
                print(f"Please enter a number between 1 and {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# FUNCTION 3: Add medication
def add_medication():
    print("\n--- ADD A NEW MEDICATION ---")

    name = get_text("Enter medication name: ")

    dose = get_text("Enter dose (e.g. 1 tablet): ")

    frequency = get_positive_number(
        "How many times per day? (1-24): ", 24
    )

    duration = get_positive_number(
        "How many days? (1-365): ", 365
    )

    # Store medication information in a dictionary
    medication = {
        "name": name,
        "dose": dose,
        "frequency": frequency,
        "duration": duration
    }

    # Add medication to the list
    medications.append(medication)

    print("\nMedication added successfully!")


# FUNCTION 4: Show all medications
def show_medications():
    print("\n--- YOUR MEDICATION LIST ---")

    if len(medications) == 0:
        print("No medications have been added yet.")

    else:
        for index, medicine in enumerate(medications, start=1):
            print(f"\nMedication {index}")
            print(f"Name: {medicine['name']}")
            print(f"Dose: {medicine['dose']}")
            print(f"Frequency: {medicine['frequency']} times per day")
            print(f"Duration: {medicine['duration']} days")


def show_schedule():
    if len(medications) == 0:
        print("\nNo medications have been added yet.")
        return

    print("\n--- EXAMPLE DAILY SCHEDULE ---")

    for medicine in medications:
        frequency = medicine["frequency"]
        interval = 24 / frequency

        print(f"\nMedication: {medicine['name']}")
        print(f"Dose: {medicine['dose']}")

        for i in range(frequency):
            total_minutes = round(i * interval * 60)
            hour = (8 + total_minutes // 60) % 24
            minute = total_minutes % 60

            print(f"Time {i + 1}: {hour:02d}:{minute:02d}")

    print("\nEducational example only. Follow prescribed instructions.")


# Save medication information to a text file
def save_medications():
    if len(medications) == 0:
        print("\nNo medications to save.")
        return

    with open("medication_schedule.txt", "w", encoding="utf-8") as file:
        file.write("PHARMADOSE - MEDICATION SCHEDULE\n")
        file.write("Educational example only\n")
        file.write("=" * 40 + "\n")

        for medicine in medications:
            file.write(f"\nMedication: {medicine['name']}\n")
            file.write(f"Dose: {medicine['dose']}\n")
            file.write(f"Frequency: {medicine['frequency']} times per day\n")
            file.write(f"Duration: {medicine['duration']} days\n")

            interval = 24 / medicine["frequency"]

            for i in range(medicine["frequency"]):
                total_minutes = round(i * interval * 60)
                hour = (8 + total_minutes // 60) % 24
                minute = total_minutes % 60

                file.write(f"Time {i + 1}: {hour:02d}:{minute:02d}\n")

    print("\nSchedule saved to medication_schedule.txt!")

  

# FUNCTION 5: Welcome message
def welcome_message():
    print("=" * 45)
    print("       WELCOME TO PHARMADOSE")
    print("   Medication Schedule Planner")
    print("=" * 45)
    print("Educational use only - Not medical advice.")


# FUNCTION 6: Main menu

    
def main():
    welcome_message()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add medication")
        print("2. Show medications")
        print("3. Show example schedule")
        print("4. Save schedule to TXT")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_medication()

        elif choice == "2":
            show_medications()

        elif choice == "3":
            show_schedule()

        elif choice == "4":
            save_medications()

        elif choice == "5":
            print("\nThank you for using PharmaDose!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()

