from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.ArtWorks import Artwork


class MainModule:
    @staticmethod
    def display_menu():
        print("-------------------------------------")
        print("Virtual Art Gallery Menu")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Get Artwork by ID")
        print("5. Search Artworks keyword")
        print("6. Add Artwork to Favorites")
        print("7. Remove Artwork from Favorites")
        print("8. Get User Favorite Artworks")
        print("9. Give Feedback")
        print("10. Show Feedbacks for a Artwork")
        print("0. Exit")
        print("-------------------------------------")

    @staticmethod
    def add_artwork(virtual_gallery):
        title = input("Enter title : ")
        description = input("Enter description: ")
        creation_date = input("Enter creation_date(in yyyy-mm-dd format): ")
        medium = input("Enter medium: ")
        image_url = input("Enter image_url: ")
        artist_id = input("Enter artist_id: ")
        artwork = Artwork(None, title, description, creation_date, medium, image_url, artist_id)
        virtual_gallery.addArtwork(artwork)

    @staticmethod
    def update_artwork(virtual_gallery):
        artwork_id = input("Enter the ID of the artwork you want to update: ")
        artwork = virtual_gallery.getArtworkById(artwork_id)
        if artwork is None:
            print("Artwork with ID", artwork_id, "not found.")
            return

        title = input("Enter the new title for the artwork (press Enter to keep current title): ")
        description = input("Enter the new description for the artwork (press Enter to keep current description): ")
        creation_date = input("Enter the new creation date for the artwork (press Enter to keep current date): ")
        medium = input("Enter the new medium for the artwork (press Enter to keep current medium): ")
        image_url = input("Enter the new image URL for the artwork (press Enter to keep current URL): ")

        if title:
            artwork.set_title(title)
        if description:
            artwork.set_description(description)
        if creation_date:
            artwork.set_creation_date(creation_date)
        if medium:
            artwork.set_medium(medium)
        if image_url:
            artwork.set_image_url(image_url)

        virtual_gallery.updateArtwork(artwork)
        #print("Artwork updated successfully!")

    @staticmethod
    def remove_artwork(virtual_gallery):
        artwork_id = input("Enter the ID of the artwork you want to remove: ")

        removed = virtual_gallery.removeArtwork(artwork_id)
        if removed:
            print("---------------Artwork removed successfully!---------------")
        else:
            print("Failed to remove artwork. Please check the artwork ID.")

    @staticmethod
    def get_artwork_by_id(virtual_gallery):
        artwork_id = input("Enter the ID of the artwork you want to retrieve: ")
        artwork = virtual_gallery.getArtworkById(artwork_id)
        if artwork:
            print("Artwork details:")
            print("ID:", artwork.get_artwork_id())
            print("Title:", artwork.get_title())
            print("Description:", artwork.get_description())
            print("Creation Date:", artwork.get_creation_date())
            print("Medium:", artwork.get_medium())
            print("Image URL:", artwork.get_image_url())
            print("Artist ID:", artwork.get_artist_id())

        else:
            print("Artwork with ID", artwork_id, "not found.")

    @staticmethod
    def search_artworks(virtual_gallery):
        keyword = input("Enter the keyword to search artworks: ")

        artworks = virtual_gallery.searchArtworks(keyword)
        if artworks:
            print("Matching artworks:")

            for artwork in artworks:
                print("---------------------------------------")
                print("ID:              ", artwork.get_artwork_id())
                print("Title:           ", artwork.get_title())
                print("Description:     ", artwork.get_description())
                print("Creation Date:   ", artwork.get_creation_date())
                print("Medium:          ", artwork.get_medium())
                print("Image URL:       ", artwork.get_image_url())
                print("---------------------------------------")
        else:
            print("No artworks found matching the keyword:", keyword)

    @staticmethod
    def add_artwork_to_favorites(virtual_gallery):

        user_id = input("Enter your user ID: ")
        virtual_gallery.showAllArtworks()
        artwork_id = input("Enter the ID of the artwork you want to add to favorites: ")

        virtual_gallery.addArtworkToFavorite(user_id, artwork_id)

    @staticmethod
    def remove_artwork_from_favorites(virtual_gallery):
        user_id = input("Enter your user ID: ")
        artwork_id = input("Enter the ID of the artwork you want to remove from favorites: ")
        virtual_gallery.removeArtworkFromFavorite(user_id, artwork_id)

    @staticmethod
    def get_user_favorite_artworks(virtual_gallery):
        user_id = input("Enter your user ID: ")
        virtual_gallery.getUserFavoriteArtworks(user_id)

    @staticmethod
    def give_feedback(virtual_gallery):
        user_id = input("Enter your user ID: ")
        virtual_gallery.showAllArtworks()
        artwork_id = input("Enter the ID of the artwork for which you want to give feedback: ")
        feedback_text = input("Enter your feedback: ")
        virtual_gallery.feedback(user_id, artwork_id, feedback_text)

    @staticmethod
    def show_feedbacks(virtual_gallery):
        artwork_id = input("Enter the ID of the artwork: ")
        feedbacks = virtual_gallery.getFeedbacksByArtworkId(artwork_id)
        if feedbacks:
            print(f"Feedbacks for Artwork ID {artwork_id}:")
            for feedback in feedbacks:
                #print(feedback)
                print("--------------------------------------------------------------")
                print(f"User ID: {feedback['UserID']}")
                print(f"Feedback: {feedback['Feedback']}")
                print("--------------------------------------------------------------")

        else:
            print(f"No feedbacks found for Artwork ID {artwork_id}")

    @staticmethod
    def main():
        virtual_gallery = VirtualArtGalleryImpl()
        while True:
            MainModule.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                MainModule.add_artwork(virtual_gallery)
            elif choice == "2":
                MainModule.update_artwork(virtual_gallery)
            elif choice == "3":
                MainModule.remove_artwork(virtual_gallery)
            elif choice == "4":
                MainModule.get_artwork_by_id(virtual_gallery)
            elif choice == "5":
                MainModule.search_artworks(virtual_gallery)
            elif choice == "6":
                MainModule.add_artwork_to_favorites(virtual_gallery)
            elif choice == "7":
                MainModule.remove_artwork_from_favorites(virtual_gallery)
            elif choice == "8":
                MainModule.get_user_favorite_artworks(virtual_gallery)
            elif choice == "9":
                MainModule.give_feedback(virtual_gallery)
            elif choice == "10":
                MainModule.show_feedbacks(virtual_gallery)
            elif choice == "0":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    MainModule.main()
