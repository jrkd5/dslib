import math
import matplotlib.pyplot as plt


SQRT_TWO_PI = math.sqrt(2 * math.pi)


def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float) -> float:
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def plot_normal_pdf() -> None:
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='m=0,s=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='m=0,s=2')
    plt.plot(xs, [normal_pdf(x, sigma=.5) for x in xs], ':', label='m=0,s=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='m=-1,s=1')
    plt.legend()
    plt.title("Various normal pdfs")
    plt.show()


def plot_normal_cdf() -> None:
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='m=0,s=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='m=0,s=2')
    plt.plot(xs, [normal_cdf(x, sigma=.5) for x in xs], ':', label='m=0,s=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='m=-1,s=1')
    plt.legend(loc=4)
    plt.title("Various normal cdfs")
    plt.show()


def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Find approximate inverse using binary seach"""

    #  if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z / 2)
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z

    return mid_z
