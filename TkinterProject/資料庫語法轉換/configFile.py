def GetInitConfig():
    import configparser

    Info =['','','','']
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')

        Info[0] = config['Server1']['ip']
        Info[1] = config['Server1']['name']

        Info[2] = config['Server1']['user']
        Info[3] = config['Server1']['pwd']
    except Exception as configError:
        raise(configError)

    return Info