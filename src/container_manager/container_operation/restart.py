import logging

class ContainerRestart:

    def __init__(self, user: dict) -> None:
        self.user = user
    
    def restart(self) -> dict:
        logging.info("Restart continer on exist")
        return self.successful_response(201)
    
    def successful_response(self, status_code:int):
        return  {
            "status": status_code,
            "status_message": "Successfully restarted..!"
        }