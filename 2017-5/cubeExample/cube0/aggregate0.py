# # -*- coding: utf-8 -*-
from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
# workspace.import_model("model.json")
workspace.import_model("G:\\迅雷下载\\cubes-master\\tests\\models\\model.json")

# 2. Get a browser
# browser = workspace.browser("irbd_balance")
#-------------------------------------------------------------------
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
#---------------------------------------------------

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["record_count"])
print("Total amount : %8d" % result.summary["amount_sum"])
print("Double amount: %8d" % result.summary["double_amount_sum"])

#
# 4. Drill-down through a dimension
#

print("\n"
      "Drill Down by Category (top-level Item hierarchy)\n"
      "==================================================")
#
result = browser.aggregate(drilldown=["item"])
#
print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))
#
for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"])
                              )

print("\n"
      "Slice where Category = Equity\n"
      "==================================================")

cut = PointCut("item", ["e"])
cell = Cell(browser.cube, cuts = [cut])

result = browser.aggregate(cell, drilldown=["item"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"],
                              ))
