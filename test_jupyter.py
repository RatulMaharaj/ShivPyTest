# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Heading

# %%
from platform import python_version

print(python_version())

# %% [markdown]
# This function returns the square of a number.

# %%
def square(x):
    return x ** 2


# %%
print(square(2))


# %%
