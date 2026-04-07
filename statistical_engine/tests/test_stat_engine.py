"""
Unit Tests for Statistical Engine
Using Python's built-in unittest framework.
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.odd_list = [1, 2, 3, 4, 5]
        self.even_list = [1, 2, 3, 4, 5, 6]
        self.multimodal = [1, 1, 2, 2, 3, 4]
        self.unique_all = [1, 2, 3, 4, 5, 6, 7, 8]
        self.single_value = [5, 5, 5, 5, 5]
    
    # ========== MEAN TESTS ==========
    def test_mean_calculation(self):
        engine = StatEngine(self.odd_list)
        self.assertEqual(engine.get_mean(), 3.0)
    
    def test_mean_with_floats(self):
        engine = StatEngine([1.5, 2.5, 3.5])
        self.assertEqual(engine.get_mean(), 2.5)
    
    # ========== MEDIAN TESTS ==========
    def test_median_odd_list(self):
        engine = StatEngine(self.odd_list)
        self.assertEqual(engine.get_median(), 3.0)
    
    def test_median_even_list(self):
        engine = StatEngine(self.even_list)
        self.assertEqual(engine.get_median(), 3.5)
    
    def test_median_unsorted(self):
        engine = StatEngine([5, 1, 4, 2, 3])
        self.assertEqual(engine.get_median(), 3.0)
    
    # ========== MODE TESTS ==========
    def test_mode_normal(self):
        engine = StatEngine([1, 2, 2, 3, 3, 3, 4])
        self.assertEqual(engine.get_mode(), [3])
    
    def test_mode_multimodal(self):
        engine = StatEngine(self.multimodal)
        self.assertEqual(engine.get_mode(), [1, 2])
    
    def test_mode_all_unique(self):
        engine = StatEngine(self.unique_all)
        self.assertEqual(engine.get_mode(), "All values are unique - no mode exists")
    
    # ========== VARIANCE TESTS ==========
    def test_population_variance(self):
        # Known: For [1,2,3,4,5], mean=3, variance_pop = (4+1+0+1+4)/5 = 2
        engine = StatEngine(self.odd_list)
        self.assertEqual(engine.get_variance(is_sample=False), 2.0)
    
    def test_sample_variance(self):
        # Known: For [1,2,3,4,5], mean=3, variance_sample = (4+1+0+1+4)/4 = 2.5
        engine = StatEngine(self.odd_list)
        self.assertEqual(engine.get_variance(is_sample=True), 2.5)
    
    # ========== STANDARD DEVIATION TESTS ==========
    def test_standard_deviation(self):
        engine = StatEngine(self.odd_list)
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), math.sqrt(2), places=5)
    
    def test_single_value_std_dev(self):
        engine = StatEngine(self.single_value)
        self.assertEqual(engine.get_standard_deviation(is_sample=False), 0.0)
    
    # ========== OUTLIER TESTS ==========
    def test_outlier_detection(self):
        # Dataset with clear outlier: 100 is far from others
        engine = StatEngine([10, 12, 11, 13, 10, 12, 11, 100])
        outliers = engine.get_outliers(threshold=2)
        self.assertIn(100.0, outliers)
    
    def test_no_outliers(self):
        engine = StatEngine([1, 2, 3, 4, 5, 6, 7, 8])
        outliers = engine.get_outliers(threshold=3)
        self.assertEqual(outliers, [])
    
    # ========== ERROR HANDLING TESTS ==========
    def test_empty_list_error(self):
        with self.assertRaises(ValueError) as context:
            StatEngine([])
        self.assertIn("empty", str(context.exception).lower())
    
    def test_mixed_data_types_error(self):
        with self.assertRaises(TypeError) as context:
            StatEngine([1, 2, '3', None, 5])
        self.assertIn("not numeric", str(context.exception).lower())
    
    def test_string_data_error(self):
        with self.assertRaises(TypeError):
            StatEngine([1, 2, "hello", 4])
    
    def test_numeric_strings_work(self):
        # Numeric strings should be convertible
        engine = StatEngine([1, 2, "3", "4.5", 5])
        self.assertEqual(engine.get_mean(), 3.1)  # (1+2+3+4.5+5)/5 = 15.5/5 = 3.1
    
    # ========== COMPREHENSIVE TESTS ==========
    def test_end_to_end_analysis(self):
        """Test full statistical analysis on a realistic dataset"""
        engine = StatEngine([15, 18, 22, 19, 21, 20, 18, 100, 19, 20])
        
        self.assertAlmostEqual(engine.get_mean(), 27.2, places=1)
        self.assertEqual(engine.get_median(), 19.5)
        self.assertAlmostEqual(engine.get_variance(is_sample=True), 657.95556, places=3)
        
        outliers = engine.get_outliers(threshold=2)
        self.assertIn(100.0, outliers)


# Add math import for the test
import math

if __name__ == "__main__":
    unittest.main()