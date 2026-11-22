from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 10


IMG_PATH = Path(__file__).resolve().parent

NAVY = '#1d4ed8'
BLUE = '#2563eb'
SKY = '#60a5fa'
RED = '#b91c1c'
ROSE = '#f87171'
TEAL = '#0f766e'
CYAN = '#0891b2'
GREEN = '#15803d'
AMBER = '#d97706'
PURPLE = '#7c3aed'
SLATE = '#334155'
GRID = '#e5e7eb'
AXIS = '#111827'
FIELD = '#cbd5e1'


def setup_axes(ax, xlabel, ylabel, x_zero=True, y_zero=True):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, color=GRID, linewidth=0.8)
    if y_zero:
        ax.axhline(y=0, color=AXIS, linewidth=1.0, zorder=2)
    if x_zero:
        ax.axvline(x=0, color=AXIS, linewidth=1.0, zorder=2)


def savefig(fig, filename):
    fig.tight_layout()
    fig.savefig(IMG_PATH / filename, dpi=220, bbox_inches='tight')
    plt.close(fig)


def second_order_solution(r1, r2, t, y0=1.0, v0=0.0):
    if np.isclose(r1, r2):
        c1 = y0
        c2 = v0 - r1 * y0
        y = (c1 + c2 * t) * np.exp(r1 * t)
        return y, c1, c2
    a = np.array([[1.0, 1.0], [r1, r2]])
    b = np.array([y0, v0])
    c1, c2 = np.linalg.solve(a, b)
    return c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t), c1, c2
