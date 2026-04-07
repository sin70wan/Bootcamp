"""
Statistical Engine Module
Implements core statistical calculations from scratch using only Python standard library.
"""

import math
from typing import List, Union, Tuple, Any


class StatEngine:
    """
    A pure-Python statistical engine for 1D numerical data.
    Calculates central tendency, dispersion, and outliers without external libraries.
    """
    
    def __init__(self, data: List[Any]):
        """
        Initialize the StatEngine with data.
        
        Args:
            data: List of numerical values (integers or floats)
        
        Raises:
            TypeError: If data contains non-numeric values
            ValueError: If data is empty
        """
        self.raw_data = data
        self.cleaned_data = self._clean_data(data)
        
    def _clean_data(self, data: List[Any]) -> List[float]:
        """
        Clean and validate input data.
        
        Args:
            data: Raw input list
        
        Returns:
            List of floats (cleaned numeric data)
        
        Raises:
            TypeError: If any value cannot be converted to float
            ValueError: If list is empty after cleaning
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        cleaned = []
        for i, val in enumerate(data):
            try:
                # Try to convert to float (handles ints, floats, numeric strings)
                cleaned.append(float(val))
            except (ValueError, TypeError):
                raise TypeError(f"Element at index {i} ('{val}') is not numeric")
        
        if not cleaned:
            raise ValueError("No valid numeric data found")
        
        return cleaned
    
    def get_mean(self) -> float:
        """
        Calculate arithmetic mean from scratch.
        
        Returns:
            Mean value as float
        """
        total = 0
        for val in self.cleaned_data:
            total += val
        return total / len(self.cleaned_data)
    
    def get_median(self) -> float:
        """
        Calculate median from scratch.
        Handles both odd and even list lengths.
        
        Returns:
            Median value as float
        """
        sorted_data = sorted(self.cleaned_data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 1:
            # Odd number of elements - return middle element
            return sorted_data[mid]
        else:
            # Even number of elements - return average of two middle elements
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    
    def get_mode(self) -> Union[List[float], str]:
        """
        Calculate mode(s) from scratch.
        Handles multimodal distributions and unique value cases.
        
        Returns:
            List of mode values if found, or message string if all values unique
        """
        # Build frequency dictionary
        freq = {}
        for val in self.cleaned_data:
            freq[val] = freq.get(val, 0) + 1
        
        # Find maximum frequency
        max_freq = 0
        for count in freq.values():
            if count > max_freq:
                max_freq = count
        
        # If max frequency is 1, all values are unique
        if max_freq == 1:
            return "All values are unique - no mode exists"
        
        # Find all values with max frequency
        modes = []
        for val, count in freq.items():
            if count == max_freq:
                modes.append(val)
        
        return sorted(modes)
    
    def get_variance(self, is_sample: bool = True) -> float:
        """
        Calculate variance from scratch.
        
        Args:
            is_sample: True for sample variance (Bessel's correction, n-1)
                      False for population variance (n)
        
        Returns:
            Variance value as float
        """
        mean = self.get_mean()
        n = len(self.cleaned_data)
        
        # Sum of squared deviations
        sum_sq_diff = 0
        for val in self.cleaned_data:
            diff = val - mean
            sum_sq_diff += diff * diff
        
        # Apply Bessel's correction for sample variance
        denominator = n - 1 if is_sample else n
        
        if denominator == 0:
            raise ValueError("Cannot calculate variance with n=1 for sample")
        
        return sum_sq_diff / denominator
    
    def get_standard_deviation(self, is_sample: bool = True) -> float:
        """
        Calculate standard deviation from scratch.
        
        Args:
            is_sample: True for sample standard deviation (Bessel's correction)
                      False for population standard deviation
        
        Returns:
            Standard deviation as float
        """
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)
    
    def get_outliers(self, threshold: float = 2.0) -> List[float]:
        """
        Identify outliers using the standard deviation method.
        Outliers are points > threshold standard deviations from the mean.
        
        Args:
            threshold: Number of standard deviations to use as cutoff
        
        Returns:
            List of outlier values
        """
        mean = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)
        
        if std_dev == 0:
            return []  # No variation, no outliers
        
        outliers = []
        for val in self.cleaned_data:
            z_score = abs(val - mean) / std_dev
            if z_score > threshold:
                outliers.append(val)
        
        return outliers