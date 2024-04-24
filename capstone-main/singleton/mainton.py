from singleton_logger import SingletonLogger

def main():
    SingletonLogger1 =SingletonLogger.get_instance()
    SingletonLogger2 =SingletonLogger.get_instance()
    
    if SingletonLogger1 is SingletonLogger2:
        print("instance sama, singleton berhasil")
        
    SingletonLogger2.log("this is logged using a singleton logging system")
    
if __name__ == "__main__":
    main()
    