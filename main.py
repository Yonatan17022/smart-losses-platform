"""
Smart Losses Platform - Demo Version
Author: Yonatan David Bernal Piñeros
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_demo_curve():
    hours = np.arange(24)
    demand = 50 + 10 * np.sin(hours / 24 * 2 * np.pi)

    df = pd.DataFrame({
        "Hour": hours,
        "Demand_MW": demand
    })

    return df


def plot_curve(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Hour"], df["Demand_MW"])
    plt.title("Hourly Demand Curve")
    plt.xlabel("Hour")
    plt.ylabel("Demand (MW)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    curve = generate_demo_curve()
    print(curve.head())

    plot_curve(curve)
