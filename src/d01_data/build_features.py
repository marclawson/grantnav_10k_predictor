# -*- coding: utf-8 -*-

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline, make_pipeline, make_union, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureExtractorText(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, *args):
        return self

    def transform(self, X, *args):
        X = X[self.columns].values
        return X

    
class FeatureExtractorOHE(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, *args):
        return self

    def transform(self, X, *args):
        X = X[self.columns].values.reshape(-1, 1)
        return X
              
              
class FeatureExtractorNumber(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, *args):
        return self

    def transform(self, X, *args):
        X = X[self.columns].values.reshape(-1,1)
        return X

    
class CustomImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, *args):
        return self

    def transform(self, X, *args):
        X = SimpleImputer(missing_values=np.NaN,
                          strategy='constant',
                          fill_value=0).fit_transform(X)
        return X