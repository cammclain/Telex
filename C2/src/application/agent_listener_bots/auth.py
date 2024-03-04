from sqlalchemy.orm import Session
from .agent_models import Agent  # Adjust the import path as necessary

async def authenticate_agent(agent_id, provided_auth_token):
    with Session() as session:
        agent = session.query(Agent).filter_by(agent_id=agent_id).first()
        if agent and agent.auth_token == provided_auth_token:
            # Optionally update the last check-in time here
            return True
        else:
            return False