import streamlit as st
import asyncio
from agents.agent_orchestration import TicketProcessor
from data_models import SupportTicket
import json

# Load response templates
with open("templates/response_templates.py", "r") as f:
    RESPONSE_TEMPLATES = exec(f.read())

# Initialize TicketProcessor
processor = TicketProcessor(RESPONSE_TEMPLATES)

st.title("Customer Support Ticket System 🤖")
#st.set_page_config(page_title="TIPSY_Bot:Customer Support Ticket System", page_icon="🤖", layout="wide")

# Input fields
ticket_id = st.text_input("Ticket ID")
subject = st.text_input("Subject")
content = st.text_area("Content", height=150)
customer_name = st.text_input("Customer Name")
customer_role = st.text_input("Customer Role")
customer_plan = st.text_input("Customer Plan")
customer_company_size = st.text_input("Customer Company Size")

if st.button("Submit Ticket"):
    if not ticket_id or not subject or not content:
        st.error("Please fill in all required fields.")
    else:
        customer_info = {
            "name": customer_name,
            "role": customer_role,
            "plan": customer_plan,
            "company_size": customer_company_size
        }
        ticket_data = {
            "id": ticket_id,
            "subject": subject,
            "content": content,
            "customer_info": customer_info
        }

        try:
            ticket = SupportTicket(**ticket_data)
            resolution = asyncio.run(processor.process_ticket(ticket))  # Run async in Streamlit

            st.subheader("Ticket Analysis")
            st.write(f"Category: {resolution.analysis.category}")
            st.write(f"Priority: {resolution.analysis.priority}")
            # ... (Display other analysis results)

            st.subheader("Generated Response")
            st.write(resolution.response.response_text)
            # ... (Display other response details)

        except Exception as e:
            st.error(f"Error processing ticket: {e}")