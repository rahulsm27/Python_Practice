#!/usr/bin/env python
# coding: utf-8

# In[22]:


class sqlops:
    
  
    
    
    
    from Custom_Logger import logger
    mylogger = logger()
    log = mylogger.log('sqlops.log')
    
    def __init__(self):
        import sqlite3
        self.db = sqlite3.connect("task.db")
        self.c = self.db.cursor()
    
    def createtable(self, table):
        try:
            self.log.info(f"Creating table {table}")
            self.c.execute(f"create table if not exists {table}(name text)")
            
        except Exception as e:
            self.log.error(f"error in creating table {e}")
            
    def insertrecord(self, table, data_list):
        try:
            self.log.info("Inserting data")
            
            for i in data_list:
                query = "('" + i[0]+"')"
                self.c.execute(f"insert into {table} values {query}")
                print (query)
                
            self.c.execute("commit")
                
            
            
        except Exception as e:
            self.log.error(f"error in inserting data table {e} insert into {table} values {query}")
            
    def fetchdata(self, table):
        try:
            self.log.info("fetching data")
            
            
                
            return  self.c.execute(f"select * from {table}")
                
            
            
        except Exception as e:
            self.log.error(f"error in fetching data table {e}")
    


# In[23]:


#sql = sqlops()


# In[24]:


#sql.createtable('test')


# In[25]:


#sql.insertrecord('test',[('aaa',1)])


# In[26]:


#data = sql.fetchdata('test')


# In[27]:


#data.fetchall()


# In[ ]:




