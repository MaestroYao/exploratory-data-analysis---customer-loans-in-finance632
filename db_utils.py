
import yaml

class RDSDatabaseConnector:
    
    def load_creds():
        with open('.gitignore/credentials.yml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
