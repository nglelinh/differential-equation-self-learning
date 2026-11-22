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


def vector_field(ax, A, xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), density=17, color=FIELD):
    x = np.linspace(*xlim, density)
    y = np.linspace(*ylim, density)
    X, Y = np.meshgrid(x, y)
    U = A[0, 0] * X + A[0, 1] * Y
    V = A[1, 0] * X + A[1, 1] * Y
    N = np.sqrt(U**2 + V**2) + 1e-9
    ax.quiver(X, Y, U / N, V / N, color=color, angles='xy', scale_units='xy', scale=12, width=0.003)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect('equal')
    setup_axes(ax, '$x_1$', '$x_2$')
