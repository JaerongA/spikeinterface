import unittest
import pytest

from spikeinterface.core.tests.testing_tools import generate_recording

from spikeinterface.toolkit.preprocessing import filter, bandpass_filter,notch_filter



def test_filter():
    rec = generate_recording()
    
    rec2 = bandpass_filter(rec,  freq_min=300., freq_max=6000.)
    
    # compute by chunk
    rec2.save(chunk_size=100000,verbose=False, progress_bar=True)
    # compute by chunkf with joblib
    rec2.save( total_memory="10k", n_jobs=4, verbose=True)
    # compute once
    rec2.save(verbose=False)
    
    # other filtering types
    rec3 = filter(rec,  band=[40., 60.], btype='bandstop')
    rec4 = filter(rec,  band=500., btype='highpass', filter_mode='ba', filter_order=2)
    
    
    rec5 = notch_filter(rec, freq=3000, q=30, margin=0.005)
    
    # import matplotlib.pyplot as plt
    # from spikeinterface.widgets import plot_timeseries
    # plot_timeseries(rec, segment_index=0)
    # plot_timeseries(rec2, segment_index=0)
    # plot_timeseries(rec3, segment_index=0)
    # plot_timeseries(rec4, segment_index=0)
    # plt.show()


if __name__ == '__main__':
    test_filter()
