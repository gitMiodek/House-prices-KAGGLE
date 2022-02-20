from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
r_forest = RandomForestRegressor(n_estimators=600, random_state=42)
xgb = XGBRegressor()
from sklearn.linear_model import Ridge
ridge = Ridge()