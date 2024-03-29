from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship  # This was missing
from sqlalchemy.ext.declarative import declarative_base

# Example adjustment for agent_models.py and c2_models.py
from .base import Base


class Agent(Base):
    __tablename__ = 'agents'
    
    id = Column(Integer, primary_key=True)
    agent_id = Column(String, unique=True, nullable=False)
    auth_token = Column(String, nullable=False)  # Add this line for authentication token
    system_info = Column(String)
    ip_address = Column(String)
    last_checkin = Column(DateTime, default=func.now())
    task_results = relationship("TaskResult", back_populates="agent")

    def __repr__(self):
        return f"<Agent(agent_id={self.agent_id}, auth_token={self.auth_token}, system_info={self.system_info}, ip_address={self.ip_address}, last_checkin={self.last_checkin})>"