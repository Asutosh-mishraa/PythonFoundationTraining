from mysql.connector import Error

from dao.IVirtualArtGallery import IVirtualArtGallery
from entity.ArtWorks import Artwork
from myexceptions.ArtWorkNotFoundException import ArtWorkNotFoundException
from myexceptions.UserNotFoundException import UserNotFoundException
from util.DBConnection import DBConnection


class VirtualArtGalleryImpl(IVirtualArtGallery):
    def addArtwork(self, artwork):
        # print("inside addartwork")
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = ("INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID) VALUES (%s, %s, "
                   "%s, %s, %s, %s)")
            values = (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(),
                      artwork.get_image_url(), artwork.get_artist_id())
            cursor.execute(sql, values)

            connection.commit()
            new_artwork_id = cursor.lastrowid
            print("Artwork ID:", new_artwork_id)
            cursor.close()
            print("---------------Artwork added successfully!---------------")
            return True

        except Exception as e:
            # print("Error adding artwork:", e)
            print("Your artist id is invalid.Only artists can add artwork.")
            return False

    def updateArtwork(self, artwork):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = ("UPDATE Artwork SET Title=%s, Description=%s, CreationDate=%s, Medium=%s, ImageURL=%s WHERE "
                   "ArtworkID=%s")
            values = (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(),
                      artwork.get_image_url(), artwork.get_artwork_id())
            cursor.execute(sql, values)

            connection.commit()
            cursor.close()
            print("---------------Artwork updated successfully!---------------")

            return True
        except Exception as e:
            print("Error updating artwork:", e)
            return False

    def removeArtwork(self, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check = "SELECT * FROM Artwork WHERE ArtworkID=%s"
            cursor.execute(sql_check, (artwork_id,))
            artwork = cursor.fetchone()
            if artwork is None:
                raise ArtWorkNotFoundException(artwork_id)

            sql = "DELETE FROM Artwork WHERE ArtworkID=%s"
            cursor.execute(sql, (artwork_id,))

            connection.commit()
            cursor.close()
            # print("Artwork removed successfully!")
            return True
        except ArtWorkNotFoundException as e:
            return False
            # print(e)
        except Exception as e:
            print("Error removing artwork:", e)
            return False

    def getArtworkById(self, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data:

                artwork = Artwork(artwork_data[0], artwork_data[1], artwork_data[2], artwork_data[3], artwork_data[4],
                                  artwork_data[5], artwork_data[6])
                return artwork
            else:
                # print("Artwork with ID", artwork_id, "not found.")
                raise ArtWorkNotFoundException(artwork_id)

        except ArtWorkNotFoundException as e:
            # print(e)
            return None
        except Exception as e:
            print("Error getting artwork by ID:", e)
            return None

    def searchArtworks(self, keyword):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = "SELECT * FROM Artwork WHERE Title LIKE %s OR Description LIKE %s"
            keyword_like = f"%{keyword}%"
            cursor.execute(sql, (keyword_like, keyword_like))
            artworks_data = cursor.fetchall()

            artworks = []

            if not artworks_data:
                print("No artworks found matching the keyword:", keyword)
            else:
                for artwork_data in artworks_data:
                    artwork = Artwork(artwork_data[0], artwork_data[1], artwork_data[2], artwork_data[3],
                                      artwork_data[4],
                                      artwork_data[5], artwork_data[6])
                    artworks.append(artwork)

                cursor.close()

            return artworks
        except Exception as e:
            print("Error searching artworks:", e)
            return []

    def showAllArtworks(self):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM artwork")
            artwork = cursor.fetchall()
            cursor.close()
            print("All artworks Available:")
            for artwork in artwork:
                print(artwork)
            print()

        except Error as e:
            print("Error fetching artwork details:", e)

    def addArtworkToFavorite(self, user_id, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check_user = "SELECT * FROM User WHERE UserID = %s"
            cursor.execute(sql_check_user, (user_id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(user_id)

            sql_check_artwork = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql_check_artwork, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data is None:
                raise ArtWorkNotFoundException(artwork_id)
            sql_check_favorites = "SELECT * FROM User_Favorite_Artwork WHERE UserID = %s AND ArtworkID = %s"
            cursor.execute(sql_check_favorites, (user_id, artwork_id))
            existing_favorite = cursor.fetchone()
            if existing_favorite:
                print("Artwork is already in the user's favorites.")
            else:
                sql_add_favorite = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (%s, %s)"
                cursor.execute(sql_add_favorite, (user_id, artwork_id))
                connection.commit()
                print("Artwork added to favorites successfully!")
                cursor.close()
                return True
            cursor.close()
            return False
        except UserNotFoundException as e:
            print(e)
        except ArtWorkNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error adding artwork to favorites:", e)

    def removeArtworkFromFavorite(self, user_id, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check_user = "SELECT * FROM User WHERE UserID = %s"
            cursor.execute(sql_check_user, (user_id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(user_id)

            sql_check_artwork = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql_check_artwork, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data is None:
                raise ArtWorkNotFoundException(artwork_id)

            sql_check_favorites = "SELECT * FROM User_Favorite_Artwork WHERE UserID = %s AND ArtworkID = %s"
            cursor.execute(sql_check_favorites, (user_id, artwork_id))
            existing_favorite = cursor.fetchone()
            if existing_favorite:
                sql_remove_favorite = "DELETE FROM User_Favorite_Artwork WHERE UserID = %s AND ArtworkID = %s"
                cursor.execute(sql_remove_favorite, (user_id, artwork_id))
                connection.commit()
                cursor.close()
                print("Artwork removed from favorites successfully!")
                return True
            else:
                print("Artwork is not in the user's favorites.")
                cursor.close()

                return False
        except UserNotFoundException as e:
            print(e)
        except ArtWorkNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error removing artwork from favorites:", e)

    def getUserFavoriteArtworks(self, user_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check_user = "SELECT * FROM User WHERE UserID = %s"
            cursor.execute(sql_check_user, (user_id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(user_id)

            sql_get_favorites = ("SELECT A.* FROM Artwork A JOIN User_Favorite_Artwork UFA ON A.ArtworkID = "
                                 "UFA.ArtworkID WHERE UFA.UserID = %s")
            cursor.execute(sql_get_favorites, (user_id,))
            favorite_artworks = cursor.fetchall()

            if not favorite_artworks:
                print("User has no favorite artworks.")
            else:
                print("Favorite artworks for User ID:", user_id)
                for artwork_data in favorite_artworks:
                    print("------------------------------------")
                    print("Artwork ID:      ", artwork_data[0])
                    print("Title:           ", artwork_data[1])
                    print("Description:     ", artwork_data[2])
                    print("Creation Date:   ", artwork_data[3])
                    print("Medium:          ", artwork_data[4])
                    print("Image URL:       ", artwork_data[5])
                    print("------------------------------------")
                cursor.close()
                return True
            cursor.close()
            return False
        except UserNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error getting user's favorite artworks:", e)

    def feedback(self, user_id, artwork_id, feedback_text):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check_user = "SELECT * FROM User WHERE UserID = %s"
            cursor.execute(sql_check_user, (user_id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(user_id)

            sql_check_artwork = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql_check_artwork, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data is None:
                raise ArtWorkNotFoundException(artwork_id)

            if not feedback_text:
                print("Feedback cannot be empty.")
                return False

            query = "SELECT * FROM Feedbacks WHERE UserID = %s AND ArtworkID = %s"
            cursor.execute(query, (user_id, artwork_id))
            existing_feedback = cursor.fetchone()

            if existing_feedback:
                update_query = "UPDATE Feedbacks SET Feedback = %s WHERE UserID = %s AND ArtworkID = %s"
                cursor.execute(update_query, (feedback_text, user_id, artwork_id))
                connection.commit()
                cursor.close()
                print("Feedback updated successfully!")
                return True
            else:
                sql = "INSERT INTO Feedbacks (UserID, ArtworkID, Feedback) VALUES (%s, %s, %s)"
                values = (user_id, artwork_id, feedback_text)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                print("Feedback added successfully!")
                return True

        except Exception as e:
            print("Error adding feedback:", e)
            return False

    def getFeedbacksByArtworkId(self,artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = %s", (artwork_id,))
            artwork = cursor.fetchone()
            if not artwork:
                print(f"Artwork with ID {artwork_id} does not exist.")
                return []
            cursor.execute("SELECT UserID, Feedback FROM Feedbacks WHERE ArtworkID = %s", (artwork_id,))
            feedbacks = cursor.fetchall()

            cursor.close()
            return feedbacks

        except Exception as e:
            print("Error retrieving feedbacks:", e)
            return []
