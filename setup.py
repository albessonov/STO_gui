from distutils.core import setup
import os
import py2exe

setup(

    windows=[{"script": "v2.py"}],

    options={"py2exe": {"includes": []}},

    py_modules=["EDR_read","states","STO_tests_V2_nanopb_pb2",],

)