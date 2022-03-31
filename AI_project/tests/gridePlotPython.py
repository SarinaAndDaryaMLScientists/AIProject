import hexalattice
from hexalattice.hexalattice import create_hex_grid

hex_centers, _ = create_hex_grid(n=100, do_plot=True)
centers_x = hex_centers[:, 0]
centers_x = hex_centers[:, 1]
