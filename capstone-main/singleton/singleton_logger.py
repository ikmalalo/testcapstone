class SingletonLogger:
    _instance = None
    
    def __init__(self):
        raise RuntimeError("This is a Singleton, invoke get_instance() instead")
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def log(self, ex: Exception):
        print(ex)
        
    def log(self, message: str):
        print(message)
        