# # -*- coding: utf-8 -*-

# # -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import cubes
import configparser
config = configparser.ConfigParser()
from cubes.tutorial.sql import create_table_from_csv
engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine,
                    "C:\\Users\\Administrator\\Desktop\\IBRD_Balance_Sheet__FY2010.csv",
                     table_name="irbd_balance",
                       fields=[
                             ("category", "string"),
                             ("category_label", "string"),
                             ("subcategory", "string"),
                             ("subcategory_label", "string"),
                             ("line_item", "string"),
                             ("year", "integer"),
                            ("amount", "integer")],
                       create_id=True
                 )
from cubes import Workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("tutorial_model.json")
browser = workspace.browser("irbd_balance")
result = browser.aggregate()

result.summary["record_count"]
print(result.summary)
result.summary["amount_sum"]
print(result.summary)

result = browser.aggregate(cuts=["a"])
for record in result:
     print (record)

result = browser.aggregate(cuts=["item"])
for record in result:
     print (record)


# cuts = [
#     PointCut("geography", ["sk"]),
#     PointCut("date", [2010, 6], [2012, 6])
# ]
