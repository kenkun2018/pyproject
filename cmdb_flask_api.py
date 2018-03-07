# encoding: utf-8
import os,sys
import mysql.connector
from flask import Flask,request,jsonify
from pprint import pprint
from analyze_config import dbconfig


app = Flask(__name__)


@app.route('/query/<targettype>' , methods=['GET'])
def hello_world(targettype):
	qkey = request.args
	print (qkey.to_dict())
	dbquery = Dbquery()
	resdata = dbquery.querydata(targettype , qkey)
	return jsonify(resdata)



class Dbquery():
	def __init__(self):
		self.db = mysql.connector.connect(**dbconfig)
		self.cursor = self.db.cursor()

	def querydata(self , targettype , param):
		allresData = []	
		#查询基础信息
		if targettype == 'baseDetail':
			for key,value in param.items():
				sql = f"SELECT instanceId,business_type from cmdb_base_gather where {key} like '%{value}%';"
			self.cursor.execute(sql)
			rows = self.cursor.fetchall()
			#pprint (rows)
			for row in rows:
				if row[1] == 'nissp':
					selectCol = 'b.instanceName,b.instanceId,b.hostname,b.privateIp,b.internetIp,t.type,t.master_slave,b.status'
				else:
					selectCol = 'b.instanceName,b.instanceId,b.hostname,b.privateIp,b.internetIp,b.business_type,b.status'
				sql = f"SELECT {selectCol} from cmdb_base_gather b,cmdb_{row[1]}_gather t where b.instanceId=t.instanceId and b.instanceId='{row[0]}';"
				print (sql)
				self.cursor.execute(sql)
				rowsdata = self.cursor.fetchall()
				for irow in rowsdata:
					allresData.append(irow)
		#查询项目信息
		elif targettype == 'project':
			for key,value in param.items():
				sql = f"""SELECT 
    b.instanceName,
    b.instanceId,
    b.hostname,
    b.privateIp,
    b.business_type,
    p.titleName,
    p.manager
FROM
    cmdb_base_gather b,
    cmdb_project_gather p
WHERE
    b.instanceId = p.instanceId
        AND p.{key} like '%{value}%';"""
			self.cursor.execute(sql)
			rows = self.cursor.fetchall()
			for row in rows:
				allresData.append(row)

		pprint (allresData)

		return allresData
		

	def __del__(self):
		self.db.close()


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0' , port=5555)