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


def rk4(f, x0, t):
    x = np.zeros((len(t), len(np.atleast_1d(x0))), dtype=float)
    x[0] = np.asarray(x0, dtype=float)
    for i in range(len(t) - 1):
        h = t[i + 1] - t[i]
        xi = x[i]
        k1 = np.asarray(f(xi, t[i]))
        k2 = np.asarray(f(xi + 0.5 * h * k1, t[i] + 0.5 * h))
        k3 = np.asarray(f(xi + 0.5 * h * k2, t[i] + 0.5 * h))
        k4 = np.asarray(f(xi + h * k3, t[i] + h))
        x[i + 1] = xi + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x


def stream_field(ax, rhs, xlim, ylim, density=25, color=FIELD):
    x = np.linspace(*xlim, density)
    y = np.linspace(*ylim, density)
    X, Y = np.meshgrid(x, y)
    U, V = rhs(X, Y)
    ax.streamplot(x, y, U, V, density=1.2, color=color, linewidth=1.0, arrowsize=1.0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
