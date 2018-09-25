#encoding:utf-8

from bs4 import BeautifulSoup

#-------------------------------------------------------
soup = BeautifulSoup(open("index.html"))

"'文档被转换成Unicode；" \
"HTML的实例也都被转换成Unicode编码。'"
#BeautifulSoup("Sacr&eacute; bleu!")
# <html><head></head><body>Sacré bleu!</body></html>

soup = BeautifulSoup("<html>data</html>")

#---------------------------------------------