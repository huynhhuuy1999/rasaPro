import os
from typing import Optional, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from .db import get_driver
from dotenv import load_dotenv

load_dotenv()  

NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

class get_list_subject(Action):

    def name(self) -> str:
        return "get_list_subject"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[str, Any]):
        drv = get_driver()
        
        with drv.session() as session:
            session = drv.session(database=NEO4J_DATABASE)
            result = session.run("MATCH (n:Teacher) RETURN n LIMIT 25")
           
        dispatcher.utter_message(text="Khoa có các môn học sau: Toán, Lý, Hóa, Sinh, Văn, Sử, Địa.")
        drv.close()
        return []
