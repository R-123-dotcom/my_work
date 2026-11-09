import datetime
import os
import pickle

FILENAME = "time_capsule.dat"


def save_capsule():
  print("\n--- Create New Time Capsule ---")
  author = input("Enter your name: ")
  message = input("Enter your message/memory: ")
  
  while True:
    try:
      date_str = input("Enter unlock date (YYYY-MM-DD): ")
      time_str = input("Enter unlock time (HH:MM in 24-hour format): ")+":00"
      unlock_dt_str = f"{date_str} {time_str}"
      unlock_time = datetime.datetime.strptime(
          unlock_dt_str, "%Y-%m-%d %H:%M:%S"
      )
      break
    except ValueError:
      print(
          "Invalid date or time format. Please use YYYY-MM-DD and HH:MM."
      )

  creation_time = datetime.datetime.now()

  capsule_data = {
      "author": author,
      "message": message,
      "creation_time": creation_time,
      "unlock_time": unlock_time,
  }

  with open(FILENAME, "wb") as file:
    pickle.dump(capsule_data, file)

  print(
      f"\nTime capsule sealed successfully! It can be opened after"
      f" {unlock_time.strftime('%Y-%m-%d %H:%M:%S')}."
  )


def open_capsule():
  print("\n--- Open Time Capsule ---")
  if not os.path.exists(FILENAME):
    print("No time capsule found! Please create one first.")
    return

  with open(FILENAME, "rb") as file:
    capsule_data = pickle.load(file)

  current_time = datetime.datetime.now()
  unlock_time = capsule_data["unlock_time"]

  if current_time < unlock_time:
    time_remaining = unlock_time - current_time
    print("\n[LOCKED] This time capsule is still sealed!")
    print(
        f"Target Unlock Time: {unlock_time.strftime('%Y-%m-%d %H:%M:%S')}"
    )
    print(
        f"Time remaining: {time_remaining.days} days,"
        f" {time_remaining.seconds // 3600} hours,"
        f" {(time_remaining.seconds // 60) % 60} minutes."
    )
  else:
    print("\n[UNLOCKED] Time capsule opened!")
    print(f"Author: {capsule_data['author']}")
    print(
        "Sealed On:"
        f" {capsule_data['creation_time'].strftime('%Y-%m-%d %H:%M:%S')}"
    )
    print(f"Message: {capsule_data['message']}")


def main():
  while True:
    print("\n=== TIME CAPSULE MENU ===")
    print("1. Create and Seal Time Capsule")
    print("2. Check / Open Time Capsule")
    print("3. Exit")
    choice = input("Select an option (1-3): ")

    if choice == "1":
      save_capsule()
    elif choice == "2":
      open_capsule()
    elif choice == "3":
      print("Exiting Time Capsule Application. Goodbye!")
      break
    else:
      print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
  main()
