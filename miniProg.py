#I AM GOING TO RESUBMIT THIS PROJECT LATER, BECAUSE I AM STUCK ON THE REGEX PART. I AM GOING TO BE STUDYING THAT SECTION AGAIN
#MEAN WHILE ILL CONTINUE WITH OOP AND SQL
#AND YES, I AM GOING TO RESUBMIT THE PROJECT BEFORE THE MONTH ENDS, SO PLEASE BE UNDERSTANDING. THANKS.

import re

def write_contacts(filename, manage_contacts): #activates write_contacts above if __name__
  with open(filename, 'w') as file:
    for unique_id, info in manage_contacts.items():
      file.write(f"{unique_id}, {info['phone number']}, {info['email']}, {info['address']}, {info['extra_notes']}\n")

def read_file(filename): #this has to be the same as the variable inside the variable below main ()
  try:
    with open(filename, 'r') as file:
      manage_contacts = {} #this is the variable thats under def main()
      for line in file:
        unique_id, phone_number, email, address, extra_notes = line.strip().split(',')
        manage_contacts[unique_id] = {'phone number': int(phone_number), 'email': email, 'address': address, 'extra_notes': extra_notes}
      return manage_contacts
  except FileNotFoundError:
    return {}    


def add_new_contact(manage_contacts):
  unique_id = input("Enter Unique ID: ")
  if unique_id in manage_contacts:
    print("Unique ID already exists!")
  else:
    phone_number = int(input("Type a phone number: "))
    email = input("Type email: ")
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    address = input("Type address: ")
    extra_notes = input("Type any notes if needed. If not, then type N/A: ")
    manage_contacts[unique_id] = {'phone number': phone_number, 'email': email, 'address': address, 'extra_notes': extra_notes}
    print("Entry added." if valid else "Email incorrect. Please select 2 to edit email. Correct format (ex. abc@gmail.com).")

def edit_contact(manage_contacts):
  unique_id = input("Type Unique ID: ")
  if unique_id not in manage_contacts:
    print("Unique ID not found")
  else:
    phone_number = int(input("Update the phone number: "))
    manage_contacts[unique_id]['phone number'] = phone_number
    
    email = input("Update email: ")
    manage_contacts[unique_id]['email'] = email
    
    address = input("Update the address: ")
    manage_contacts[unique_id]['address'] = address
    
    extra_notes = input("Update the notes: ")
    manage_contacts[unique_id]['extra_notes'] = extra_notes

def delete_contact(manage_contacts):
  try:
    delete_contact_info = input("Please type the Unique ID in order to delete: ")
    if delete_contact_info in manage_contacts:
      manage_contacts.pop(delete_contact_info)
      print("Contact info has been deleted")
    else:
      print(f"Contact info for {delete_contact_info} was not found!")
  except Exception:
    []

def search_contact(manage_contacts):
  unique_id = input("Type the Unique ID to search: ")
  if unique_id in manage_contacts:
    info = manage_contacts[unique_id]
    print(f"Unique ID: {unique_id}, Phone number: {info['phone number']}, Email: {info['email']}, Address: {info['address']}, Extra Notes: {info['extra_notes']}")
  else:
    print("Info not found!")

def display_contacts(manage_contacts):
  for unique_id, info in manage_contacts.items():
    print(f"Unique ID: {unique_id}, Phone number: {info['phone number']}, Email: {info['email']}, Address: {info['address']}, Extra Notes: {info['extra_notes']}")

def export_contacts():
  pass

def import_contacts():
  pass

def main():
  manage_contacts = read_file('contact_database.txt') #this is for the read function

  while True:
    print("\n1. Add a new contact \n2. Edit an existing contact \n3. Delete a contact \n4. Search for a contact \n5. Display all contacts \n6. Export contacts to a text file \n7. Import contacts \n8. Quit")
    choice = input("Pick a selection: ")

    if choice == '1':
      add_new_contact(manage_contacts)
      
    elif choice == '2':
      edit_contact(manage_contacts)

    elif choice == '3':
      delete_contact(manage_contacts)

    elif choice == '4':
      search_contact(manage_contacts)
      
    elif choice == '5':
      display_contacts(manage_contacts)
      
    elif choice == '6':
      import_contacts(manage_contacts)
      
    elif choice == '7':
      export_contacts(manage_contacts)
      
    elif choice == '8':
      break
    else:
      print("Invalid")
    
    write_contacts('contact_database.txt', manage_contacts) #activates variables under while True:

if __name__ == "__main__":
  main()