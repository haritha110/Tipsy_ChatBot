RESPONSE_TEMPLATES = {
    "access_issue": """
    Hello {name},

    I understand you're having trouble accessing the {feature}. Let me help you resolve this.

    {diagnosis}

    {resolution_steps}

    Priority Status: {priority_level}
    Estimated Resolution: {eta}

    Please let me know if you need any clarification.

    Best regards,
    Baguette Support
    """,

    "billing_inquiry": """
    Hi {name},

    Thank you for your inquiry about {billing_topic}.

    {explanation}

    {next_steps}

    If you have any questions, don't hesitate to ask.

    Best regards,
    Baguette Billing Team
    """
}
