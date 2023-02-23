from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSubmit(Action):


    def name(self) -> Text:
        return "action_submit"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        # get user input values
        person_name = tracker.get_slot("person_name")
        experience_years = tracker.get_slot("experience_years")
        experience_field = tracker.get_slot("experience_field")
        skill_category = tracker.get_slot("skill_category")
        skills_list = tracker.get_slot("skills_list")
        project_type = tracker.get_slot("project_type")
        project_clients = tracker.get_slot("project_clients")

        # do something with user input
        # for example, save the data to a database


        dispatcher.utter_message(text="Thank you for your time and consideration. I hope to hear back from you soon.")
        return
