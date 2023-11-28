# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/PaulAndree/Curso2023-2024-ODKG/blob/assigments123/Assignment4/course_materials/notebooks/Task08.ipynb

**Task 08: Completing missing data**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

from rdflib.namespace import RDF
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://data.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

#List all elements from g1
for s, p, o in g1.triples((None, None, None)):
  print(s, p)

#Extract the properties, FN, Given, Email from g2 and add them in g1

q = prepareQuery("""select ?s ?p ?o where
{
  ?s ?p ?o.
  filter(?p=vcard:FN || ?p=vcard:Given || ?p=vcard:EMAIL)

}""", initNs={"vcard": vcard})

for new in g2.query(q):
    g1.add(new)

#List the final triples with data updated
for s, p, o in g1:
    print(s, p, o)