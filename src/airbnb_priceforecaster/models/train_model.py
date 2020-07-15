from airbnb_priceforecaster.data import AirBnBDataset
from airbnb_priceforecaster.features import get_pipeline
from ml_tooling import Model
from sklearn.ensemble import RandomForestRegressor


def train_model(year, month, day, clf=RandomForestRegressor()):
    dataset = AirBnBDataset(year=year, month=month, day=day)
    dataset.create_train_test()

    clf = get_pipeline(clf)
    model = Model(clf)
    return model.score_estimator(dataset)


if __name__ == '__main__':
    train_model(2020, 5, 30)
