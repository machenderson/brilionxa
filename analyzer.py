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
