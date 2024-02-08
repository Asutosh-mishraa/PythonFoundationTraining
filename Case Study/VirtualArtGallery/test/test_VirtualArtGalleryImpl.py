import pytest
from unittest.mock import patch, Mock

from dao.AdditionalFunctionImpl import AdditionalFunctionImpl
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.ArtWorks import Artwork
from entity.Gallery import Gallery


def test_add_artwork():
    virtual_gallery = VirtualArtGalleryImpl()
    artwork = Artwork(None, "Test Artwork", "Test Description", "2024-02-10", "Oil on canvas", "test_image_url", 1)
    result = virtual_gallery.addArtwork(artwork)
    assert result == True


def test_update_artwork():
    virtual_gallery = VirtualArtGalleryImpl()
    artwork = Artwork(6, "Test Artwork", "Test Description new", "2024-02-10", "Oil on canvas", "test_image_url", 1)
    result = virtual_gallery.updateArtwork(artwork)
    assert result == True


def test_remove_artwork():
    virtual_gallery = VirtualArtGalleryImpl()
    removed = virtual_gallery.removeArtwork(6)
    assert removed == True


def test_search_artwork():
    virtual_gallery = VirtualArtGalleryImpl()
    result = virtual_gallery.searchArtworks(1)
    assert result is not None


def test_create_gallery():
    additional_functions = AdditionalFunctionImpl()
    gallery = Gallery(None, 'Test gallery Name', 'Test description', 'Test Location', 'Test Curator',
                      '10:00 AM - 6:00 PM')
    result = additional_functions.addGallery(gallery)
    assert result == True


def test_update_gallery():
    additional_functions = AdditionalFunctionImpl()
    gallery = Gallery(None, 'Test gallery Name', 'Test description', 'Test Location', 'Test Curator',
                      '10:00 AM - 6:00 PM')
    result = additional_functions.updateGallery(gallery)
    assert result == True


def test_remove_gallery():
    additional_functions = AdditionalFunctionImpl()
    result = additional_functions.removeGallery(6)
    assert result == True


def test_search_gallery():
    additional_functions = AdditionalFunctionImpl()
    result = additional_functions.getGalleryById(1)
    assert result is not None
