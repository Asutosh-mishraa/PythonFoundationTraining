class Artist:
    def __init__(self, artist_id=None, name=None, biography=None, birth_date=None, nationality=None, website=None,
                 contact_information=None):
        self.__artist_id = artist_id
        self.__name = name
        self.__biography = biography
        self.__birth_date = birth_date
        self.__nationality = nationality
        self.__website = website
        self.__contact_information = contact_information

    # Getter methods
    def get_artist_id(self):
        return self.__artist_id

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def get_birth_date(self):
        return self.__birth_date

    def get_nationality(self):
        return self.__nationality

    def get_website(self):
        return self.__website

    def get_contact_information(self):
        return self.__contact_information

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_biography(self, biography):
        self.__biography = biography

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def set_website(self, website):
        self.__website = website

    def set_contact_information(self, contact_information):
        self.__contact_information = contact_information
