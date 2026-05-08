import seaborn as sns
import matplotlib.pyplot as plt

# Estilo general
sns.set_style('whitegrid')

# Cargar el dataset penguins
penguins = sns.load_dataset('penguins')

# Crear FacetGrid por sex y species, con hue por island
g = sns.FacetGrid(
    penguins,
    row='sex',
    col='species',
    hue='island',
    margin_titles=True,
    height=4,
    aspect=1.1,
    palette='Set2',
    despine=False
)

g.map_dataframe(
    sns.scatterplot,
    x='flipper_length_mm',
    y='body_mass_g',
    alpha=0.7,
    s=50
)

g.add_legend(title='Island')

g.set_axis_labels('Flipper length (mm)', 'Body mass (g)')

g.set(xlim=(penguins['flipper_length_mm'].min() - 5, penguins['flipper_length_mm'].max() + 5),
      ylim=(penguins['body_mass_g'].min() - 200, penguins['body_mass_g'].max() + 200))

g.fig.subplots_adjust(top=0.88, hspace=0.3, wspace=0.2)

g.fig.suptitle('Scatter de flipper_length_mm vs body_mass_g por species y sex', fontsize=16, fontweight='bold')

plt.show()
