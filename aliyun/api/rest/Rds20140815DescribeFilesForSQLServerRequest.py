'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeFilesForSQLServerRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.EndTime = None
		self.PageNumber = None
		self.PageSize = None
		self.StartTime = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeFilesForSQLServer.2014-08-15'
