class Constant:
    @staticmethod
    def get_table_prefix(table: str) -> str:
        prefixes = {
            "datastore": "DST",
            "datastore_roles": "DSRO",
            "datastore_config": "DSCF",
            "dataset": "DAT",
            "dataset_roles": "DTRO",
            "files": "FILE",
            "project": "PROJ",
            "project_roles": "PJRO",
            "project_git_info": "PGIT",
            "user": "USER",
            "team": "TEAM",
            "team_roles": "TMRO",

            
        }
        return prefixes[table]
    
    @staticmethod
    def get_table_id(table: str) -> str:
        tables = {
            "datastore": "datastore_id",
            "datastore_roles": "datastore_roles_id",
            "datastore_config": "datastore_config_id",
            "dataset": "dataset_id",
            "dataset_roles": "dataset_roles_id",
            "files": "file_id",
            "project": "project_id",
            "project_roles": "project_roles_id",
            "project_git_info": "project_git_info_id",
            "user": "user_id",
            "team": "team_id",
            "team_roles": "team_roles_id",
            
        }
        return tables[table]