import logging

class ContainerDeploy:

    def __init__(self, user: dict) -> None:
        self.user = user
    
    def deploy(self) -> dict:
        logging.info("Deploying new application")
        return self.successful_response(201)
    
    def successful_response(self, status_code:int):
        return  {
            "status": status_code,
            "status_message": "Successfully deployed..!"
        }