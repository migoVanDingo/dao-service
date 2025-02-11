class Constant:
    @staticmethod
    def get_table_prefix(table: str) -> str:
        prefixes = {
            "datastore": "DST",
            "datastore_roles": "DSRO",
            "datastore_config": "DSCF",
            "datastore_files": "DSFI",
            "dataset": "DAT",
            "dataset_roles": "DTRO",
            "dataset_files": "DTFI",
            "files": "FILE",
            "project": "PROJ",
            "project_roles": "PRJRO",
            "project_git_info": "PGIT",
            "user": "USER",
            "user_registration": "USRG",
            "user_roles": "USRO",
            "team": "TEAM",
            "team_roles": "TMRO",
            "jobs": "JOB",
            "job_tasks": "TASK",
            "label_project": "LBLP",
            "user_session": "SESS",

            
        }
        return prefixes[table]
    
    @staticmethod
    def get_table_id(table: str) -> str:
        tables = {
            "datastore": "datastore_id",
            "datastore_roles": "datastore_roles_id",
            "datastore_config": "datastore_config_id",
            "datastore_files": "datastore_files_id",
            "dataset": "dataset_id",
            "dataset_roles": "dataset_roles_id",
            "dataset_files": "dataset_files_id",
            "files": "file_id",
            "project": "project_id",
            "project_roles": "project_roles_id",
            "project_git_info": "project_git_info_id",
            "user": "user_id",
            "user_registration": "user_registration_id",
            "user_roles": "user_role_id",
            "team": "team_id",
            "team_roles": "team_roles_id",
            "jobs": "job_id",
            "job_tasks": "task_id",
            "label_project": "label_project_id",
            "user_session": "session_id",
            
        }
        return tables[table]