import pytest
import polars as pl
from maplib import Mapping
import pathlib
import os

REPO_PATH = pathlib.Path(__file__).parent.parent.resolve()

SHAPE_GRAPH = "urn:digdir:shapes"

def test_validate_example():
    if "GITHUB_STEP_SUMMARY" in os.environ :
        f = open(os.environ["GITHUB_STEP_SUMMARY"], "a")
    else:
        f = None
    m = Mapping()
    m.read_triples(str(REPO_PATH / "examples" / "example-dataset.ttl"))
    m.read_triples(str(REPO_PATH / "shacl" / "DCAT-AP-NO-shacl_shapes_2.00.ttl"), graph=SHAPE_GRAPH)
    report = m.validate(shape_graph=SHAPE_GRAPH, include_conforms=False, include_shape_graph=True)
    results_df = report.results()
    if results_df is not None:
        violations_df = results_df.filter(pl.col("result_severity").eq("<http://www.w3.org/ns/shacl#Violation>"))
        if violations_df.height > 0:
            print("\n__Example file validation failures:__ {}\n".format(violations_df.height), file=f)
            print(violations_df.to_pandas().to_markdown(index=False), file=f)
            assert violations_df.height == 0
