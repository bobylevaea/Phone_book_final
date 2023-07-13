import view
from module import PhoneBook, Contact
import text


pb = PhoneBook()

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                pb.open()
                view.print_message(text.load_successful)
            case 2:
                pb.save()
                view.print_message(view.text.save_successful)
            case 3:
                contacts = pb.get_contacts()
                view.show_contacts(contacts, view.text.empty_file)
            case 4:
                new_contact = view.input_contact()
                new = Contact(*new_contact)
                pb.add(new)
                view.print_message(text.add_successful(new.name))
            case 5:
                search_input = input(view.text.search_contact)
                search_result = pb.search_contact(search_input)
                if search_result:
                    view.show_contacts(search_result, view.text.empty_file)
                else:
                    view.print_message(view.text.not_found)
            case 6:
                contact_id = int(input(view.text.input_index))
                contacts = pb.get_contacts()
                if contact_id in pb.contacts:
                    old_contact = pb.contacts[contact_id].to_tuple()
                    new_contact = []
                    for i, field in enumerate(view.text.input_change_contact):
                        value = input(field)
                        if value:
                            new_contact.append(value)
                        else:
                            new_contact.append(old_contact[i])
                    pb.edit_contact(contact_id, new_contact)
                    view.print_message(view.text.edit_successful)
                else:
                    view.print_message(view.text.invalid_index)
            case 7:
                number_delete = int(input(view.text.input_index_delete))
                deleted = pb.delete_contact_by_number(number_delete)
                if deleted:
                    view.print_message(view.text.delete_successful)
                else:
                    view.print_message(view.text.delete_error)
            case 8:
                view.print_message(view.text.message_exit)
                return