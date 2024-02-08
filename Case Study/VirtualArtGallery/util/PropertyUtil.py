class PropertyUtil:
    @staticmethod
    def getPropertyString():
        with open("../database_properties.txt", "r") as file:
            properties = {}
            for line in file:
                key, value = line.strip().split("=")
                properties[key.strip()] = value.strip()
        return properties


"""print(PropertyUtil.getPropertyString())"""
