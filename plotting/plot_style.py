"""Shared visual style for experiment plots."""

SPATIAL_FIGSIZE = (12, 9)
TITLE_FONT_SIZE = 22
AXIS_LABEL_FONT_SIZE = 17
TICK_FONT_SIZE = 15
LEGEND_FONT_SIZE = 14
NODE_LABEL_FONT_SIZE = 10
TARGET_LABEL_FONT_SIZE = 12
COLORBAR_LABEL_FONT_SIZE = 15


def apply_plot_style(plt) -> None:
    plt.rcParams.update(
        {
            "axes.titlesize": TITLE_FONT_SIZE,
            "axes.labelsize": AXIS_LABEL_FONT_SIZE,
            "xtick.labelsize": TICK_FONT_SIZE,
            "ytick.labelsize": TICK_FONT_SIZE,
            "legend.fontsize": LEGEND_FONT_SIZE,
        }
    )
