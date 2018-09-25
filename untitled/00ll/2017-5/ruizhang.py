# # -*- coding: utf-8 -*-
import py2neo
from pymongo import MongoClient
db = MongoClient("mongodb://localhost:27017")
col = db.zhiwang['paper']
#从Mongodb中删选出需要的数据
papers = col.find({"authors":{"$elemMatch":{"author_name":"汤庸","author_orgn_name":"华南师范大学"}}})
paper_list = []
for paper in papers:
    paper_list.append(paper)

from py2neo import Graph,Node,Relationship
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="asdasd"
)

#创建实体
class School(GraphObject):
    __primarykey__ = "name"
    name = Property()
    #创建关系
    teachers = RelatedFrom("Person","teached_in")

class Person(GraphObject):
    __primarykey__ = "name"

    name = Property()
    domain = Property()

    published = RelatedTo(Paper)
    teached_in = RelatedTo(School)

class Paper(GraphObject):
    __primarykey__ = "title"

    title = Property()
    pub_date = Property()
    journal = Property()
    download_num = Property()
    quote_num = Property()

    authors = RelatedFrom("Person", "published")

for paper in paper_list:
    one_paper = Paper()
    one_paper.title = paper['title']
    one_paper.pub_date = paper['pub_date']
    one_paper.journal = paper['journal']
    one_paper.download_num = paper['download_num']
    one_paper.quote_num = paper['quote_num']
    for author in paper['authors']:
        one_person = Person.select(graph, author['author_name']).first()
        if one_person:
            one_person.published.add(one_paper,properties={'time':one_paper.pub_date})
            graph.push(one_person)
        else:
            one_author = Person()
            one_school = School()
            one_school.name = author['author_orgn_name']
            one_author.name = author['author_name']
            one_author.code = ",".join(author['author_domain'])
            one_author.teached_in.add(one_school)
            one_author.published.add(one_paper,properties={'time':one_paper.pub_date})
            graph.push(one_author)