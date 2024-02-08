from abc import ABC, abstractmethod


class IVirtualArtGallery(ABC):
    @abstractmethod
    def addArtwork(self, artwork):
        pass

    @abstractmethod
    def updateArtwork(self, artwork):
        pass

    @abstractmethod
    def removeArtwork(self, artworkID):
        pass

    @abstractmethod
    def getArtworkById(self, artworkID):
        pass

    @abstractmethod
    def searchArtworks(self, keyword):
        pass

    @abstractmethod
    def showAllArtworks(self):
        pass
    @abstractmethod
    def addArtworkToFavorite(self, userID, artworkID):
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self, userID, artworkID):
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self, userID):
        pass

    @abstractmethod
    def feedback(self, user_id, artwork_id, feedback_text):
        pass

    @abstractmethod
    def getFeedbacksByArtworkId(self, artwork_id):
        pass
