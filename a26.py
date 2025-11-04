import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

def draw_flowchart(steps, filename="daily_routine_flowchart.png",
                   box_width=6, box_height=0.8, vspace=0.6, fontsize=10):
    n = len(steps)
    fig_height = n * (box_height + vspace) * 1.1
    fig = plt.figure(figsize=(6, max(4, fig_height)))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, n * (box_height + vspace) + 1)
    ax.axis('off')

    # compute y positions
    y_start = n * (box_height + vspace)
    positions = []
    for i in range(n):
        y = y_start - i * (box_height + vspace)
        positions.append(y)

    # center x coordinate
    x_center = 5
    for i, (step, y) in enumerate(zip(steps, positions)):
        # draw simple white box (no color)
        box = FancyBboxPatch((x_center - box_width/2, y - box_height/2),
                              box_width, box_height,
                              boxstyle="round,pad=0.3",
                              linewidth=1.2, edgecolor="black",
                              facecolor="white")  # <- white fill
        ax.add_patch(box)

        # wrap text if needed
        max_char_per_line = 30
        if len(step) > max_char_per_line:
            words = step.split()
            lines = []
            current = ""
            for w in words:
                if len(current) + 1 + len(w) <= max_char_per_line:
                    current = (current + " " + w).strip()
                else:
                    lines.append(current)
                    current = w
            lines.append(current)
            text = "\n".join(lines)
        else:
            text = step

        ax.text(x_center, y, text, ha="center", va="center", fontsize=fontsize)

        # draw arrow to next
        if i < n - 1:
            y_next = positions[i + 1]
            ax.annotate("",
                        xy=(x_center, y_next + box_height/2 + 0.02),
                        xytext=(x_center, y - box_height/2 - 0.02),
                        arrowprops=dict(arrowstyle="->", linewidth=1.2))

    plt.tight_layout()
    fig.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return os.path.abspath(filename)


if __name__ == "__main__":
    steps = [
        "Start",
        "Wake up",
        "Brush teeth / Shower",
        "Eat breakfast",
        "Go to school / work",
        "Do daily tasks / Meetings / Classes",
        "Return home",
        "Eat dinner",
        "Relax / Study / Hobby",
        "Prepare for next day",
        "Go to sleep",
        "End"
    ]

    out = draw_flowchart(steps)
    print("Flowchart saved to:", out)