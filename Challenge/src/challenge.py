# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import numpy as np 
import matplotlib.pyplot as plt
import pylab
import gwpy
import gwosc
import pycbc
from pycbc.filter import resample_to_delta_t, highpass
from pycbc.catalog import Merger
from pycbc.psd import interpolate, inverse_spectrum_truncation
from pycbc.frame import read_frame
from gwosc.datasets import event_gps
from gwpy.timeseries import TimeSeries
import matplotlib.colors as mplc


# %%
src_dir=os.getcwd()
main_dir=os.path.dirname(src_dir)
data_dir=os.path.join(main_dir,"data")

# %% [markdown]
# # CHALLENGE 1
# ### 1. Load the data into memory.  What are the sampling rate and duration of the data?

# %%
gwf_1 = read_frame(os.path.join(data_dir,"challenge1.gwf"), "H1:CHALLENGE1")
gwpy_1=TimeSeries.from_pycbc(gwf_1)


# %%
print(f"The duration is {gwf_1.duration}s and the sample rate is {gwf_1.sample_rate}Hz")

# %% [markdown]
# ### 2. Plot the data in the time-domain.

# %%
#plot of the signal
#plt.plot(gwf_1.sample_times,gwf_1)
gwpy_1.plot()
print("")

# %% [markdown]
# ### 3. Plot a spectrogram (or q-transform) of the data, and try to identify the signal.
# 

# %%
qt_gwf_1=gwf_1.qtransform(frange=(20,500), qrange=(20, 30))
#qt=qt_gwf_1[2][:][::-1]


# %%
""" plt.figure(figsize=(10,10))
qt=qt_gwf_1[2][:][:]
plt.imshow(qt,aspect="auto",extent=(qt_gwf_1[0][0],qt_gwf_1[0][-1],qt_gwf_1[1][0],qt_gwf_1[1][-1]))
plt.colorbar()
plt.yscale("log")
plt.xlim(-15,15)
plt.title("QTranform")
plt.xlabel("Time [s]")
plt.ylabel("F [Hz]")

 """
# %%



# %%

#qtr=gwpy_1.q_transform(frange=(20,500), qrange=(20, 30))


# %%
#plt.pcolormesh([qt_gwf_1[0],qt_gwf_1[1],] qt_gwf_1[2])


# %%



# %%



# %%



