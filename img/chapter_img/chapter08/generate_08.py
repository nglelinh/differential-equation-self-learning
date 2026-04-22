#!/usr/bin/env python3
"""
Generate educational illustrations for Chapter 08 - Fourier Series and Transforms.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


IMG_PATH = Path(
    "/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter08"
)
IMG_PATH.mkdir(parents=True, exist_ok=True)

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update(
    {
        "figure.figsize": (12, 8),
        "font.size": 12,
        "axes.titlesize": 15,
        "axes.labelsize": 12,
        "legend.fontsize": 10,
        "lines.linewidth": 2.2,
    }
)


def square_wave(x: np.ndarray) -> np.ndarray:
    y = np.sign(np.sin(x))
    y[np.isclose(np.sin(x), 0.0)] = 0.0
    return y


def sawtooth_wave(x: np.ndarray) -> np.ndarray:
    return ((x + np.pi) % (2 * np.pi) - np.pi) / np.pi


def triangle_wave(x: np.ndarray) -> np.ndarray:
    return 2 * np.abs(sawtooth_wave(x)) - 1


def square_partial_sum(x: np.ndarray, n_terms: int) -> np.ndarray:
    s = np.zeros_like(x)
    for k in range(n_terms):
        n = 2 * k + 1
        s += np.sin(n * x) / n
    return 4 * s / np.pi


def triangle_coeffs(max_n: int) -> np.ndarray:
    coeffs = np.zeros(max_n)
    for n in range(1, max_n + 1):
        if n % 2 == 1:
            coeffs[n - 1] = 8 / (np.pi**2 * n**2) * ((-1) ** ((n - 1) // 2))
    return coeffs


def gaussian(x: np.ndarray, sigma: float = 0.55) -> np.ndarray:
    return np.exp(-(x**2) / (2 * sigma**2))


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(IMG_PATH / name, format="svg", bbox_inches="tight")
    plt.close(fig)


def figure_01() -> None:
    x = np.linspace(-np.pi, np.pi, 1200)
    target = square_wave(x)
    partials = [1, 3, 9]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax = axes[0]
    ax.plot(x, target, color="#0f172a", label="periodic target")
    for n, color in zip(partials, ["#16a34a", "#0ea5e9", "#ef4444"]):
        ax.plot(x, square_partial_sum(x, n), color=color, alpha=0.95, label=f"{n} odd harmonics")
    ax.set_ylabel("f(x)")
    ax.set_title("Periodic function and Fourier partial sums")
    ax.legend(loc="upper right", ncol=2)

    ax = axes[1]
    harmonics = np.arange(1, 12, 2)
    amplitudes = 4 / (np.pi * harmonics)
    ax.bar(harmonics, amplitudes, color="#2563eb", width=0.7)
    ax.set_xlabel("harmonic n")
    ax.set_ylabel("amplitude")
    ax.set_title("Odd harmonics of the square wave")
    ax.set_xticks(harmonics)

    for axis in axes:
        axis.set_xlim(-np.pi, np.pi)
        axis.grid(alpha=0.25)

    save(fig, "01_periodic_functions_fourier_series.svg")


def figure_02() -> None:
    x = np.linspace(-np.pi, np.pi, 1000)
    f = triangle_wave(x)
    n_max = 11
    coeffs = triangle_coeffs(n_max)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    ax = axes[0]
    ax.plot(x, f, color="#0f172a")
    ax.fill_between(x, 0, f, color="#22c55e", alpha=0.15)
    ax.set_title("Function to project onto trigonometric modes")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(-np.pi, np.pi)

    ax = axes[1]
    n = np.arange(1, n_max + 1)
    colors = ["#2563eb" if abs(c) > 0 else "#cbd5e1" for c in coeffs]
    ax.bar(n, coeffs, color=colors, width=0.72)
    ax.axhline(0.0, color="#0f172a", linewidth=1)
    ax.set_title("Fourier coefficients: orthogonality isolates each mode")
    ax.set_xlabel("mode n")
    ax.set_ylabel("coefficient")
    ax.set_xticks(n)

    save(fig, "02_fourier_coefficients.svg")


def figure_03() -> None:
    x = np.linspace(-np.pi, np.pi, 1600)
    target = square_wave(x)
    partials = [5, 15, 60]

    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.2))

    ax = axes[0]
    ax.plot(x, target, color="#0f172a", linewidth=2.5, label="target")
    for n, color in zip(partials, ["#16a34a", "#0ea5e9", "#ef4444"]):
        ax.plot(x, square_partial_sum(x, n), color=color, label=f"{n} odd harmonics")
    ax.set_title("Global convergence away from jumps")
    ax.set_xlabel("x")
    ax.set_ylabel("partial sum")
    ax.set_xlim(-np.pi, np.pi)
    ax.legend(loc="upper right")

    ax = axes[1]
    zoom = np.abs(x) < 0.65
    ax.plot(x[zoom], target[zoom], color="#0f172a", linewidth=2.5, label="target")
    for n, color in zip(partials, ["#16a34a", "#0ea5e9", "#ef4444"]):
        ax.plot(x[zoom], square_partial_sum(x, n)[zoom], color=color, label=f"{n} odd harmonics")
    ax.axvline(0.0, color="#64748b", linestyle="--", linewidth=1.2)
    ax.set_title("Gibbs overshoot near a discontinuity")
    ax.set_xlabel("x")
    ax.set_ylabel("partial sum")
    ax.legend(loc="lower right")

    save(fig, "03_convergence_fourier_series.svg")


def figure_04() -> None:
    x = np.linspace(-np.pi, np.pi, 1000)
    even_f = np.cos(x) + 0.35 * np.cos(2 * x)
    odd_f = np.sin(x) - 0.35 * np.sin(2 * x)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)

    ax = axes[0]
    ax.plot(x, even_f, color="#2563eb")
    ax.plot(-x, even_f, color="#93c5fd", linestyle="--")
    ax.axvline(0.0, color="#0f172a", linewidth=1)
    ax.set_title("Even symmetry -> cosine series")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(-np.pi, np.pi)
    ax.text(-2.95, 1.05, "f(-x)=f(x)", color="#1d4ed8", fontsize=12)

    ax = axes[1]
    ax.plot(x, odd_f, color="#dc2626")
    ax.plot(-x, -odd_f, color="#fca5a5", linestyle="--")
    ax.axvline(0.0, color="#0f172a", linewidth=1)
    ax.set_title("Odd symmetry -> sine series")
    ax.set_xlabel("x")
    ax.set_xlim(-np.pi, np.pi)
    ax.text(-2.95, 1.05, "f(-x)=-f(x)", color="#b91c1c", fontsize=12)

    save(fig, "04_even_odd_functions.svg")


def figure_05() -> None:
    x_half = np.linspace(0, np.pi, 500)
    f_half = x_half / np.pi
    x_full = np.linspace(-np.pi, np.pi, 1000)
    even_ext = np.abs(x_full) / np.pi
    odd_ext = x_full / np.pi

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), sharey=True)

    ax = axes[0]
    ax.plot(x_half, f_half, color="#0f172a")
    ax.fill_between(x_half, 0, f_half, color="#22c55e", alpha=0.18)
    ax.set_title("Data only on [0, L]")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(-np.pi, np.pi)
    ax.set_xticks([0, np.pi])
    ax.set_xticklabels(["0", "L"])

    ax = axes[1]
    ax.plot(x_full, even_ext, color="#2563eb")
    ax.axvline(0.0, color="#0f172a", linewidth=1)
    ax.set_title("Even extension -> cosine modes")
    ax.set_xlabel("x")
    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels(["-L", "0", "L"])

    ax = axes[2]
    ax.plot(x_full, odd_ext, color="#dc2626")
    ax.axvline(0.0, color="#0f172a", linewidth=1)
    ax.axhline(0.0, color="#0f172a", linewidth=1)
    ax.set_title("Odd extension -> sine modes")
    ax.set_xlabel("x")
    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels(["-L", "0", "L"])

    save(fig, "05_half_range_expansions.svg")


def figure_06() -> None:
    x = np.linspace(-np.pi, np.pi, 1200)
    coeff_modes = np.array([1.15, 0.75, 0.45, 0.22, 0.12])
    f = sum(a * np.cos((i + 1) * x) for i, a in enumerate(coeff_modes))
    mode_energy = 0.5 * coeff_modes**2

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    ax = axes[0]
    ax.plot(x, f, color="#0f172a")
    ax.fill_between(x, 0, f**2 / np.max(f**2), color="#a78bfa", alpha=0.15)
    ax.set_title("Signal in physical space")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(-np.pi, np.pi)
    ax.text(-2.95, np.max(f) * 0.83, r"$\int |f|^2 \leftrightarrow \sum |c_n|^2$", fontsize=13)

    ax = axes[1]
    n = np.arange(1, len(coeff_modes) + 1)
    ax.bar(n, mode_energy, color="#7c3aed", width=0.72)
    ax.set_title("Energy carried by Fourier modes")
    ax.set_xlabel("mode n")
    ax.set_ylabel("energy contribution")
    ax.set_xticks(n)
    ax.text(0.65, mode_energy.max() * 0.93, f"total = {mode_energy.sum():.3f}", fontsize=12)

    save(fig, "06_parsevals_theorem.svg")


def figure_07() -> None:
    theta = np.linspace(0, 2 * np.pi, 600)
    unit_x = np.cos(theta)
    unit_y = np.sin(theta)
    n = np.arange(-5, 6)
    spectrum = np.exp(-0.26 * (n**2))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    ax = axes[0]
    ax.plot(unit_x, unit_y, color="#0f172a")
    ax.axhline(0.0, color="#94a3b8", linewidth=1)
    ax.axvline(0.0, color="#94a3b8", linewidth=1)
    for ang, label, color in [(np.pi / 4, r"$e^{ix}$", "#2563eb"), (-2 * np.pi / 3, r"$e^{-2ix}$", "#dc2626")]:
        ax.arrow(0, 0, np.cos(ang) * 0.9, np.sin(ang) * 0.9, width=0.018, color=color, length_includes_head=True)
        ax.text(np.cos(ang) * 1.02, np.sin(ang) * 1.02, label, color=color, fontsize=12)
    ax.set_title("Complex exponentials rotate on the unit circle")
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")

    ax = axes[1]
    ax.stem(n, spectrum, basefmt=" ", linefmt="#0ea5e9", markerfmt="o")
    ax.set_title("Complex coefficients indexed by positive and negative modes")
    ax.set_xlabel("mode n")
    ax.set_ylabel(r"$|c_n|$")
    ax.set_xticks(n)
    ax.axvline(0.0, color="#94a3b8", linewidth=1)

    save(fig, "07_complex_fourier_series.svg")


def figure_08() -> None:
    x = np.linspace(-8, 8, 1600)
    signal = gaussian(x, 0.85) * np.cos(4.8 * x)
    xi = np.fft.fftshift(np.fft.fftfreq(x.size, d=(x[1] - x[0]))) * 2 * np.pi
    spectrum = np.fft.fftshift(np.abs(np.fft.fft(signal)))
    spectrum /= spectrum.max()

    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.2))

    ax = axes[0]
    ax.plot(x, signal, color="#0f172a")
    ax.fill_between(x, 0, signal, color="#22c55e", alpha=0.14)
    ax.set_title("Localized signal in physical space")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(-8, 8)

    ax = axes[1]
    mask = np.abs(xi) < 12
    ax.plot(xi[mask], spectrum[mask], color="#2563eb")
    ax.fill_between(xi[mask], 0, spectrum[mask], color="#60a5fa", alpha=0.18)
    ax.set_title("Continuous frequency spectrum")
    ax.set_xlabel(r"frequency $\xi$")
    ax.set_ylabel(r"$|\hat f(\xi)|$")
    ax.set_xlim(-12, 12)

    save(fig, "08_fourier_transform_introduction.svg")


def main() -> None:
    figure_01()
    figure_02()
    figure_03()
    figure_04()
    figure_05()
    figure_06()
    figure_07()
    figure_08()
    print("Generated Chapter 08 illustrations")


if __name__ == "__main__":
    main()
