import os, sys

print(os.getcwd())
print('Done down here!')

def whereami() -> str:
    """Print current working directory
    Edit

    This is a paragraph that contains `a link`_.

    .. _a link: https://domain.invalid/
    :repository_url:`Repository<>`

    Returns:
        str: Current working directory

    """
    cwd = os.getcwd()
    print(cwd)
    return cwd

def whoami():
    print(sys.executable)