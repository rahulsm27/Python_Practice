#!/usr/bin/env python
# coding: utf-8

# In[9]:



class solutions:
    
    from Custom_Logger import logger
    mylogger = logger()
    log = mylogger.log()
    

    def returnwordtuple(self, filename):
        try:
            file = open(filename,'r')
            dict1 = {}
            self.log.info("Reading file data")
            for line in file.readlines():
                if line in dict1:
                    dict1[line] = dict1[line]+1
                else:
                    dict1[line[:-1]] = 1
        except Exception as e:
            self.log.error(f"Error in reading file data {e}")
          #  print("errror",e)
            
            

        final_list = [(k,v) for k,v in dict1.items()]

        return final_list
    
    def reducewords(self,data_list):
        try :
            from functools import reduce

            temp = [{}]
            temp.extend(data_list)

            self.log.info("Reducing file content")
            def finda(a,b):
                if b[0][0]  in a:
                    a[b[0][0]] += 1
                else:
                    a[b[0][0]] = 1
                return a
            return(reduce(finda,temp))
        
        except Exception as e:
            self.log.error (f"Error occured in reduing {e}")
        
        
    
    def filterwords(self, filename):
        try :
            import regex as re
            f = open(filename,'r')
            finallist = []
            pattern = '[A-za-z]+'
            self.log.info("Filtering file contents")
            for lines in f.readlines():
                word = lines[:-1] # removing \n
                word = re.findall(pattern,word)
                if word :
                    finallist.extend(word)
        except Exception as e:
             self.log.error (f"Erro occured in filtering words {e}")
            
        return finallist


# In[ ]:





# In[10]:


#s = solutions()


# In[11]:


#s.filterwords('vocab.pubmed.txt')


# In[12]:


#s.returnwordtuple('vocab.pubmeadfd.txt')


# In[ ]:





# In[ ]:




