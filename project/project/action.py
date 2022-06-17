from conDB import Con

c = Con

class Action:
    def addHW(name, hw_name):
        ID = c.addHW(name, hw_name)
        data = c.getHWByID(ID)
        return data
    
    def DeleteHW(ID):
        boolean = c.DeleteHW(ID)
        if boolean:
            data = {"error": False, "Delete": "Succeses"}
        else:
            data = {"error": True}
        return data
    
    def getHWByID(ID):
        data = c.getHWByID(ID)
        return data
    
    def updateStatusHW(ID, status):
        boolean = c.updateStatusHW(ID, status)
        if boolean:
            data = c.getHWByID(ID)
        else:
            data = {"error": True}
        return data
    
    def updateValueHW(ID, value):
        boolean = c.updateValueHW(ID, value)
        if boolean:
            data = c.getHWByID(ID)
        else:
            data = {"error": True}
        return data
    
    def getAllHW():
        data = c.getAllHW()
        return data
    
    def getValueHWByID(ID):
        data = c.getValueHWByID(ID)
        return data
    
    def getStatusHWByID(ID):
        data = c.getStatusHWByID(ID)
        return data
    
    def updateStatusValueHW(ID, status, value):
        boolean = c.updateStatusValueHW(ID, status, value)
        if boolean:
            data = c.getHWByID(ID)
        else:
            data = {"error": True}
        return data
    
    def getAutoHWByID(ID):
        data = c.getAutoHWByID(ID)
        return data
    
    def updateAutoHW(ID, auto):
        boolean = c.updateAutoHW(ID, auto)
        if boolean:
            data = c.getHWByID(ID)
        else:
            data = {"error": True}
        return data