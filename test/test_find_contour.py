import unittest

from findContours import find_contours

def test_no_image():
    # assert find_contours("") == AttributeError
    pass

def test_simple_image():
    _, numContours, _ = find_contours('simpleLaser.jpg')
    assert numContours == 7
    
def test_small_real_image():
    _, numContours, _ = find_contours('smallRealBoard1.jpg')
    assert numContours == 11
    
def test_large_real_image():
    pass
    
def test_complicated_image():
    pass
    