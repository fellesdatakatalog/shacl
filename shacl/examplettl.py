from datacatalogtordf import Catalog, Dataset


def datasetrdf():
    """Unfinished example of how to build a dataset with python"""
    # Create catalog object
    catalog = Catalog()
    catalog.identifier = "http://example.com/catalogs/1"
    catalog.title = {"en": "A dataset catalog"}
    catalog.publisher = "https://example.com/publishers/1"

    # Create a dataset:
    dataset = Dataset()
    dataset.identifier = "http://example.com/datasets/1"
    dataset.title = {"nb": "inntektsAPI", "en": "incomeAPI"}
    #
    # Add dataset to catalog:
    catalog.datasets.append(dataset)

    # get rdf representation in turtle (default)
    rdf = catalog.to_rdf(format="turtle")
    return rdf
    # print(rdf.decode())
