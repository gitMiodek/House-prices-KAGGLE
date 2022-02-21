#ML models used in house pricing project

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor

r_forest = RandomForestRegressor(n_estimators=600, random_state=42)
xgb = XGBRegressor()
ridge = Ridge(alpha = 10,tol = 1e-15)
svr = SVR(kernel='rbf',C = 20000,epsilon = 0.001)
gbr = GradientBoostingRegressor(n_estimators=2000,learning_rate=0.01,max_depth=5)