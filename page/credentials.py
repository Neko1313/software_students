import json

class Credentials():
    def __init__(self) -> None:
        self.personal = {
            'name': '',
            'series': '',
            'number': ''
        }
        self.answers = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: '',
            10: '',
            11: '',
            12: '',
            13: '',
            14: '',
            15: '',
        }
        
    def write_info(self):
        final_dict = {
                'personal': self.personal,
                'answers': self.answers
        }
        with open("answers.json", "w", encoding = "utf-8") as write_file:
            json.dump(final_dict, write_file, ensure_ascii=False)
                
    def get_info(self):
        return {
                'personal': self.personal,
                'answers': self.answers
            }
        
    def write_answer(self, number, answer):
        self.answers[number] = answer
        