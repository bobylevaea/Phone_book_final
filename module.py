import os
import json


class Contact:
    def __init__(self, name: str, phone: str, comment: str, id: str = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_tuple(self) -> tuple[str]:
        return self.name, self.phone, self.comment

    def to_json(self):
        data = {'name': self.name, 'phone': self.phone, 'comment': self.comment}
        if self.id is not None:
            data['id'] = self.id
        return data

    def __str__(self):
        return f'{self.name} {self.phone} {self.comment}'


class PhoneBook:
    def __init__(self, path: str = 'phones.txt'):
        self.path = path
        self.contacts: dict[int, Contact] = {}
        self.open()

    def open(self):
        self.contacts.clear()
        if not os.path.exists(self.path):
            self.save()
            return True
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            if data:
                for key, values in data.items():
                    self.contacts[int(key)] = Contact(*values.values())
                return True
            else:
                return False

    def save(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump({str(uid): values.to_json() for uid, values in self.contacts.items()}, file, indent=4, ensure_ascii=False)

    def add(self, new: Contact):
        new_id = self.check_id()['id']
        new.id = new_id
        self.contacts[new_id] = new
        self.update_contact_indexes()
        self.save()

    def get_contacts(self):
        contacts_list = [((uid,) + contact.to_tuple()) for uid, contact in self.contacts.items()]
        return contacts_list

    def search_contact(self, contact):
        found_contacts = []
        for uid, c in self.contacts.items():
            if contact.lower() in c.name.lower() or contact.lower() in c.phone.lower():
                found_contacts.append((uid,) + c.to_tuple())
        return found_contacts

    def edit_contact(self, contact_id, new_contact):
        contact = self.contacts.get(contact_id)
        if contact is not None:
            updated_contact = Contact(*new_contact, id=contact.id)
            self.contacts[contact_id] = updated_contact
            self.save()
            return True
        return False

    def delete_contact_by_number(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self.update_contact_indexes()
            self.save()
            return True
        return False

    def check_id(self):
        uid_list = []
        for contact in self.contacts.values():
            if contact.id is not None:
                uid_list.append(int(contact.to_json()['id']))
        if not uid_list:
            return {'id': 1}
        return {'id': max(uid_list) + 1}

    def _is_valid_index(self, index):
        return 0 <= index < len(self.contacts)

    def update_contact_indexes(self):
        contact_ids = list(self.contacts.keys())
        contact_ids.sort()
        updated_contacts = {}
        for i, contact_id in enumerate(contact_ids, start=1):
            contact = self.contacts[contact_id]
            contact.id = i
            updated_contacts[i] = contact
        self.contacts = updated_contacts