# # -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import cubes
from cubes.compat import ConfigParser
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
configg = ConfigParser()
print configg
print type(configg)
configg.read('slicer.ini')

workspace = Workspace(config=configg)
browser = workspace.browser("irbd_balance")
result = browser.aggregate()
result.summary["record_count"]
