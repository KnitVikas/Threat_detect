import logging
from typing import Dict, List, Optional
from pydantic import BaseModel
import pandas as pd

import pickle

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
with open("encoders.pkl", "rb") as f:
    label_encoders, scaler = pickle.load(f)

# Get feature names and categorical features
    train_feature_names = scaler.feature_names_in_
    categorical_features = list(label_encoders.keys()) if label_encoders else []
    print("categorical_features", categorical_features )
    
    logger.info(f"Loaded categorical features: {categorical_features}")
    logger.info(f"All feature names: {train_feature_names}")