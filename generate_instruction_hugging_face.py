"""
Read data from the dataset and generate the instruction for hugging face
"""

import os
import json
import tqdm
import logging
import argparse
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

# Read the squad_dataset.jsonl



