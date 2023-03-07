import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
# print(melbourne_data.describe())
# print columns of data
# print(melbourne_data.columns)


# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom',
                      'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
# print(X.describe())
# print(X.head())


# Define model. Specify a number for random_state to ensure same results each run
# melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
# melbourne_model.fit(X, y)
# print("The predictions are")
# print(melbourne_model.predict(X.head()))
# predicted_home_prices = melbourne_model.predict(X)
# print(mean_absolute_error(y, predicted_home_prices))


# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)
# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
# print(mean_absolute_error(val_y, val_predictions))


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(
        max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)
# for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %
#           (max_leaf_nodes, my_mae))


forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
