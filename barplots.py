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



# Plot a barplot using different color by group of rows
color_palette = {
    'Struggling Stars': 'red',
    'Developing Dynamos': 'orange',
    'Competent Champions': 'green',
    'Exceptional Experts': 'blue',
    'Elite Achievers': 'purple'
}
def plot_barplot(df, x_axis, y_axis, title, rotation, color_palette, group_name):
    """plot barplot with rotation xaxis"""
    ax = sns.barplot(x=x_axis,
                     y=y_axis,
                     data=df,
                     hue=group_name,
                     palette=color_palette
                     )
    if rotation:
        ax.set_xticklabels(ax.get_xticklabels(), rotation)
    sns.despine(
        left=True,
        bottom=True
    )
    plt.title(title)
    plt.show()


