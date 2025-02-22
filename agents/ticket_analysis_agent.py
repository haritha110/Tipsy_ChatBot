from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from data_models import TicketAnalysis, TicketCategory, Priority

class TicketAnalysisAgent:
    async def analyze_ticket(self, ticket_content: str, customer_info: Optional[dict] = None) -> TicketAnalysis:
        category = TicketCategory.TECHNICAL  # Default, but will be overwritten
        priority = Priority.LOW
        key_points = []
        required_expertise = ["General Support"]
        sentiment = 0.0
        urgency_indicators = []
        business_impact = "Low"
        suggested_response_type = "Standard"

        ticket_content_lower = ticket_content.lower()  # Convert to lowercase ONCE
        # subject_lower = ticket_content.lower()  # If you add subject, do this separately

        # Use more precise keyword matching (important!)
        if any(keyword in ticket_content_lower for keyword in ["billing", "invoice", "payment"]):
            category = TicketCategory.BILLING
            required_expertise = ["Billing Support"]
        elif any(keyword in ticket_content_lower for keyword in ["feature request", "new feature", "suggest"]):
            category = TicketCategory.FEATURE
            required_expertise = ["Product Team"]
        elif any(keyword in ticket_content_lower for keyword in ["access", "login", "dashboard", "account"]):
            category = TicketCategory.ACCESS
            required_expertise = ["Account Support"]
        elif any(keyword in ticket_content_lower for keyword in ["error", "not working", "issue", "problem", "crash"]):
            category = TicketCategory.TECHNICAL
            required_expertise = ["Technical Support"]

        if customer_info and isinstance(customer_info, dict): # Check if it's a dictionary
            role = customer_info.get("role", "").lower()
            if "director" in role or "c-level" in role:
                priority = Priority.HIGH

        urgency_keywords = ["urgent", "asap", "immediately", "critical", "system down", "important"]
        if any(keyword in ticket_content_lower for keyword in urgency_keywords): # More efficient way
            priority = Priority(max(priority.value, Priority.HIGH.value))
            urgency_indicators.extend(keyword for keyword in urgency_keywords if keyword in ticket_content_lower)

        if "payroll" in ticket_content_lower or "revenue" in ticket_content_lower or "demo" in ticket_content_lower:
            priority = Priority(max(priority.value, Priority.URGENT.value))
            business_impact = "High"

        # Key Point Extraction (Improved and consistent)
        if category == TicketCategory.ACCESS:
            key_points.extend(keyword for keyword in ["dashboard access issue", "403 error encountered", "login problem"] if keyword in ticket_content_lower)
        elif category == TicketCategory.BILLING:
            key_points.extend(keyword for keyword in ["billing cycle inquiry", "pro-rating question", "invoice date"] if keyword in ticket_content_lower)
        elif category == TicketCategory.TECHNICAL:
            key_points.extend(keyword for keyword in ["system outage reported", "403 error encountered"] if keyword in ticket_content_lower)

        return TicketAnalysis(
            category=category,
            priority=priority,
            key_points=key_points,
            required_expertise=required_expertise,
            sentiment=sentiment,
            urgency_indicators=urgency_indicators,
            business_impact=business_impact,
            suggested_response_type=suggested_response_type,
        )



