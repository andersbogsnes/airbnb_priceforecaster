from ml_tooling import Model
from sklearn.ensemble import RandomForestRegressor
from airbnb_priceforecaster.features import features


def build_model():
    estimator = RandomForestRegressor(n_jobs=-1, max_depth=3)
    return Model(estimator, feature_pipeline=features)
