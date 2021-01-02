import robin_stocks as rs
import yaml

with open(r'credentials.yaml') as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)

rs.login(username=config['username'], password=config['password'], expiresIn=86400, by_sms=True)

print("Authenticated with Robinhood")
