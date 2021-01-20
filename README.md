<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p align="center"><strong><img src="https://media.dhakatribune.com/uploads/2016/11/nsulogo.jpg" alt="" width="307" height="172" /></strong></p>
<p align="center"><strong>North South University</strong></p>
<p align="center">Department of Electrical &amp; Computer Engineering</p>
<p align="center"><strong>Project Final Report</strong></p>
<p align="center"><strong>Group No</strong>: 05</p>
<p align="center"><strong>Fall 2020</strong></p>
<p align="center"><strong>Project Name</strong>: Coupon Finder</p>
<p align="center"><strong>Course No</strong>: CSE 299 <strong>Section</strong><strong>:</strong> 02</p>
<p align="center"><strong>Faculty</strong>: Shaikh Shawon Arefin Shimon (Sas3)</p>
<p align="center"><strong><u>Member 1</u></strong><u>:</u></p>
<p align="center"><strong>Name</strong><strong>:</strong> Nazia Tabassum Toma</p>
<p align="center"><strong>ID</strong><strong>:&nbsp; </strong>1721536042</p>
<p align="center"><strong>Email</strong><strong>:</strong> <a href="mailto:nazia.tabassum@northsouth.edu">nazia.tabassum@northsouth.edu</a></p>
<p align="center"><strong>Git Repository</strong><strong>: </strong><a href="https://github.com/NSU-FA20-CSE299-2/Group05">https://github.com/NSU-FA20-CSE299-2/Group05/</a></p>
<p align="center"><strong>Date Prepared</strong><strong>: </strong>18/01/2020</p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>

***1. Introduction*** <br/>
We all want to find the best deals online. Coupon finder is a trusted online platform and is leading the way to discover, compare, and leverage the best discount deals, exclusive discount offers, and fascinating daily deals. Our aim is to provide massive discounts across a broad range of products, services, and activities.\
Coupon finder brings an opportunity to save money on online shopping at your favorite online store. It is, therefore, essential to understanding the way in which to use these coupon codes to save substantial amounts of money.

***2. Features***
- Anyone on the website can find the available coupon codes, offers & deals.
- Category based on shop types such as fashion, food, gadgets, etc.
- Shop website redirection from the Coupon Finder page. 
- Sign up option- Registered users will receive free email notifications about the top offers.
- Admin Panel – the admins will have full control over the whole system adding/updating shop names and/or updating other information

***3. Business Impact***
- At the growing edge of online shopping, customers will be more likely to buy their necessary stuff online as discounts are available in an organized manner. It will save their hard-earned money.
- Affiliated online shops will get information about what their customers are looking for with more discounts.
- Online shops can advertise their hot deals and get more customers.
- A cost-effective way to promote a brand, and its products while not spending huge sums without results.

## 4. Proposed Technology Stack 
We decided to go with the latest technologies for developing this application in order to give users a better experience.

*4.1 Frontend* <br/>
For the frontend, we used HTML, CSS, and Bootstrap. Bootstrap’s responsive CSS adjusts to phones, tablets, and desktops.  It also gives a more premium user interface and smoother experience. <br/>

A total of 6 page-templates in plan (as of November 14, 2020)
1. Homepage
2. Sign up page
3. Login page
4. Admin dashboard
5. Category Based Search Page
6. View Discount Coupon Page with shop details



*4.2 Backend & Database* <br/>

Python’s web framework - Django will be used as the website’s backend. Django ensures rapid development providing high security and maintenance. Django takes care of much of the hassle of web development, so we can focus on writing our code without needing to reinvent the wheel. We will be using MySQL as the database. MySQL offers advanced features and reliability far beyond a typical freeware project.

1. Account Creating, Password Recover:
- Sign up form
- Login
- Facebook login
- Google login
- Forgot Password
- MySQL Database
2. Searching Facility:
- Category based
- Shop based
3. Dashboard:
- Admin dashboard

## 5. Implemented Technology Stack 

*5.1 Frontend* <br/>
For the frontend, we used Bootstrap 4 and css for giving smoother and premium experience to our customers.

We implemented 6 pages.
1. Homepage
2. Gadget Coupon Page
3. Food Coupon page
4. Fashion Coupon page
6. Contact us page

*5.2 Backend & Database* <br/>
Python’s web framework - Django was used as the website’s backend. Django ensures rapid development providing high security and maintenance. Django takes care of much of the hassle of web development, so we can focus on writing our code without needing to reinvent the wheel. For the database requirement we have opted to use a SQL database that comes with Django by default And so we have decided to use sqlite3 for the projects database requirement.

1. Backend for Homepage 
2. Backend for Gadget Coupon Page 
3. Backend for Food Coupon page
4. Fashion Coupon page     
5. Dashboard:
- Admin dashboard

***6. Roadblocks***

We tried to use Python's Scrapy Framework for scrapping data from the shop websites but we found that those data are not always updated and mostly written in Bangla. So we decided not to go with web scrapping approach. 

Also, in our project proposal we wanted to implement a Sign Up/Login portal for our users but on the implementation stage, we decided not to go with that because main goal of our project was finding coupons only. Instead of Login portal we decided to have a notification system for users through mail about new availabe coupons.



***7. MONETIZATION***

- CPC- Cost per click will be added to the advertisements.
The percentage of selling will be taken from online shops as per the use of coupons.
- Online shops will have to pay if they want to promote their hot deals or trending products.
- The percentage and cost will be calculated based on website traffic.



***8. Developed Project***

**Admin Dashboard** <br/>
Only superadmin can access this dashboard using username and password. Super admin can add, remove, edit any available code to the website.

![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/admin1.png)
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/admin2.png)
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/admin3.png)
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/admin4.png)


**Homepage** <br/>
User can visit this page and find available coupons.

![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/homepage1.png)
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/homepage2.png)


**Gadget Coupon Page** <br/>

User can find coupons for gadgets in this page.

![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/gadget1.png)


**Food Coupon Page** <br/>

User can find coupons for food iteams in this page.

![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/food1.png)
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/food2.png)


**Fashion Coupon Page** <br/>

User can find coupons for fashion iteams in this page.
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/fashion1.png)

**Contact Us Page** <br/>
![alt text](https://github.com/NSU-FA20-CSE299-2/Group05/blob/main/Code/Images/contactus.png)



