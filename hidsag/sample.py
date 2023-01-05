import os
import json
import h5py
import pandas as pd

from .utils import *


class HIDSAGSample(object):
    def __init__(self, metadata, dataset_path=None):
        self.data = pd.DataFrame()
        self.metadata = metadata
        self.dataset_path = dataset_path

    def __repr__(self):
        return self.metadata['sample_name']

    def __len__(self):
        """
        Return datafile length as number of rows
        :return: Int. Datafile length
        """
        return len(self.data)

    def __iter__(self):
        """
        Return list of variables
        :return: Array-like. List of variables
        """
        return iter(list(self.data))
    
    def get_variables(self):
        """
        Return the variables of the sample as a dictionary
        :return: Dictionary-like. Dictionary with the list of variables
        """
        return self.metadata['vars']

    def list_crops(self):
        crop_list = []
        for crop in range(len(self.metadata['crops'])):
            for dkey in self.metadata['crops'][crop].keys():
                if dkey != "tags":
                    crop_list.append(dkey)
        
        return crop_list
    
    def get_metadata(self, crop, hsi_image):
        return self.metadata['crops'][self.list_crops().index(crop)][crop][hsi_image]
        
    def get_data(self, crop, hsi_image):
        global DATASET_PATH
        path_hsi = self.metadata['crops'][self.list_crops().index(crop)][crop][hsi_image]['path_hsi']
        hsi_full_path = os.path.join(self.dataset_path, self.metadata['sample_name'], path_hsi)
        sample_hsi_file = h5py.File(hsi_full_path, 'r')
        sample_hsi_data = sample_hsi_file['/hsi_data']
        return sample_hsi_data