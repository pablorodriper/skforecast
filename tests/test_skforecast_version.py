from skforecast import __version__
import tomli

def test_version_in_init_and_pyproject_toml(version="0.10.0rc1"):
    """
    Test that version in __init__.py and pyproject.toml are the same.

    Parameters
    ----------
    version : str, optional
    """

    with open("./pyproject.toml", mode='rb') as fp:
        pyproject = tomli.load(fp)

    version_in_tolm = pyproject['project']['version']
    version_in_init = __version__

    assert version_in_init ==  version
    assert version_in_tolm == version    


# Test are located inside each module's folder