class Constant:
    @staticmethod
    def get_table_prefix(table: str) -> str:
        prefixes = {
            "datastore": "DSTR",
            "dataset": "DSET"
            
        }
        return prefixes[table]
    
    @staticmethod
    def get_table_id(table: str) -> str:
        tables = {
            "datastore": "datastore_id",
            "dataset": "dataset_id"
            
        }
        return tables[table]