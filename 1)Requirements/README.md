# GUI Based Banking System
Online banking system provides is specifically developed for internet banking for Balance  Enquiry, Funds Transfer to another account in the same bank, Request for cheque  book/change of address/stop payment of cheques, Mini statements (Viewing Monthly and  annual statements).

The Traditional way of maintaining details of a user in a bank was to enter the details and record  them. Every time the user need to perform some transactions he has to go to bank and perform  the necessary actions, which may not be so feasible all the time. It may be a hard hitting task for  the users and the bankers too. The project gives real life understanding of Internet banking and  activities performed by various roles in the supply chain. Here, we provide an automation for  banking system through Internet. Internet banking system project captures activities performed by different roles in real life banking which provides enhanced techniques  for maintaining the required information up to date, which results in efficiency. The project  gives real life understanding of Internet banking and activities performed by various roles in the  supply chain.

# Overall Description
## Product Perspective 
This is a simple GUI based application which is very easy to understand and use. It uses Tkinter module for the GUI. Talking about the application, the user can simply create their account and login in order to manage their bank accounts. 
## Product Features 
The user can register his/her account by providing details such as username, opening balance, and pin number. After that, the user has to provide those details in order to access their account. The user can view his/her transaction details, balance inquiry, credit and debit amount. By entering a certain amount only, the user can credit or debit amounts. From this type of application, a user can simply manage his personal accounts with fewer efforts. 
## Operating Environment 
In order to run the project, we have to install Python which a free and open-source IDLE. We will run this application on windows pc. Complier/Interpreter used will be VS Code.
## Assumptions and Dependencies
The only tangible benefit provided by the proposed system is that the paper work is reduced to the minimum and hence the reduction in cost incurred on Stationary and its storage. The system provides many benefits that can’t be measured in terms of Money for e.g., user’s friendliness, more user response being more efficient. 

The proposed system is technically feasible as it can be developed easily with the help of available technology.  Automation makes our life easy. The proposed system is highly user friendly and is much easily able to interact with the system. Therefore, the users will readily accept the system as data entry and making queries can be easily done.

# Functional Requirement Specification
Requirements specifications add further information to the requirements definition. Natural language is often used to write requirements specifications. However, a natural language specification is not a particularly good basis for either a design or a contract between customer and system developer.
A Functional Requirements Specification describes what is required to meet the users' business needs. Functional requirements specify which actions the design must provide in order to benefit the system's users. Functional requirements are determined by the needs, user, and task analysis of the current system.

 Customer
We mention to what the customer needs to do on internet banking system and we are going to go through these needs and how the customer can do it.

 Login
Definition: For the users to be able to use this system, they have to enter username and password which they have created before and been saved in the database in the 
Login page. The user might be a customer or an Admin also.
Inputs: Username and password.
Outputs: The system will state whether inputs are correct or not.
Pre conditions: The user must have signed in the system and have a valid username and password. Then the system will show the main page to the valid customer and display message “welcome to the internet banking
system please click on the left menu bar to choose your option!” he/she can make has/her transaction, but if the user made wrong in username or password then he/she will be invalid user and will see a message “Alert Invalid Username and Password” and to login again.
Post conditions: The user will enter the main page of him/her self.

 View Account
Definition: View Account allows to a customer to view today’s up-to-the minute balance information on deposit (saving/current), credit card, etc. The customer can also view transaction history with retention period up to a maximum of 90 days. Within this feature, the customer can request for account such as “view online, by e-mail or by post option. But the customer most be logged in the internet banking.
Inputs: there are not inputs in this function.
Outputs: the system will show the View Account page and display a message” Please click on the respective account/card types for more details. Customer can choose current account or saving account for more details.
Pre conditions: The customer must be a valid customer and signed in the system.
Post conditions: The customer clicks on the logout button or select other functionality options. 

 Logout
Definition: This function is used when a logged in user finishes his/her job and wants to be logged out therefore, that no one can abuse his/her username.
Inputs: there are not inputs in this function.
Outputs: The system will show the user has been logged out successfully.
Pre conditions: The user should have logged into the system.
Post conditions: The user will enter the main page of the system.

# Non-functional Requirements
Non-functional requirements are requirements that are not directly concerned with the specific functions delivered by the system. They may relate to emergent system properties such as reliability, response time and store occupancy. They may specify system performance, security, availability, and other emergent properties. This means that they are often more critical than individual functional requirements. System users can usually find ways to work around a system function that doesn’t really meet their needs. However, failing to meet a nonfunctional requirement can mean that the whole system is unusable. Non-functional requirements needed in this internet banking system are identified as performance
requirements, safety requirements, security requirements and software quality attributes.

 Performance Requirements
 
 Increase Customer Satisfaction
 
Internet banking system must allows customers to access banking services 24 hours a day, 365 days a year with minimum downtime period for backup and maintenance.

Expand Product Offerings

The new services allows bank to capture a larger percentage of their customers’ asset base. The internet banking system will provide facilities for bank to offer new services and products onto its homepage.

 Reduce Overall Costs
 
It will help to reduce a bank’s costs in two fundamentalways: it minimize the cost of processing transactions and reduces the number of branches required to service an
equivalent number of customer.

 Safety Requirements
 
 Backup, recovery & business continuity Banks should ensure adequate back up of data as may be required by their operations. Banks should also have, well
 1. Both data and software should be backed up periodically, the frequency of back up depending on the recovery needs of the application. The back-up may be incremental or complete. Automating the backup procedures is preferred to obviate operator errors and missed back-ups.
2. Recovery and business continuity measures, based on criticality of the systems, should be in place and a documented plan with the organization and assignment of responsibilities of the key decision making personnel should exist.
3. An off-site back up is necessary for recovery from major failures / disasters to ensure business continuity. Depending on criticality, different technologies based on back up, hot sites, warm sites or cold sites should be available for business continuity. The business continuity plan should be frequently tested.

 Security Requirements
 
We understand that there is nothing more important than knowing that transactions are private and secure.Therefore, we have applied the very latest in technology when creating the Internet Banking security architecture. The best way to understand the security architecture within the Internet Banking is to take it one step at a time.These security features are described briefly below.

 Sign-off Button
 
When an end-user is finished with Internet Banking, they should click the Sign-off button before going anywhere else on the Web. This ends the Internet Banking session.

 Failed Log-on Attempts
 
As an added security feature, the Internet Banking System is denied access after a pre-determined number of failed log-on attempts. If users have been locked out due to exceeding the pre-determined number of log-on attempts,the users must contact the Bank in order to be reinitialized.

Encryption

In addition to password protection, we ensures server authentication by using the latest techniques of data encryption. Data encryption is a way of translating data into a form that is unintelligible without a deciphering mechanism. 
