from abc import ABC, abstractmethod


class IAdditionalFunction(ABC):
    @abstractmethod
    def addGallery(self, gallery):
        pass

    @abstractmethod
    def updateGallery(self, gallery):
        pass

    @abstractmethod
    def removeGallery(self, gallery_id):
        pass

    @abstractmethod
    def getGalleryById(self, gallery_id):
        pass

    @abstractmethod
    def searchGalleries(self, keyword):
        pass

    # Artwork_gallery Management
    @abstractmethod
    def addArtworkToGallery(self, gallery_id, artwork_id):
        pass

    @abstractmethod
    def removeArtworkFromGallery(self, gallery_id, artwork_id):
        pass

    @abstractmethod
    def getArtworksOfGallery(self, gallery_id):
        pass

    # Artist management
    @abstractmethod
    def createArtist(self, artist):
        pass

    @abstractmethod
    def updateArtist(self, artist):
        pass

    @abstractmethod
    def deleteArtist(self, artist_id):
        pass

    @abstractmethod
    def getArtistById(self, artist_id):
        pass

    # User management
    @abstractmethod
    def createUser(self, user):
        pass

    @abstractmethod
    def updateUser(self, user):
        pass

    @abstractmethod
    def deleteUser(self, user_id):
        pass

    @abstractmethod
    def getUserById(self, user_id):
        pass
