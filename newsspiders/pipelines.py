# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='penghy',
        charset='utf8',
        use_unicode=False
    )
    return conn
class NewsspidersPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into sunck.news(标题,正文) values (%s,%s)'
        try:
            cursor.execute(sql, (item['tags'], item['content']))
            dbObject.commit()
        except :
            dbObject.rollback()
        return item
