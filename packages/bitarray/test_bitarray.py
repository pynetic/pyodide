from pyodide_test_runner import run_in_pyodide


@run_in_pyodide(packages=["bitarray-tests"])
def test_bitarray(selenium):
    import bitarray

    bitarray.test()
