class Constant:
    @staticmethod
    def get_table_prefix(table: str) -> str:
        prefixes = {
            "datastore": "DSTR",
            "dataset": "DSET",
            "files": "FILE",
            "project": "PROJ",
            "project_git_info": "PGIT",
            "user": "USER",
            
        }
        return prefixes[table]
    
    @staticmethod
    def get_table_id(table: str) -> str:
        tables = {
            "datastore": "datastore_id",
            "dataset": "dataset_id",
            "files": "file_id",
            "project": "project_id",
            "project_git_info": "project_git_info_id",
            "user": "user_id",
            
        }
        return tables[table]