from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# Assuming Base is defined in a shared base.py or within these files
from .agent_models import Agent

# Example adjustment for agent_models.py and c2_models.py
from .base import Base


class Command(Base):
    __tablename__ = 'commands'
    
    id = Column(Integer, primary_key=True)
    command_text = Column(Text, nullable=False)
    issued_by = Column(String)
    issued_at = Column(DateTime, default=func.now())
    
    # Establishes a relationship with TaskResult
    task_results = relationship("TaskResult", back_populates="command")

    def __repr__(self):
        return f"<Command(command_text={self.command_text}, issued_by={self.issued_by}, issued_at={self.issued_at})>"

class TaskResult(Base):
    __tablename__ = 'task_results'
    
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    command_id = Column(Integer, ForeignKey('commands.id'))
    result = Column(Text)
    received_at = Column(DateTime, default=func.now())
    
    # Correctly establish relationships to Agent and Command
    agent = relationship("Agent", back_populates="task_results")
    command = relationship("Command", back_populates="task_results")

    def __repr__(self):
        return f"<TaskResult(result={self.result}, received_at={self.received_at})>"
