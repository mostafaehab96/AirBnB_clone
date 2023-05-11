#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review"""

    def test_inherits_from_base_model(self):
        """Test that Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test that Review has the expected attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of Review"""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertTrue(isinstance(review_dict["created_at"], str))
        self.assertTrue(isinstance(review_dict["updated_at"], str))
        self.assertTrue(isinstance(review_dict["id"], str))
        self.assertEqual(review_dict["place_id"], "")
        self.assertEqual(review_dict["user_id"], "")
        self.assertEqual(review_dict["text"], "")
        self.assertTrue("created_at" in review_dict)
        self.assertTrue("updated_at" in review_dict)
        self.assertTrue("id" in review_dict)
        self.assertTrue("place_id" in review_dict)
        self.assertTrue("user_id" in review_dict)
        self.assertTrue("text" in review_dict)

if __name__ == "__main__":
    unittest.main()

