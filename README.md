# Zorvyn-Assignment
This is the assignemt that i got for Backend developer role 
# finance-backend-
This assignment i was tasked to build Finance Data Processing and Access Control Backend 
We were tasked for building the backend for a finance dashboard system where different users interact with financial record based on their role. 
In this assignment we have build :
1.Role based Access Control 
2.Secure Authentication 
3.Financial Record Management 
4.Dashboard Summary API 
5.Validation and Error Handling 
I have written the whole backend using Python. I chose Python beacuse of its simplicity and rapid development capabilities and availablity of Framework like FastAPI that allows building high performance APIs with minimal efforsts.Python is really good for the data processing and analytics tasks which was our requirement . 

Tech Stack 
1.Fast API 
I choose this because it provides high performance,built in validation and automatic API documentation,which make overall development process much more faster and clean compared to traditional framework like Node.js 
2.SQLAlchemy 
  It provide a flexibility between ORM (Object relation mapping)and raw SQL which is very useful for both CRUD operations and complex query
3. SQLite 
    I used SQLite for simplicity and ease of setup, since the goal was to demonstrate backend logic rather than production-scale infrastructure.
4. JSON Web Token(JWT)
    I implemented JWT-based authentication because it allows stateless and scalable user authentication, which fits well with REST APIs. 

Users Roles 
1. Viewer : Read only access
2. Analyst : Read + analytics dashboard access
3. Admin : Full control

Autherntiation 
1.JWT based Authentication 
2.Login return access token 
3.Token are required for protected routes 

API Endpoints 
1.Auth 
  POST / auth/login : Used for Login and get token 
2.Users 
  POST /users : Create user 
  GET/users : Get all users 
3.Records 
  POST/records : Create a financial record 
  GET/records : Get records with filter and Pagination
  PUT / recordds/{id} : Update record
  DELETE/records/{id} : Delete record
4. Dashboard
  GET /dashboard/summary : Total income,expense, net balance 
  GET / dashboard/category : Category wise totals 
  GET/dashboard/trends : Monthly trends
  GET / dashboard/recent : Recent Transaction 
Filtering and Pagination : To filter the records using query parameters 
These are the following featiures that i have implemented 
1.User management with roles 
2.Role based access control 
3.JWT authentication 
4.CRUD operation 
5.Filtering and pagination 
6.Dashboard analytics
7.Soft delete that ensures data safety and auditability
8.Rate limiting that protects the system from a misuse
9.Search record feature improve the usability for large datasets
Database Design 
USER Table 
  id
  name
  email
  password
  role (viewer, analyst, admin)
  is_active
  created_at
Financial Record Table 
  id
  user_id (FK)
  amount
  type (income / expense)
  category
  date
  notes
  created_at
Backend Architecture 
I have used a Layered Architecture for the backend  
      Client → Routes → Services → Models → Database
               ↑
           Schemas (Validation)
               ↑
         Auth & RBAC (Security)
1.Rotes Layer (app/routes/)
    Handles HTTP requests 
    Define API endpoints and call service layer
    Applies authentication and role checks 
2.Service Layer(app/service)
    It contains Business logic iyt process data,applies filter and handles the complex operations 
3.Model layer(app/models/)
    It is used to define the database structure like Tables,Relationships and Schema Mapping 
4.Schemas LAYER(app/schemas)
  It is for the input validation as it ensures correct data format and prevents the invalid inputs 
5. Database Layer(app/db/)
    It handels the database connection like SQLAlhemy setup and dession management 
6. Core Layer (app/core/)
    It has security and Utilities features like JWT authentication and Role based access control 

Layered based architecture is very easy to scale and it is clean and easy to maintain 
While building this i have made some Asumptions that are as follows : 
1.Sngle currency system 
2.Categories are free text it means that user can enter any category as plain text without restriction 
3.Authentication simpleified for demonstration 

There are things that i would like to improve like Adding refresh tokens for authentication,Caching for this Project to work for Efficiently 


Author : Atish Kumar Jha 
