#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import dateparser

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    dateparser.parse(fdp.ConsumeUnicodeNoSurrogates(64))
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()