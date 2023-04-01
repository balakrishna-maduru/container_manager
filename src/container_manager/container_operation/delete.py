import logging

class ContainerDelete:

    def __init__(self, user: dict) -> None:
        self.user = user
    
    def delete(self) -> dict:
        logging.info("Delete continer on exist")
        return self.successful_response(203)
    
    def successful_response(self, status_code:int):
        return  {
            "status": status_code,
            "status_message": "Successfully deleted ...!"
        }