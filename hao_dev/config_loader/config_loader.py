import json
import os

# 加载配置文件，并将其存储在全局变量中，供后续业务代码使用
# 读取MYSQL_CFG、INFLUX_DB_CFG、NOTIFY_CFG
config_path = "config-example.json"
if os.path.isfile(config_path):
    try:
        with open(config_path, "r")  as f:
            json_data = json.load(f)

        _g = globals()
        for k, v in json_data.items():
            _g[k] = v

        print("load config success")

    except Exception as e:
        print("load config failed, error: %s" % e)
else:
    print("config file not exist")