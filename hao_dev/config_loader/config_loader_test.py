from config_loader import MYSQL_CFG, INFLUX_DB_CFG, NOTIFY_CFG

if __name__ == '__main__':
    print(MYSQL_CFG)
    print(INFLUX_DB_CFG)
    print(NOTIFY_CFG)

    extra_info2 = NOTIFY_CFG['EXTRA_INFO2']
    print(extra_info2)
    print("------------------")
    print("extra_info2[\"1\"]:" + extra_info2["1"])
    temp = 1
    temp = str(temp)
    print("extra_info2[1]:" + extra_info2[temp])


