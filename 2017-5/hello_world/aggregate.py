from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. 创建 workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")

# 2. 获得 browser
browser = workspace.browser("irbd_balance")



# 3. 运用 aggregates
result = browser.aggregate()

# print("Total\n"
#       "----------------------")
#
# print("Record count : %8d" % result.summary["record_count"])
# print("Total amount : %8d" % result.summary["amount_sum"])
# print("Double amount: %8d" % result.summary["double_amount_sum"])

#
# 4. Drill-down through a dimension
#


# print("\n"
#       "Drill Down by Category (top-level Item hierarchy)\n"                        #表的标题
#       "==================================================")
# #
#
# result = browser.aggregate(drilldown=["item"])          #表的操作[操作的对象]
# print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))   #表头的格式
#
# #
# for row in result.table_rows("item"):
#     print("%-20s%10d%10d%10d" % ( row.label,                                            #表内容的格式
#                               row.record["record_count"],
#                               row.record["amount_sum"],
#                               row.record["double_amount_sum"])
#                               )

print("\n"
      "Slice where Category = Equity\n"                                                  #表头的格式
      "==================================================")

# cut = PointCut("item", ["e"])                           #cut 操作：某个维度的一部分
cut = PointCut("date",  [2008], [2013, 12, 24])
cell = Cell(browser.cube, cuts = [cut])                  #形成cell

# result = browser.aggregate(cell, drilldown=["item"])    #表的操作[操作参数]
result = browser.aggregate(cell, drilldown=["year"])

# print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))
#
# for row in result.table_rows("item"):
#     print("%-20s%10d%10d%10d" % ( row.label,
#                               row.record["record_count"],
#                               row.record["amount_sum"],
#                               row.record["double_amount_sum"],
#                               ))
