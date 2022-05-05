#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nest_asyncio
nest_asyncio.apply()

import twint

def extract_data(topic, namefile):
    #configuration
    config = twint.Config()
    config.Search = topic
    config.Lang = "en"
    config.Limit = 1000
    config.Since = "2022-02-28"
    #config.Until = "2022-03-11"
    config.Store_csv = True       # store tweets in a csv file
    config.Output = "./data/"+namefile+".csv"
    #running search
    twint.run.Search(config)


# In[ ]:


extract_data('Ukraine', 'Ukraine')
extract_data('Russia', 'Russia')
extract_data('petrol russia Ukraine','petrol' )
extract_data('gaz russia Ukraine', 'gaz')


# In[ ]:




