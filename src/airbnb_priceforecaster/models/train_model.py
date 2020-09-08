from airbnb_priceforecaster.data import AirBnBDataset
from airbnb_priceforecaster.features import features
from ml_tooling import Model
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from airbnb_priceforecaster import VISUALIZATIONS


def train_model(year, month, day, graphs=True, clf=RandomForestRegressor()):
    dataset = AirBnBDataset(year=year, month=month, day=day)
    dataset.create_train_test()

    model = Model(clf, feature_pipeline=features)
    result = model.score_estimator(dataset)
    model.config.N_JOBS = 6
    with model.log("randomforest"):
        model.save_estimator()

    if graphs:
        result.plot.feature_importance()
        plt.savefig(VISUALIZATIONS / "confusion_matrix.png")

        result.plot.residuals()
        plt.savefig(VISUALIZATIONS / "residuals.png")

        result.plot.prediction_error()
        plt.savefig(VISUALIZATIONS / "prediction_error.png")

    return result
