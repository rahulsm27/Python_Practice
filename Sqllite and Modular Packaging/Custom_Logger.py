#!/usr/bin/env python
# coding: utf-8

# In[9]:


import logging 


# In[10]:


class logger:
    
    def __init__(self):
        pass
   
    
    def log(self,filename = 'application.log', level = logging.DEBUG):
        
        logger = logging.getLogger()
        logger.setLevel(level)
        
        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(filename,mode = 'w+')

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        
        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
        return logger
        
  


# In[ ]:


#mylogger = logger()
#logging_data = mylogger.log("sqllite.log",logging.DEBUG)
#logging_data.info("asdfa This is info asdfa")

