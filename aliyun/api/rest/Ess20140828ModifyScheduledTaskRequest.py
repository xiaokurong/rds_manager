'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ess20140828ModifyScheduledTaskRequest(RestApi):
	def __init__(self,domain='ess.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Description = None
		self.LaunchExpirationTime = None
		self.LaunchTime = None
		self.RecurrenceEndTime = None
		self.RecurrenceType = None
		self.RecurrenceValue = None
		self.ScheduledAction = None
		self.ScheduledTaskId = None
		self.ScheduledTaskName = None
		self.TaskEnabled = None

	def getapiname(self):
		return 'ess.aliyuncs.com.ModifyScheduledTask.2014-08-28'
