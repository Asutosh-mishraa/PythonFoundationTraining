from dao.AdditionalFunctionImpl import AdditionalFunctionImpl
from entity.Artists import Artist
from entity.ArtWorks import Artwork
from entity.Gallery import Gallery


class MainDriver:
    @staticmethod
    def display_menu():
        print("---- Virtual Art Gallery Menu ----")
        print("1. Add Gallery")
        print("2. Update Gallery")
        print("3. Remove Gallery")
        print("4. Search Galleries")
        print("5. Get Gallery by ID")
        print("6. Add Artwork to Gallery")
        print("7. Remove Artwork from Gallery")
        print("8. Get Artworks of Gallery")
        print("9. Create Artist")
        print("10. Update Artist")
        print("11. Delete Artist")
        print("12. Get Artist by ID")
        print("13. Create User")
        print("14. Update User")
        print("15. Delete User")
        print("16. Get User by ID")
        print("0. Exit")

    @staticmethod
    def main():
        additional_functions = AdditionalFunctionImpl()

        while True:
            MainDriver.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter gallery name: ")
                description = input("Enter gallery description: ")
                location = input("Enter gallery location: ")
                curator = input("Enter gallery Artist ID: ")
                opening_hours = input("Enter gallery opening hours: ")
                gallery = Gallery(None, name, description, location, curator, opening_hours)
                additional_functions.addGallery(gallery)

            elif choice == "2":
                gallery_id = input("Enter the ID of the gallery you want to update: ")

                gallery = additional_functions.getGalleryById(gallery_id)

                if gallery:
                    new_name = input(f"Enter new name for gallery (current: {gallery.name})(press Enter to keep "
                                     f"current title): ")
                    new_description = input(f"Enter new description for gallery (current: {gallery.description})("
                                            f"press Enter to keep current title): ")
                    new_location = input(f"Enter new location for gallery (current: {gallery.location})(press Enter "
                                         f"to keep current title): ")
                    new_curator = input(f"Enter new curator for gallery (current: {gallery.curator})(press Enter to "
                                        f"keep current title): ")
                    new_opening_hours = input(
                        f"Enter new opening hours for gallery (current: {gallery.opening_hours})(press Enter to keep "
                        f"current title): ")

                    if new_name:
                        gallery.set_name(new_name)
                    if new_description:
                        gallery.set_description(new_description)
                    if new_location:
                        gallery.set_location(new_location)
                    if new_curator:
                        gallery.set_curator(new_curator)
                    if new_opening_hours:
                        gallery.set_opening_hours(new_opening_hours)

                    additional_functions.updateGallery(gallery)
                    print("Gallery updated successfully!")
                else:
                    print("Gallery not found.")

            elif choice == "3":
                gallery_id = input("Enter gallery ID to remove: ")
                additional_functions.removeGallery(gallery_id)

            elif choice == "4":

                keyword = input("Enter keyword to search galleries: ")
                additional_functions.searchGalleries(keyword)

            elif choice == "5":
                gallery_id = input("Enter gallery ID: ")
                gallery = additional_functions.getGalleryById(gallery_id)
                print("Gallery name:", gallery.get_name(), "\nGallery opening hours:", gallery.get_opening_hours())

            elif choice == "6":
                gallery_id = input("Enter gallery ID: ")
                artwork_id = input("Enter artwork ID: ")
                additional_functions.addArtworkToGallery(gallery_id, artwork_id)

            elif choice == "7":
                gallery_id = input("Enter gallery ID: ")
                artwork_id = input("Enter artwork ID: ")
                additional_functions.removeArtworkFromGallery(gallery_id, artwork_id)

            elif choice == "8":
                gallery_id = input("Enter gallery ID: ")
                additional_functions.getArtworksOfGallery(gallery_id)

            elif choice == "9":
                name = input("Enter artist name: ")
                biography = input("Enter artist biography: ")
                birth_date = input("Enter artist birth date (YYYY-MM-DD): ")
                nationality = input("Enter artist nationality: ")
                website = input("Enter artist website: ")
                contact_information = input("Enter artist contact information: ")
                artist = Artist(None, name, biography, birth_date, nationality, website, contact_information)

                additional_functions.createArtist(artist)

            elif choice == "10":
                artist_id = input("Enter the ID of the artist you want to update: ")
                artist = additional_functions.getArtistById(artist_id)
                if artist is None:
                    print("Artist with ID", artist_id, "not found.")
                else:
                    new_name = input("Enter the new name for the artist (press Enter to keep current name): ")
                    new_biography = input(
                        "Enter the new biography for the artist (press Enter to keep current biography): ")
                    new_birth_date = input(
                        "Enter the new birth date for the artist (press Enter to keep current birth date): ")
                    new_nationality = input(
                        "Enter the new nationality for the artist (press Enter to keep current nationality): ")
                    new_website = input("Enter the new website for the artist (press Enter to keep current website): ")
                    new_contact_information = input(
                        "Enter the new contact information for the artist (press Enter to keep current contact "
                        "information): ")

                    if new_name:
                        artist.set_name(new_name)
                    if new_biography:
                        artist.set_biography(new_biography)
                    if new_birth_date:
                        artist.set_birth_date(new_birth_date)
                    if new_nationality:
                        artist.set_nationality(new_nationality)
                    if new_website:
                        artist.set_website(new_website)
                    if new_contact_information:
                        artist.set_contact_information(new_contact_information)

                    if additional_functions.updateArtist(artist):
                        print("Artist updated successfully!")
                    else:
                        print("Failed to update artist. Please try again.")

            elif choice == "11":
                artist_id = input("Enter the ID of the artist you want to delete: ")
                if additional_functions.deleteArtist(artist_id):
                    print("Artist deleted successfully!")
                else:
                    print("Failed to delete artist. Please check the artist ID.")

            elif choice == "12":

                artist_id = input("Enter artist ID: ")
                artist = additional_functions.getArtistById(artist_id)
                print("Artist name: ", artist.get_name(), "\nArtist Website:", artist.get_website())

            elif choice == "13":
                pass

            elif choice == "14":
                pass

            elif choice == "15":
                pass

            elif choice == "16":
                pass

            elif choice == "0":
                print("Exiting the program...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    MainDriver.main()
