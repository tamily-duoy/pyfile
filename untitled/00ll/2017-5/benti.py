#!/usr/bin/env python
# -*- coding: utf-8 -*-
# curl http://localhost:7474/db/data/
# {
#  "extensions" : {
#  },
#  "node" : "http://localhost:7474/db/data/node",
#  "node_index" : "http://localhost:7474/db/data/index/node",
#  "relationship_index" : "http://localhost:7474/db/data/index/relationship",
#  "extensions_info" : "http://localhost:7474/db/data/ext",
#  "relationship_types" : "http://localhost:7474/db/data/relationship/types",
#  "batch" : "http://localhost:7474/db/data/batch",
#  "cypher" : "http://localhost:7474/db/data/cypher",
#  "transaction" : "http://localhost:7474/db/data/transaction",
#  "neo4j_version" : "2.0.0-M03"
# }



from __future__ import print_function
 
import sys
from py2neo import neo4j, Node, Relationship


graph_db = neo4j.GraphDatabaseService()
 
class Person(object):
   
  _root = graph_db.get_or_create_indexed_node("reference",
     "contacts", "root")
   
  @classmethod
  def create(cls, name, *emails):
    person_node, _ = graph_db.create(Node(name=name),
       Relationship(cls._root, "PERSON", 0))
    for email in emails:
      graph_db.create(Node(email=email), Relationship(cls._root, "EMAIL", 0),
         Relationship(person_node, "EMAIL", 0))
    return Person(person_node)
   
  @classmethod
  def get_all(cls):
    return [Person(person.end_node) for person in
       cls._root.match("PERSON")]
   
  def __init__(self, node):
    self._node = node
   
  def __str__(self):
    return self.name + "\n" + "\n".join(" <{0}>"
       .format(email) for email in self.emails)
   
  @property
  def name(self):
    return self._node["name"]
   
  @property
  def emails(self):
    return [rel.end_node["email"] for rel in
       self._node.match("EMAIL")]
 
if __name__ == "__main__":
  if len(sys.argv) < 2:
    app = sys.argv[0]
    print("Usage: {0} add <name> <email> [<email>...]".format(app))
    print("    {0} list".format(app))
    sys.exit()
  method = sys.argv[1]
  if method == "add":
    print(Person.create(*sys.argv[2:]))
  elif method == "list":
    for person in Person.get_all():
      print(person)
  else:
    print("Unknown command")