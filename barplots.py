# pip install seaborn
import seaborn as sns
def plot_barplot(df, x_axis, y_axis, title, vertical, rotation):
    """plot horizontal barplot with rotation xaxis"""
    ax = sns.barplot(x=x_axis, y=y_axis, data=df)
    if rotation:
        ax.set_xticklabels(ax.get_xticklabels(), rotation)
    if vertical:
      sns.despine(
          left=True,
          bottom=True
      )
    plt.title('Survivors')
    plt.show()


