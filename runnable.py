import dataiku
import csv
client = dataiku.api_client()
# This file is the actual code for the Python runnable someidentifier
from dataiku.runnables import Runnable

class MyRunnable(Runnable):
    """The base interface for a Python runnable"""

    def __init__(self, project_key, config, plugin_config):
        """
        :param project_key: the project in which the runnable executes
        :param config: the dict of the configuration of the object
        :param plugin_config: contains the plugin settings
        """
        self.project_key = project_key
        self.config = config
        self.plugin_config = plugin_config
        
    def get_progress_target(self):
        """
        If the runnable will return some progress info, have this function return a tuple of 
        (target, unit) where unit is one of: SIZE, FILES, RECORDS, NONE
        """
        return None

    def run(self, progress_callback):
        """
        Do stuff here. Can return a string or raise an exception.
        The progress_callback is a function expecting 1 value: current progress
        """
        filepath = self.config.get("user_file_location")
        print(filepath)
        with open(filepath) as f:
            usersfile = f.readlines()
            for line in usersfile:
                userdetails = line.split(',')
                username = userdetails[0]
                password = userdetails[1]
                display_name = userdetails[2]
                usergroup = [userdetails[3]]
                if len(userdetails)>4:
                  usergroup.append(userdetails[4])
                new_user = client.create_user(username, password, display_name, source_type='LOCAL', groups=[usergroup])
        prettyprinter.pprint(client.list_users())
        raise Exception("unimplemented")
