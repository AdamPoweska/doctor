PostgreSQL-backed Django application designed to simulate a doctor–patient management system. The system handles medical specializations, doctor profiles, and appointment scheduling, offering comprehensive functionality for healthcare operations. The project was further enhanced with a Django REST Framework (DRF) version, enabling full API-based interaction and seamless integration with external clients. It supports hierarchical relationships between medical specializations, doctors, and appointment slots, utilizing nested API endpoints for structured and efficient data access.
Responsibilities:
• Designed and implemented a relational database schema to manage doctors, specializations, and appointment schedules.  
• Developed backend logic for appointment creation, assignment, and retrieval, ensuring proper relational integrity.  
• Built and maintained RESTful APIs using Django REST Framework to provide full CRUD functionality.  
• Implemented nested routing to support hierarchical access patterns, such as specialization → doctor → appointments.  
• Created multiple serializer layers (simple, detailed, and nested) to accommodate varied API consumption needs.  
• Integrated custom validation logic with UniqueTogetherValidator to prevent duplicate doctor records.  
• Developed custom queryset filtering for nested resources, such as appointments per doctor.  
• Implemented role-based permissions to restrict write operations to authenticated or staff users.  
• Designed a clean separation between core models (Doctor, Specialization, Appointment) to ensure scalability and maintainability.  
• Extended the system into a dedicated DRF API version to enable seamless integration with frontend and external systems.

User_1
P@ssword!1

superuser: admin
pw: 1234
