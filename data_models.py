from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

class TicketCategory(Enum):
    TECHNICAL = "technical"
    BILLING = "billing"
    FEATURE = "feature"
    ACCESS = "access"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

@dataclass
class TicketAnalysis:
    category: TicketCategory
    priority: Priority
    key_points: List[str]
    required_expertise: List[str]
    sentiment: float
    urgency_indicators: List[str]
    business_impact: str
    suggested_response_type: str

@dataclass
class ResponseSuggestion:
    response_text: str
    confidence_score: float
    requires_approval: bool
    suggested_actions: List[str]

@dataclass
class SupportTicket:
    id: str
    subject: str
    content: str
    customer_info: dict

@dataclass
class TicketResolution:
    analysis: TicketAnalysis
    response: ResponseSuggestion