
# # -*- coding: utf-8 -*-
import py2neo
from py2neo import Graph,Node,Relationship
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="neo4j"
)



# test_graph = Graph(
#     "http://localhost:7474",
#     # username="neo4j",
#     # password="neo4j"
# )


