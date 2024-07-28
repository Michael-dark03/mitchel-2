import numpy as np

# (A) Create array foo from 0 to 29 using arange
foo = np.arange(30)
print("Foo:", foo)
print("Foo shape:", foo.shape)

# (B) Reshape foo to a 2D matrix and store in bar
bar = foo.reshape(6, 5)
print("\nBar:", bar)
print("Bar shape:", bar.shape)

# (C) Reshape bar to a 3D matrix and store in baz
baz = bar.reshape(3, 2, 5)
print("\nBaz:", baz)
print("Baz shape:", baz.shape)

# (D) Update the second row of bar
bar[1, 0] = -1
print("\nUpdated Bar:", bar)
print("Foo did not change because reshape creates a new copy.")
print("Baz did not change as it was reshaped from bar, which is a copy.")

# (E) Sum baz over different dimensions
sum_over_second_dim = np.sum(baz, axis=1)
sum_over_third_dim = np.sum(baz, axis=2)
sum_over_first_and_third_dim = np.sum(baz, axis=(0, 2))
print("\nSum over second dimension:\n", sum_over_second_dim)
print("\nSum over third dimension:\n", sum_over_third_dim)
print("\nSum over first and third dimension:\n", sum_over_first_and_third_dim)

# (F) Slicing operations
row_2_bar = bar[1]
print("\nSecond row of Bar:", row_2_bar)

last_column_bar = bar[:,-1]
print("\nLast column of Bar:", last_column_bar)

top_right_submatrix_bar = bar[:2, 3:]
print("\nTop right 2x2 submatrix of Bar:\n", top_right_submatrix_bar)