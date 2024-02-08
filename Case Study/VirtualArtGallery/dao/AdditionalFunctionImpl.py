from dao.IAdditionalFunction import IAdditionalFunction
from entity.ArtWorks import Artwork
from entity.Artists import Artist
from entity.Gallery import Gallery
from util.DBConnection import DBConnection


class AdditionalFunctionImpl(IAdditionalFunction):
    # gallery management
    def addGallery(self, gallery):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = "INSERT INTO Gallery (Name, Description, Location, Curator, OpeningHours) VALUES (%s, %s, %s, %s, %s)"
            values = (gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(),
                      gallery.get_opening_hours())
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            print("Gallery created successfully.")
            return True

        except Exception as e:
            print("Error creating gallery:", e)
            return False

    def updateGallery(self, gallery):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = ("UPDATE Gallery SET Name = %s, Description = %s, Location = %s, Curator = %s, OpeningHours = %s "
                   "WHERE GalleryID = %s")
            values = (gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(),
                      gallery.get_opening_hours(), gallery.get_gallery_id())
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()

            print("Gallery updated successfully.")
            return True

        except Exception as e:
            print("Error updating gallery:", e)
            return False

    def removeGallery(self, gallery_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check = "SELECT * FROM Gallery WHERE GalleryID = %s"
            cursor.execute(sql_check, (gallery_id,))
            gallery_data = cursor.fetchone()

            if gallery_data:
                sql_delete = "DELETE FROM Gallery WHERE GalleryID = %s"
                cursor.execute(sql_delete, (gallery_id,))
                connection.commit()
                cursor.close()
                print("Gallery removed successfully.")
                return True
            else:
                print("Gallery with ID", gallery_id, "does not exist.")
                return False

        except Exception as e:
            print("Error removing gallery:", e)
            return False

    def searchGalleries(self, keyword):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = "SELECT * FROM Gallery WHERE Name LIKE %s OR Description LIKE %s"
            keyword_like = f"%{keyword}%"
            cursor.execute(sql, (keyword_like, keyword_like))
            galleries_data = cursor.fetchall()

            galleries = []
            for gallery_data in galleries_data:
                gallery = Gallery(gallery_data[0], gallery_data[1], gallery_data[2], gallery_data[3], gallery_data[4],
                                  gallery_data[5])
                galleries.append(gallery)

            return galleries

        except Exception as e:
            print("Error searching galleries:", e)

    def getGalleryById(self, gallery_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            sql = "SELECT * FROM Gallery WHERE GalleryID = %s"
            cursor.execute(sql, (gallery_id,))
            gallery_data = cursor.fetchone()

            if gallery_data:
                gallery = Gallery(gallery_data[0], gallery_data[1], gallery_data[2], gallery_data[3], gallery_data[4],
                                  gallery_data[5])
                return gallery
            else:
                print("Gallery with ID", gallery_id, "not found.")
                return None

        except Exception as e:
            print("Error retrieving gallery by ID:", e)
            return None

    # Artwork_gallery Management
    def addArtworkToGallery(self, gallery_id, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()


            sql_check = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql_check, (artwork_id,))
            artwork_data = cursor.fetchone()

            sql_check = "SELECT * FROM Gallery WHERE GalleryID = %s"
            cursor.execute(sql_check, (gallery_id,))
            gallery_data = cursor.fetchone()

            if artwork_data and gallery_data:
                sql_insert = "INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES (%s, %s)"
                cursor.execute(sql_insert, (artwork_id, gallery_id))
                connection.commit()
                print("Artwork added to gallery successfully.")
                cursor.close()
                return True
            else:
                print("Artwork or gallery does not exist.")
                return False
        except Exception as e:
            print("Error adding artwork to gallery:", e)

    def removeArtworkFromGallery(self, gallery_id, artwork_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            sql_check = "SELECT * FROM Artwork_Gallery WHERE ArtworkID = %s AND GalleryID = %s"
            cursor.execute(sql_check, (artwork_id, gallery_id))
            link_data = cursor.fetchone()

            if link_data:
                sql_delete = "DELETE FROM Artwork_Gallery WHERE ArtworkID = %s AND GalleryID = %s"
                cursor.execute(sql_delete, (artwork_id, gallery_id))
                connection.commit()
                cursor.close()
                print("Artwork removed from gallery successfully.")
                return True
            else:
                print("Artwork is not linked to the gallery.")

                return False
        except Exception as e:
            print("Error removing artwork from gallery:", e)

    def getArtworksOfGallery(self, gallery_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            sql = ("SELECT a.* FROM Artwork a INNER JOIN Artwork_Gallery ag ON a.ArtworkID = ag.ArtworkID WHERE "
                   "ag.GalleryID = %s")
            cursor.execute(sql, (gallery_id,))
            artworks_data = cursor.fetchall()

            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(artwork_data[0], artwork_data[1], artwork_data[2], artwork_data[3], artwork_data[4],
                                  artwork_data[5], artwork_data[6])
                artworks.append(artwork)

            return artworks

        except Exception as e:
            print("Error retrieving artworks of gallery:", e)

    # Artist management
    def createArtist(self, artist):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_insert = ("INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation) "
                          "VALUES (%s, %s, %s, %s, %s, %s)")
            values = (artist.get_name(), artist.get_biography(), artist.get_birth_date(), artist.get_nationality(),
                      artist.get_website(), artist.get_contact_information())
            cursor.execute(sql_insert, values)
            connection.commit()
            print("Artist added successfully.")
            artist_id = cursor.lastrowid
            print("Your Artist ID:", artist_id)
            cursor.close()
            return True

        except Exception as e:
            print("Error adding artist:", e)
            return False

    def updateArtist(self, artist):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            sql_update = ("UPDATE Artist SET Name = %s, Biography = %s, BirthDate = %s, Nationality = %s, Website = "
                          "%s, ContactInformation = %s WHERE ArtistID = %s")
            value = (artist.get_name(), artist.get_biography(), artist.get_birth_date(), artist.get_nationality(),
                     artist.get_website(), artist.get_contact_information(), artist.get_artist_id())
            cursor.execute(sql_update, value)
            connection.commit()
            cursor.close()
            print("Artist updated successfully.")
            return True

        except Exception as e:
            print("Error updating artist:", e)

    def deleteArtist(self, artist_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql_check = "SELECT * FROM Artist WHERE ArtistID = %s"
            cursor.execute(sql_check, (artist_id,))
            gallery_data = cursor.fetchone()

            if gallery_data:
                sql_delete = "DELETE FROM Artist WHERE ArtistID = %s"
                cursor.execute(sql_delete, (artist_id,))
                connection.commit()
                cursor.close()
                print("Artist removed successfully.")
                return True
            else:
                print("No artist found.")
        except Exception as e:
            print("Error removing artist:", e)
        return False

    def getArtistById(self, artist_id):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            sql = "SELECT * FROM Gallery WHERE ArtistID = %s"
            cursor.execute(sql, (artist_id,))
            artist_data = cursor.fetchone()

            if artist_data:
                artist = Artist(artist_data[0], artist_data[1], artist_data[2], artist_data[3], artist_data[4],
                                artist_data[5], artist_data[6])
                return artist
            else:
                print("Artist with ID", artist_id, "not found.")
                return None

        except Exception as e:
            print("Error retrieving gallery by ID:", e)
        return None

    # User management
    def createUser(self, user):
        pass

    def updateUser(self, user):
        pass

    def deleteUser(self, user_id):
        pass

    def getUserById(self, user_id):
        pass
