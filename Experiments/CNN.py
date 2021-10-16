import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from keras.preprocessing.text import Tokenizer
from keras import Sequential
import sys
import pandas as pd
import numpy as np
import warnings
import copy
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

