

class Visitee:

    def __init__(self, visiteeLastName, visiteeFirstName, phoneNumber, location, address):

        self.visiteeLastName = visiteeLastName
        self.visiteeFirstName = visiteeFirstName
        self.phoneNumber = phoneNumber
        self.location = location    # the place, for example "Christopher House"
        self.address = address

    def json(self):
        # Don't send the password in the result, just the username
        return {'visitee last name': self.visiteeLastName,
                'visitee first name': self.visiteeFirstName,
                'phone number': self.phoneNumber,
                'location': self.location
                }

    def add_visitee(self):
        # write json to file
        pass

    def remove_visitee(self):
        # remove visitor from json file
        pass

    def list_visitees_by_location(self):
        # if many visitees are in the same place (hospital, nursing home, etc.), list them
        pass

