This is a lightweight Python tool called "**Brilionx**". Its core function is a portfolio risk analyzer, specifically designed to calculate the Sharpe Ratio and volatility of asset portfolios, helping investors understand 'how much return each risk earns'.

## 🛠️ Name of the Tool ：Brilonx analyzer (v0.2)

This is a simple but powerful script that can evaluate asset performance based on historical return data.

### 1. Updated Code: `analyzer.py`

Python

```
import numpy as np

class LuminaQuant:
    """
    BrilionX Financial Analytics: LuminaQuant
    A lightweight tool for portfolio risk assessment.
    """
    def __init__(self, returns, risk_free_rate=0.02):
        """
        :param returns: List or Numpy Array of historical daily returns.
        :param risk_free_rate: Annualized risk-free rate (default 2%).
        """
        self.returns = np.array(returns)
        self.rf = risk_free_rate

    def calculate_volatility(self):
        """Calculates annualized volatility."""
        return np.std(self.returns) * np.sqrt(252)

    def calculate_sharpe_ratio(self):
        """Calculates the Sharpe Ratio."""
        avg_return = np.mean(self.returns) * 252
        annual_vol = self.calculate_volatility()
        if annual_vol == 0:
            return 0
        return (avg_return - self.rf) / annual_vol

    def calculate_max_drawdown(self):
        """
        Calculates the Maximum Drawdown (MDD).
        Returns: (mdd_value, cumulative_wealth_index)
        """
        # Calculate cumulative returns (wealth index) starting from 1
        cumulative_wealth = np.cumprod(1 + self.returns)
        
        # Calculate the running maximum
        running_max = np.maximum.accumulate(cumulative_wealth)
        
        # Calculate drawdown series
        drawdowns = (cumulative_wealth - running_max) / running_max
        
        # Identify the maximum drawdown
        max_drawdown = np.min(drawdowns)
        
        return max_drawdown, cumulative_wealth

# --- BrilionX Demo Usage ---
if __name__ == "__main__":
    # Simulate 252 days of daily returns
    np.random.seed(42)
    simulated_returns = np.random.normal(0.0005, 0.015, 252)
    
    lq = LuminaQuant(simulated_returns)
    mdd, wealth_index = lq.calculate_max_drawdown()
    
    print(f"--- BrilionX LuminaQuant Risk Report ---")
    print(f"Annual Volatility: {lq.calculate_volatility():.2%}")
    print(f"Sharpe Ratio:      {lq.calculate_sharpe_ratio():.2f}")
    print(f"Max Drawdown:      {mdd:.2%}")
```

---

### 2. Metric Definitions

| **Metric**       | **Description**                                | **Importance**                                 |  |  |  |
| ------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | -- | -- | -- |
| **Annual Volatility** | The standard deviation of returns scaled to a year.  | Measures the "intensity" of price swings.            |
| **Sharpe Ratio**      | Risk-adjusted return calculation.                    | Higher is better; indicates efficiency.              |
| **Max Drawdown**      | The peak-to-trough decline during a specific period. | Measures the "worst-case scenario" for capital loss. |

---

### 3. Open Source Documentation (`README.md`)

> **Project:** Brilonx analyzer
> 
> **Author:** **Brilionx**
> 
> **License:** MIT
> 
> **Overview:** > A minimalist Python utility for calculating core financial risk metrics. Designed for developers and quants who need quick, dependency-light risk analysis.
> 
> **How to Run:**
> 
> 1. Ensure `numpy` is installed: `pip install numpy`.
> 2. Run the script: `python analyzer.py`.
> 
> **Mathematical Logic:**
> 
> We utilize the Cumulative Wealth Index to track equity curves and calculate MDD as:
> 
> $$
> Drawdown_t = \frac{Wealth_t - \max(Wealth_{0...t})}{\max(Wealth_{0...t})}
> 
> $$

---
[Brilionx analyzer](https://github.com/machenderson/brilionxa)：This is a simple but powerful script that can evaluate asset performance based on historical return data.

[Brilionx FingerTrap](https://github.com/machenderson/brilionxf)：This tool identifies potential fat-finger incidents by detecting price deviations that significantly exceed typical market volatility within a narrow timeframe.

[Brilionx DataFetcher](https://github.com/machenderson/brilionxd)：The tool now includes a robust exporting feature to save your findings as persistent files.

[Brilionx CryptoPulse-Sentinel](https://github.com/machenderson/brilionxc)：This tool is divided into four distinct modules: ​Data Ingestion​, ​Quantitative Analysis​, ​Real-time Detection​, and ​Audit Export​.

---

### BrilionX, MEV, and Mindedge Venture: A Triumvirate of Stock Market Success Stories
