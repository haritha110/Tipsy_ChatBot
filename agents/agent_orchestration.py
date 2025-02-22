from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from data_models import TicketAnalysis, ResponseSuggestion, TicketCategory, SupportTicket, TicketResolution # Import data models
from agents.ticket_analysis_agent import TicketAnalysisAgent
from agents.response_generation_agent import ResponseAgent
from data_models import TicketAnalysis, ResponseSuggestion, TicketCategory, SupportTicket, TicketResolution, Priority  # Add Priority here
from templates.response_templates import RESPONSE_TEMPLATES   # Import the dictionary

class TicketProcessor:
    def __init__(self, response_templates: Dict[str, str]):  # Add templates here
        self.analysis_agent = TicketAnalysisAgent()
        self.response_agent = ResponseAgent()
        self.context = {}
        self.response_templates = response_templates  # Store templates

    async def process_ticket(
            self,
            ticket: SupportTicket,
    ) -> TicketResolution:

        try:
            # --- Context Maintenance (Basic) ---
            self.context["customer_name"] = ticket.customer_info.get("name", "Valued Customer")  # Example context
            self.context["customer_history"] = ticket.customer_info  # Placeholder for actual history

            # --- Sequential Processing ---
            analysis = await self.analysis_agent.analyze_ticket(
                ticket.content, ticket.customer_info
            )
            response_suggestion = await self.response_agent.generate_response(
                analysis, RESPONSE_TEMPLATES, self.context
            )

            # --- Response Validation (Placeholder - more sophisticated validation needed in real scenario) ---
            if not response_suggestion.response_text:
                raise ValueError("Response generation failed: Empty response")

            return TicketResolution(analysis=analysis, response=response_suggestion)

        except Exception as e:
            print(f"Error processing ticket {ticket.id}: {e}")
            # --- Error Handling ---
            error_response_text = f"Apologies, we encountered an issue processing your request. Please try again later or contact support directly. Error details: {e}"
            error_response = ResponseSuggestion(
                response_text=error_response_text,
                confidence_score=0.1,
                requires_approval=True,
                suggested_actions=["Escalate to human support"],
            )
            error_analysis = TicketAnalysis(  # Create a default analysis for error case
                category=TicketCategory.TECHNICAL,  # Default error category
                priority=Priority.HIGH,  # Error is usually high priority
                key_points=["System error during processing"],
                required_expertise=["Technical Escalation"],
                sentiment=-0.8,  # Negative sentiment due to error
                urgency_indicators=["Processing failure"],
                business_impact="Unknown",
                suggested_response_type="Error Response"
            )
            return TicketResolution(analysis=error_analysis, response=error_response)