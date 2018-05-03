from datetime import datetime, timedelta
from pymongo import MongoClient, errors

class MogoQueue():

    OUTSTANDING = 1
    PROCESSING = 2
    COMPLETE = 3

    def __init__(self,db,collection,timeout = 300):
        self.client = MongoClient()
        self.Client = self.client[db]
        self.db = self.Client[collection]
        self.timeout = timeout

    def __bool__(self):
        record = self.bd.find_one(
            {'status' :{'$ne': self.COMPLETE}}
        )

        return True if record else False

    def push(self,url,title):
        try:
            print('正在存入数据库-----------')
            self.db.insert({'_id':url,'status':self.OUTSTANDING,'标题':title,})
        except errors.DuplicateKeyError as e:
            print("数据库以存在")


    def push_show(self,url,title):
        try:
            print('------正在存储下载URL--------')
            self.db.insert({'_id':url,"标题" :title})
        except errors.DuplicateKeyError as e:
            print('数据已存在')


    def pop(self):

        record = self.db.find_and_modify(
            query= {'status': self.OUTSTANDING},
            update = {'$set':{'status':self.PROCESSING}}
        )

        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError

    def pop_title(self,url):
        record = self.db.find_one({'_id':url})
        return record['标题']

    def peek(self):

        record = self.db.find_one({'status': self.OUTSTANDING})
        if record:
            return record['_id']


    def complete(self,url):
        self.db.update({'_id': url}, {'$set': {'status': self.COMPLETE}})

    def repair(self):
        record = self.db.find_and_modify(
            query={
                'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                'status': {'$ne': self.COMPLETE}
            },
            update={'$set': {'status': self.OUTSTANDING}}
        )
        if record:
            print('重置URL状态', record['_id'])

    def clear(self):

        self.db.drop()