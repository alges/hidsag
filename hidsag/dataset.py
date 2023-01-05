import os
import json
from glob import glob

from .utils import *
from .sample import *

def set_dataset(dataset):
    global CURRENT_DATASET
    CURRENT_DATASET = dataset
    return dataset
    
def get_dataset():
    global CURRENT_DATASET
    return CURRENT_DATASET
    
def get_wavelength():
    global DATASET_PATH 
    wavelength_path = os.path.join(DATASET_PATH, "wavelengths.json")
    
    try:
        with open(wavelength_path) as wavelength_file:
            wvmetadata = json.load(wavelength_file)
    except IOError:
        print("Wavelength metadata file does not exist ({})".format(wavelength_path))

    return json2obj(wvmetadata)
        
    
def list_samples(dataset_path="./data"):
    global CURRENT_DATASET
    global DATASET_PATH 
    DATASET_PATH = os.path.join(dataset_path, f"{CURRENT_DATASET}")
    samples_dirs = sorted(glob(os.path.join(dataset_path, f"{CURRENT_DATASET}/*/"), 
                          recursive = True))
    samples_names = [] 
    for dirname in samples_dirs:
        samples_names.append(os.path.basename(os.path.dirname(dirname)))
    return samples_names
    
def get_json_sample(sample_name):
     global DATASET_PATH
     metadata_path = os.path.join(DATASET_PATH, sample_name, "metadata.json")

     try:
         with open(metadata_path) as metadata_file:
             metadata = json.load(metadata_file)
     except IOError:
         print("Metadata file does not exist ({})".format(metadata_path))

     return json2obj(metadata)

def get_sample(sample_name):
     global DATASET_PATH
     metadata_path = os.path.join(DATASET_PATH, sample_name, "metadata.json")

     try:
         with open(metadata_path) as metadata_file:
             metadata = json.load(metadata_file)
     except IOError:
         print("Metadata file does not exist ({})".format(metadata_path))

     sample = HIDSAGSample(metadata, DATASET_PATH)
     return sample

def get_samples_list(dataset_path="./data"):
    global CURRENT_DATASET
    global DATASET_PATH 
    DATASET_PATH = os.path.join(dataset_path, f"{CURRENT_DATASET}")
    samples_dirs = sorted(glob(os.path.join(dataset_path, f"{CURRENT_DATASET}/*/"), 
                          recursive = True))
    samples_names = [] 
    for dirname in samples_dirs:
        samples_names.append(os.path.basename(os.path.dirname(dirname)))
        
    samples_crops_list = []
    
    for sample_name in samples_names:
        sample = get_json_sample(sample_name)
        for crop in range(1, len(sample.crops)+1):
            samples_crops_list.append({'sample_id': sample_name, **sample.vars, 'CROP': crop, 'tags': ",".join(sample.crops[crop-1]['tags']), 'kind': 'swir_low', **{f'image_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['swir_low']['image_dims'].items()}, **{f'real_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['swir_low']['real_dims'].items()}})
            samples_crops_list.append({'sample_id': sample_name, **sample.vars, 'CROP': crop, 'tags': ",".join(sample.crops[crop-1]['tags']), 'kind': 'vnir_low', **{f'image_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['vnir_low']['image_dims'].items()}, **{f'real_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['vnir_low']['real_dims'].items()}})
            samples_crops_list.append({'sample_id': sample_name, **sample.vars, 'CROP': crop, 'tags': ",".join(sample.crops[crop-1]['tags']), 'kind': 'vnir_high', **{f'image_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['vnir_high']['image_dims'].items()}, **{f'real_dims@{k}': v for k, v in sample.crops[crop-1][str(crop).zfill(2)]['vnir_high']['real_dims'].items()}})
    
    return samples_crops_list