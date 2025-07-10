from importlib.resources import files


def test_fontra_client_bundling():
    # Make sure the client folder exists and has been populated by the bundler
    names = list(files("fontra.client").iterdir())
    assert names
