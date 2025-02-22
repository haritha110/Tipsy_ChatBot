from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from data_models import TicketAnalysis, ResponseSuggestion, TicketCategory


class ResponseAgent:
    async def generate_response(
            self,
            ticket_analysis: TicketAnalysis,
            response_templates: Dict[str, str],
            context: Dict[str, Any]
    ) -> ResponseSuggestion:

        template_key = None
        if ticket_analysis and isinstance(ticket_analysis, TicketAnalysis):  # Check if it's a TicketAnalysis object
            if ticket_analysis.category == TicketCategory.ACCESS:
                template_key = "access_issue"
            elif ticket_analysis.category == TicketCategory.BILLING:
                template_key = "billing_inquiry"

        template = response_templates.get(template_key, response_templates.get("default_response",
                                                                               "Default Response: We are looking into your issue."))  # Provide a default template

        response_text = template  # Initialize with the chosen template or the default

        confidence_score = 0.7
        requires_approval = False
        suggested_actions = []

        if ticket_analysis and isinstance(ticket_analysis, TicketAnalysis) and context and isinstance(context,
                                                                                                      dict):  # Check if both objects exist
            # --- Template Customization ---
            name = context.get("customer_name", "Customer")
            priority_level = ticket_analysis.priority.name

            # Initialize these variables with default values to avoid errors
            feature = "feature_name_placeholder"
            diagnosis = "diagnosis_placeholder"
            resolution_steps = "resolution_steps_placeholder"
            billing_topic = "billing_topic_placeholder"
            explanation = "explanation_placeholder"
            next_steps = "next_steps_placeholder"
            eta = "24-48 hours"  # Placeholder ETA

            if ticket_analysis.category == TicketCategory.ACCESS:
                feature = "admin dashboard"
                diagnosis = "We have identified a potential issue with account permissions."
                resolution_steps = "Our team is currently investigating and will restore your access as soon as possible. In the meantime, please ensure you are using the correct login credentials."
            elif ticket_analysis.category == TicketCategory.BILLING:
                billing_topic = "your billing cycle"
                explanation = "Our billing cycle starts on the 15th of each month. Since you signed up on the 20th, you are seeing a charge for the period from the 15th to the end of the month."
                next_steps = "We will ensure your next invoice is correctly pro-rated."

            try:  # Use a try-except block for template formatting
                response_text = template.format(
                    name=name,
                    feature=feature,
                    diagnosis=diagnosis,
                    resolution_steps=resolution_steps,
                    priority_level=priority_level,
                    eta=eta,
                    billing_topic=billing_topic,
                    explanation=explanation,
                    next_steps=next_steps
                )
            except KeyError as e:  # Catch missing keys
                print(f"Missing key in template or context: {e}")
                response_text = "Error generating response: Missing information."  # Provide a user-friendly message
                confidence_score = 0.1  # Lower confidence
                requires_approval = True  # Requires approval

        return ResponseSuggestion(
            response_text=response_text,
            confidence_score=confidence_score,
            requires_approval=requires_approval,
            suggested_actions=suggested_actions,
        )





