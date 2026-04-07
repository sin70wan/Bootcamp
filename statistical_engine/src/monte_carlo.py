"""
Monte Carlo Simulation Module
Simulates server crash probabilities to demonstrate Law of Large Numbers.
"""

import random
from typing import Dict, List


def simulate_crashes(days: int) -> Dict:
    """
    Simulate daily server crashes with 4.5% probability per day.
    
    Args:
        days: Number of days to simulate
    
    Returns:
        Dictionary containing simulation results
    """
    crash_probability = 0.045  # 4.5% chance per day
    
    crashes = 0
    daily_results = []
    
    for day in range(days):
        # Generate random number between 0 and 1
        rand_num = random.random()
        
        # Crash occurs if random number < crash probability
        if rand_num < crash_probability:
            crashes += 1
            daily_results.append(1)
        else:
            daily_results.append(0)
    
    simulated_probability = crashes / days
    
    return {
        "days": days,
        "total_crashes": crashes,
        "simulated_probability": simulated_probability,
        "theoretical_probability": crash_probability,
        "daily_results": daily_results,
        "difference": abs(simulated_probability - crash_probability)
    }


def run_lln_demonstration() -> None:
    """
    Run simulations for different sample sizes to demonstrate LLN.
    """
    print("\n" + "="*70)
    print("LAW OF LARGE NUMBERS DEMONSTRATION")
    print("="*70)
    print("\nTheoretical crash probability: 4.5% (0.045)\n")
    
    sample_sizes = [30, 365, 10000]
    results = []
    
    for days in sample_sizes:
        result = simulate_crashes(days)
        results.append(result)
        
        print(f"Simulation for {days} days:")
        print(f"  ├── Total crashes: {result['total_crashes']}")
        print(f"  ├── Simulated probability: {result['simulated_probability']:.4f} ({result['simulated_probability']*100:.2f}%)")
        print(f"  ├── Theoretical probability: {result['theoretical_probability']:.3f} ({result['theoretical_probability']*100:.1f}%)")
        print(f"  └── Difference: {result['difference']:.4f}")
        print()
    
    # Interpretation
    print("-"*70)
    print("INTERPRETATION:")
    print("-"*70)
    print("""
    The Law of Large Numbers states that as sample size increases, the
    simulated (empirical) probability converges to the theoretical probability.
    
    Observations from our simulation:
    - At 30 days: The simulated probability can be significantly different
      from 4.5% due to random chance (small sample size).
    - At 365 days (1 year): The simulated probability gets closer to 4.5%,
      but still has noticeable variation.
    - At 10,000 days: The simulated probability is very close to 4.5%,
      demonstrating convergence.
    
    Why it's dangerous for the startup:
    Using only 30 days of data to predict yearly maintenance budgets
    is risky because the small sample may not represent the true 4.5%
    crash rate. If the 30-day period coincidentally had fewer crashes,
    the startup would under-budget for maintenance and face unexpected
    costs. Conversely, if it had more crashes, they'd over-budget.
    
    Reliable predictions require large sample sizes that reflect the
    true underlying probability.
    """)
    
    return results


if __name__ == "__main__":
    run_lln_demonstration()