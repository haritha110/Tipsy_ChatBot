import asyncio
import json
from ctypes import pythonapi
from agents.agent_orchestration import TicketProcessor
from data_models import SupportTicket
from dotenv import load_dotenv
import os
from templates.response_templates import RESPONSE_TEMPLATES  # Import the dictionary

load_dotenv()

with open("templates/response_templates.py", "r") as f:
    RESPONSE_TEMPLATES = exec(f.read())

async def main():
    processor = TicketProcessor(RESPONSE_TEMPLATES)

    SAMPLE_TICKETS = [
        {
            "id": "TKT-001",
            "subject": "Cannot access admin dashboard",
            "content": """
            Hi Support,
            Since this morning I can't access the admin dashboard. I keep getting a 403 error.
            I need this fixed ASAP as I need to process payroll today.

            Thanks,
            John Smith
            Finance Director
            """,
            "customer_info": {
                "role": "Admin",
                "plan": "Enterprise",
                "company_size": "250+",
                "name": "John Smith"
            }
        },
        {
            "id": "TKT-002",
            "subject": "Question about billing cycle",
            "content": """
            Hello,
            Our invoice shows billing from the 15th but we signed up on the 20th.
            Can you explain how the pro-rating works?

            Best regards,
            Sarah Jones
            """,
            "customer_info": {
                "role": "Billing Admin",
                "plan": "Professional",
                "company_size": "50-249",
                "name": "Sarah Jones"
            }
        },
        {
            "id": "TKT-003",
            "subject": "URGENT: System down during demo",
            "content": """
            System crashed during customer demo!!!
            Call me ASAP: +1-555-0123

            -Sent from my iPhone
            """,
            "customer_info": {
                "role": "Sales Director",
                "plan": "Enterprise",
            }
        },
        {
            "id": "TKT-004",
            "subject": "It's not working",
            "content": "Nothing works. Please help.",
            "customer_info": {
                "role": "User",
                "plan": "Basic",
            }
        }
    ]

    for ticket_data in SAMPLE_TICKETS:

        ticket = SupportTicket(**ticket_data)  # Create SupportTicket object here
        resolution = await processor.process_ticket(ticket)  # Pass the ticket
        print(f"--- Ticket ID: {ticket.id} ---")
        print(f"Analysis Category: {resolution.analysis.category}")
        print(f"Analysis Priority: {resolution.analysis.priority}")
        print(f"Response: \n{resolution.response.response_text}\n")


        print("\n--- Analysis Results ---")
        print(f"Category: {resolution.analysis.category}")
        print(f"Priority: {resolution.analysis.priority}")
        print(f"Key Points: {resolution.analysis.key_points}")
        print(f"Required Expertise: {resolution.analysis.required_expertise}")
        print(f"Sentiment: {resolution.analysis.sentiment}")
        print(f"Urgency Indicators: {resolution.analysis.urgency_indicators}")
        print(f"Business Impact: {resolution.analysis.business_impact}")
        print(f"Suggested Response Type: {resolution.analysis.suggested_response_type}")

        print("\n--- Generated Response ---")
        print(f"Response Text: {resolution.response.response_text}")
        print(f"Confidence Score: {resolution.response.confidence_score}")
        print(f"Requires Approval: {resolution.response.requires_approval}")
        print(f"Suggested Actions: {resolution.response.suggested_actions}")
        print("-" * 30)


if __name__ == "__main__":  # This block should only appear ONCE, at the very end
    asyncio.run(main())