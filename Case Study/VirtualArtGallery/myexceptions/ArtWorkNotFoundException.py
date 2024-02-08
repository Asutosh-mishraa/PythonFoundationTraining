class ArtWorkNotFoundException(Exception):
    def __init__(self, artwork_id):
        self.artwork_id = artwork_id

    def __str__(self):
        return f"Artwork with ID {self.artwork_id} not found in the database"
