class Constant:
    @staticmethod
    def get_table_prefix(table: str) -> str:
        prefixes = {
            "datastore": "DSTR",
            "dataset": "DSET",
            "files": "FILE"
            
        }
        return prefixes[table]
    
    @staticmethod
    def get_table_id(table: str) -> str:
        tables = {
            "datastore": "datastore_id",
            "dataset": "dataset_id",
            "files": "file_id"
            
        }
        return tables[table]