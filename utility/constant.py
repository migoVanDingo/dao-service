class Constant:
    @staticmethod
    def get_service_prefix(service_id: str) -> str:
        prefixes = {
            "datastore-management-service": "DSMS",
            
        }
        return prefixes[service_id]
    
    @staticmethod
    def get_service_id(service_prefix: str) -> str:
        services = {
            "datastore-management-service": "datastore_id"
            
        }
        return services[service_prefix]