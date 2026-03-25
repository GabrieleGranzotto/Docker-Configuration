import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm, cbook
import numpy as np
import pandas as pd
plt.style.use('ggplot')

def plot_3d(csv_name, default_cmap='RdYlBu_r', save_plot=False, output_filename='graphs/3d_plot.png'):
    def parsing_csv_name(csv_name):
        parts = csv_name.split('/')[-1].replace('.csv', '').split('_')
        infrastructure = parts[0].capitalize()
        program = parts[1].capitalize()
        type_test = 'Shared' if parts[2] == 'condiviso' else 'Local'
        cache_test = 'No Direct I/O' if parts[3] == 'cache' else 'Direct I/O'
        if parts[4] == 'cache':
            idx = 5
        else:
            idx = 4
        metric_test = 'Read' if parts[idx] == 'rread' else 'Write'
        return [infrastructure, program, type_test, cache_test, metric_test]
    name_params = parsing_csv_name(csv_name)

    angle = 80
    elevation = 15
    standard_azimuth = -60
    azimuth = angle + standard_azimuth

    df = pd.read_csv(csv_name, index_col=0).dropna()
    z = df.values
    x = df.columns.values.astype(float)
    y = df.index.values

    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='3d'))

    ax.view_init(elev=elevation, azim=azimuth)
    ls = LightSource(azdeg=120, altdeg=90)

    hmin, hmax = -1_000_000, 11_000_000
    norm = cm.colors.Normalize(vmin=hmin, vmax=hmax)
    rgb = ls.shade(z, cmap=plt.get_cmap(default_cmap), norm=norm, vert_exag=0.1, blend_mode='soft')
    ax.set_zlim(0, 10_000_000)
    ax.set_xlim(4, np.max(x))
    ax.set_ylim(64, np.max(y))
    ax.plot_surface(X, Y, z, rstride=1, cstride=1, facecolors=rgb,
                    linewidth=0, antialiased=False, shade=False)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    ax.set_title(f'{name_params[1]} Plot - {name_params[0]} {name_params[2]} {name_params[3]} Test: {name_params[4]}')
    ax.set_xlabel('Record Length')
    ax.set_ylabel('File Size (kB)')
    ax.set_zlabel(f'{name_params[4]} Throughput')

    m = cm.ScalarMappable(cmap=plt.get_cmap(default_cmap))
    m.set_clim(hmin, hmax)
    m.set_array(z)
    fig.colorbar(m, shrink=0.5, aspect=10, ax=ax, label='Z value')
    if save_plot:
        # save plot with less white space around
        plt.savefig(output_filename, dpi=400, bbox_inches='tight')
    plt.close()

path_csv = './misc/risultati_benchmark/'
path_plot_save = './misc/graphs/'
program_name = 'iozone'
infrastructure_name = ['vm', 'docker']
type_test = ['locale', 'condivisa']
cache_test = ['cache', 'no_cache']
metrics_test = ['rread', 'rwrite']
for type_t in type_test:
    for cache_t in cache_test:
        for metric_t in metrics_test:
            for infrastructure in infrastructure_name:
                csv_name = f'{path_csv}{infrastructure}_{program_name}_{type_t}_{cache_t}_{metric_t}.csv'
                output_filename = f'{path_plot_save}{infrastructure}_{program_name}_{type_t}_{cache_t}_{metric_t}_3d_plot.png'
                plot_3d(csv_name, save_plot=True, output_filename=output_filename)