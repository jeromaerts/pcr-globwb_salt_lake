#!/usr/bin/env python
# coding: utf-8

# # Model Run PCR-GLOBWB Great Salt Lake using eWaterCycle
# 
# ### contact: j.p.m.aerts@tudelft.nl

# In[1]:


import ewatercycle.forcing
import ewatercycle.models
import ewatercycle.parameter_sets

from pathlib import Path

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# ## Set Paths

# In[2]:


ROOT = Path('/home/jaerts/banafsheh/salt_lake_pcr-globwb/')
MODELDATA = Path('/gpfs/work1/0/wtrcycle/users/jaerts/pcrglobwb2_input/')


# ## Set Config

# In[3]:


ewatercycle.CFG.load_from_file(f'{ROOT}/ewatercycle_salt_lake.yml')


# # Load Parameter Set

# In[4]:


salt_lake = ewatercycle.parameter_sets.ParameterSet(
    name="pcr-globwb_salt_lake",
    directory=f"{MODELDATA}/",
    config=f"{ROOT}/salt_lake_05min.ini",
    target_model="pcrglobwb",
    supported_model_versions={"setters"},
)


# # Load Forcing Data

# In[5]:


forcing = ewatercycle.forcing.load_foreign(
    target_model="pcrglobwb",
    start_time="2001-01-01T00:00:00Z",
    end_time="2017-12-31T00:00:00Z",
    directory=f"{ROOT}/",
    shape=None,  # if available, it can be used e.g. for plotting
    forcing_info=dict(
        # model-specific options
        precipitationNC="pcrglobwb_OBS6_ERA5_reanaly_1_day_pr_2002-2017_salt_lake.nc",
        temperatureNC="pcrglobwb_OBS6_ERA5_reanaly_1_day_tas_2002-2017_salt_lake.nc",
    ),
)
print(forcing)


# # Model Setup

# In[6]:


pcrglob = ewatercycle.models.PCRGlobWB(
    version="setters", parameter_set=salt_lake, forcing=forcing
)
print(pcrglob)


# In[7]:


cfg_file, cfg_dir = pcrglob.setup(
    max_spinups_in_years=30,
    start_time='2002-01-01T00:00:00Z',
    end_time='2017-12-31T00:00:00Z'
)
cfg_file, cfg_dir


# In[8]:


pcrglob.parameters


# In[9]:


pcrglob.initialize(cfg_file)


# # Model Run

# In[ ]:


while pcrglob.time < pcrglob.end_time:
    print(pcrglob.time_as_isostr, end="\r")
    pcrglob.update()
    
print('Model Run finished!')


# In[ ]:


pcrglob.finalize()


# In[ ]:




