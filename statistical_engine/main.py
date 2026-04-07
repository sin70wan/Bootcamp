"""
Statistical Engineering & Simulation - Main Entry Point
Demonstrates the complete statistical engine and Monte Carlo simulation.
"""

import json
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stat_engine import StatEngine
from monte_carlo import run_lln_demonstration, simulate_crashes


def load_salary_data():
    """Load the mock salary dataset from JSON file."""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_salaries.json')
    
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    return data['salaries']


def analyze_salaries():
    """Perform statistical analysis on startup salaries."""
    print("\n" + "="*70)
    print("STARTUP SALARY ANALYSIS")
    print("="*70)
    
    salaries = load_salary_data()
    engine = StatEngine(salaries)
    
    # Basic statistics
    mean = engine.get_mean()
    median = engine.get_median()
    mode = engine.get_mode()
    variance_sample = engine.get_variance(is_sample=True)
    variance_pop = engine.get_variance(is_sample=False)
    std_dev_sample = engine.get_standard_deviation(is_sample=True)
    outliers = engine.get_outliers(threshold=2)
    
    print(f"\n📊 Dataset: {len(salaries)} startup salaries")
    print(f"\n📈 CENTRAL TENDENCY:")
    print(f"   Mean:  ${mean:,.2f}")
    print(f"   Median: ${median:,.2f}")
    print(f"   Mode:  {mode}")
    
    print(f"\n📉 DISPERSION:")
    print(f"   Sample Variance: {variance_sample:,.2f}")
    print(f"   Population Variance: {variance_pop:,.2f}")
    print(f"   Standard Deviation (Sample): ${std_dev_sample:,.2f}")
    
    print(f"\n🔍 OUTLIER DETECTION (threshold=2σ):")
    print(f"   Found {len(outliers)} outliers:")
    for i, outlier in enumerate(outliers[:10]):  # Show first 10
        print(f"      {i+1}. ${outlier:,.2f}")
    if len(outliers) > 10:
        print(f"      ... and {len(outliers) - 10} more")
    
    print(f"\n" + "-"*70)
    print("WHY RELYING ONLY ON THE MEAN IS DANGEROUS:")
    print("-"*70)
    print(f"""
    The mean salary (${mean:,.0f}) is heavily skewed upward by a few extremely
    high salaries (executives, founders). However, the median salary (${median:,.0f})
    better represents what a typical employee earns.
    
    The large standard deviation (${std_dev_sample:,.0f}) indicates extreme volatility
    in compensation. Many employees earn much less than the mean, while a
    few earn astronomically more.
    
    This is why standard deviation is crucial - it reveals the "real picture"
    of volatility that the mean alone hides.
    """)


def run_monte_carlo():
    """Run the Monte Carlo simulation for server crashes."""
    print("\n" + "="*70)
    print("MONTE CARLO SERVER CRASH SIMULATION")
    print("="*70)
    run_lln_demonstration()


def main():
    """Main entry point."""
    print("\n" + "="*70)
    print("STATISTICAL ENGINEERING & SIMULATION")
    print("="*70)
    print("A pure-Python statistical engine demonstrating the Law of Large Numbers")
    
    # Part 1: Analyze salaries with our statistical engine
    analyze_salaries()
    
    # Part 2: Run Monte Carlo simulation
    run_monte_carlo()
    
    print("\n" + "="*70)
    print("✅ Analysis Complete!")
    print("="*70)


if __name__ == "__main__":
    main()