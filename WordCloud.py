from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hive_service import ThriftHive
# Required packages for WordCloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from wordcloud import WordCloud, STOPWORDS

def HiveConnector(subReddit , ip, port = 10000):
	transport = TSocket.TSocket(ip,port)
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = ThriftHive.Client(protocol)
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = ThriftHive.Client(protocol)
	transport.open()
	SQL_stm = "SELECT get_json_object(RC_table.json, '$.body') "
	SQL_stm = SQL_stm + "FROM RC_table "
	SQL_stm = SQL_stm + "WHERE get_json_object(RC_table.json, '$.subreddit') = '" +
	subReddit +"'"
	client.execute(SQL_stm)
	Output = client.fetchAll()
	transport.close()
return Output