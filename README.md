# **Ayo Recipes**

![overview of AYO RECIPES on all devices](static/images/readme/general-overview.png)

Ayo Recipes is a modern recipe sharing website that caters to people of all ages. Its mission is to provide users with luxury cuisine food recipes in the comfort of their own home, eliminating the stress associated with pre-cooking.  At Ayo Recipes, we understand the hassle of cooking as well as the thought process involved in deciding on a specific meal to prepare .

Ayo Recipes provides users with simple recipes shared by our members, as well as coupons for kitchenware that makes cooking easier and more enjoyable. The user can easily search for a recipe category/recipe name, view its content, and order the meal from the page; however, the user must login/register to the site in order to see the order button, access cooking tips and tricks, and create their own recipe.

The goal of the site is for the user to be able to perform basic CRUD functionality(Create, Read, Update, and Delete) on the site and interact with it intuitively, having  a positive experience.   

[View deployed site](http://ayo-recipes.herokuapp.com/)

# **Table of Contents**   
1. [UX Development](#ux-development)
    * [PROJECT GOAL](#project-goal) 
        * [Business Goals](#business-goals)
      
    * [USER STORIES](#user-stories)
        * [New User](#new-user)
        * [Registered Users/Returning Users](#registered-user-or-returning-users)
        * [Admin User](#admin-user)
        * [Target Audience](#target-audience)

   * [RESEARCH](#research)

   * [DESIGN](#design)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Imagery](#imagery)
        * [Wireframes](#wireframes)
        * [Database Structure](#database-structure)

      
2. [Features](#features)  
    * [EXISTING FEATURES](#existing-features) 
        * [General Features On All Pages](#general-features-on-all-pages)
        * [Features Of Each Page](#features-of-each-page)
        * [Features To Implement In Future](#features-to-implement-in-future)

      
3. [Technology Used](#technology-used)  
    * [Language Used](#language-used) 
    * [Frameworks,libraries and Program Used](#frameworkslibraries-and-program-used)  
   
4. [Testing](#testing)   
    * [TEST.md](#testing)   

5. [Deployment](#deployment)  
    * [Deployment Heroku](#deployment-heroku) 
    * [Steps To Use This Project](#steps-to-use-this-project)  

7. [Credits](#credits)  
    * [Content](#content) 
    * [Media](#media)  
 
8. [Acknowledgements](#acknowledgements)  

<br/>   

# **UX Development**   

## **PROJECT GOAL**
Ayo Recipe's primary goal is to provide a visually appealing and highly intuitive recipe sharing site for users of all ages. The user should be able to see all recipes and recipes in each category, as well as perform basic CRUD (Create, Read, Update, and Delete) functions on the site. 

The user would be able to interact with the site in order to create, edit, delete, and add recipes to their profile, with some restrictions in place only for the admin user. The admin user has the ability to create, edit, and delete recipe categories, as well as perform basic user functions.

#### **Business Goals** 
As the site owner I want to :
1.	Create a visually appealing site that users are able to interact with and perform all the CRUD functions. 
2.	Create a highly intuitive website that promotes brand awareness and is user friendly.
3.	Be able to collect data from various users once they register/login to assist with more business informed decisions. 
4.	Attract new users to the site to  boost online traffic.

### **USER STORIES**
#### **NEW USER**
As a new/ unregistered user, I want to:
1.	Easily understand the purpose of the site and how it works 
2.	View all the recipes available with directions on how to prepare and cook the recipe. 
3.	Easily search for recipes and be able to view the full details of the recipe interested in.
4.	Easily locate the call to action buttons on the site to allow the user either register or Sign up .

#### **REGISTERED USER OR RETURNING USERS**
As a returning/ registered user, I want to:
1.	Easily Log In into my profile dashboard to explore recipes made by me.
2.	Easily search for recipes either by recipe name or the recipe category.
3.	Be able to create my own recipe and share on the site. Edit it’s content and delete if the case need be. 
4.	Easily edit my personal profile in case changes are needed. 
5.	Be able to order recipes online.

#### **ADMIN USER**
As an Admin User, I want to:
1.	Be able to do all the functionalities assigned to a registered user .
2.	Restrict access for certain features that can only be accessed by the admin. 
3.	Add, Edit, or Delete the category of recipes present.
4.	Be able to edit , delete and update any recipes listed on the site.

#### **TARGET AUDIENCE**
- Those looking for festive recipes to make.
- Individuals who are willing to post their own recipes on the internet.
- Individuals who are interested in food and enjoy cooking. 
- Individuals who are want to learn how to cook. 
- People who appreciate the ease of ordering food via technology and social media. 


### **RESEARCH**   
To get some UX inspiration for Ayo, I researched other recipe sharing websites like
1. [Yummly](https://www.yummly.co.uk/)
2. [Bbcgoodfood](https://www.bbcgoodfood.com/)
3. [Epicurious](https://www.epicurious.com/) 
4. Similar recipe sharing sites created by other Code Institute peers (searched in the Slack channel peer-code-review) were examined. 

To gain a design understanding of what these sites have in common and how Ayo Recipes can improve their own service by addressing the problems associated with recipe sharing sites. According to research, these sites appeared to be a bit overwhelming and were packed with a lot of information that bombarded the user as to where to start, potentially leading to users abandoning the site.

Ayo Recipes is a fun modern recipe sharing platform that considers the aforementioned issues. The site has been evenly spaced and kept clean in order for the user to easily navigate through the various pages without feeling overwhelmed. The admin manages the site's information, which is regularly updated to keep it up to date and to ensure that the UX is consistent across all pages and that all links work

## **DESIGN**   
### **Color Scheme**   
The colours used in the design of Ayo Recipes were created using the [Adobe Color site](https://color.adobe.com/search?q=recipe&t=term). The colours were handpicked and researched to ensure that they communicated to our users subconsciously. 

[Jen David](https://jenndavid.com/colors-that-influence-food-sales-infographic/) has provided us with a colour chart that can influence your gourmet industry business and has been used in the colour selection for Ayo Recipes. The colours reflect the Ayo Recipes brand in order to build trust with users and stimulate their taste buds by using bright colours (yellow and orange) to catch our users' attention and brown/white to give it a warm, welcoming, and clean look. <br/>
![The color scheme](static/images/readme/colorpalette.png "The color scheme")  

<br/>

### **Typography**    
The [Google Fonts](https://fonts.google.com) Dancing Script and Poppins are used on the website to ensure consistency and to give the site a distinct and friendly look similar to other recipe sharing websites. The two fonts are appealing to our target audience, and a backup font has been included called sans-serif.

<br/>

### **Imagery**  
The photos on the site were obtained from a free image provider [Unsplash](https://unsplash.com/), and the recipe images were obtained from bbcgoodfood, Yummly, and epicurious.

Photoshop was used to create the brand logo and the background image that appears on some pages of the website.

The photographs depict modern cuisine dishes that can be prepared in the comfort of one's own home. The images' purpose is to attract users' attention to the Ayo Recipe website, where they can login/register to create their own recipes.

<br/>

### **Wireframes**
The entire site's wireframe can be found below. This depicts the site on a desktop and a mobile device, with some tablet view wireframes indicating when the screen view differs.

* [Wireframe for Home Page](static/images/readme/homepage-wireframe.png)   
* [Wireframe for Recipes Page](static/images/readme/wireframe-recipes-page.png)   
* [Wireframe for Individual Single Recipe Page](static/images/readme/single-view-recipe.png)
* [Wireframe for Register Page](static/images/readme/register-wireframe.png)   
* [Wireframe for Profile with recipes](static/images/readme/profile-with-recipe-wireframe.png)
* [Wireframe for Profile without recipes](static/images/readme/profile-no-recipe-wireframe.png) 
* [Wireframe for Edit Profile](static/images/readme/edit-profile-wireframe.png)  
* [Wireframe for Add Recipe](static/images/readme/add-recipe-wireframe.png)   
* [Wireframe for Edit Recipe ](static/images/readme/edit-recipe-wireframe.png)
* [Wireframe for Manage Categories](static/images/readme/wireframe-for-managecategories.png)
* [Wireframe for Edit Category](static/images/readme/edit-category-wireframe.png)
* [Wireframe for Side Nav](static/images/readme/tablet-view.png)
* [Wireframe for View Each Category](static/images/readme/view-category-wireframe.png)
* [Wireframe for Delete Category](static/images/readme/delete-category-wireframe.png)
* [Wireframe for Tips & Tricks](static/images/readme/wireframe-for-tips-page.png)
* [Wireframe for Login](static/images/readme/login-page.png)

<br/>

### **Database Structure** 
MongoDB was chosen as the database for this project due to the flexibility it offers for non-relational data. [Diagram.io](https://dbdiagram.io/home) was used to create the data schema for this project. Our schema had three collections: 
* Users
* Categories
* Recipes 
   
![Database structure](static/images/readme/database-schema.png "Database schema")   

Users can create an unlimited number of recipes, but each recipe is associated with a unique user id. The same holds true for the recipes table; each recipe is assigned to a single category name and description. 
    
<br /> 
  
# **Features**  
## **Existing Features** 

### **GENERAL FEATURES ON ALL PAGES :**  
   - Each page is fully responsive on all pages and has been designed to be extremely user-friendly.

   - **Navigation Bar** - On all pages of Ayo Recipes, there is a fully responsive navigation bar. When the brand logo in the upper left corner is clicked, it takes the user to the homepage. The menu items on the left collapse to a hamburger icon when the width of the website is reduced to a smaller device, such as a mobile device. The user can easily click the icon to view Ayo Recipes' side nav bar and swipe left to hide it.
      * When a guest user visits the site, they will notice the following menu items at the top right: (Recipes, Create Recipes, Login, Register ) 
      * Members who are logged in can access the following menu items: (Recipes, Profile, Tips & Tricks, Logout), which allow them to create, edit, and delete recipes as well as receive discounts on kitchenwares.
      * When an admin user logs in, they see the same menu items as registered users, but there is an additional menu item that states "Manage categories.".

   - **Flash Messages** - When a user performs a basic CRUD function, flash messages appear on all pages to provide feedback on the action they performed. 

   - **Recipe Card containers** - Throughout the site, recipe card containers have been used to display the recipe image, name, and description in an orderly and appealing manner. The user can view more information about the recipes by clicking on the images in the card

   - **Footer** - The footer section contains Ayo Recipes' social media handles, where users can learn more about them in order to build trust with the brand and confirm business legitimacy. It also includes some additional links to cooking-related information.

   - **Defensive back-end programming** - There has been some back-end defensive programming to prevent users from accessing pages/functions that they are not permitted to access. For example, when a user views a single recipe, they cannot see the " ORDER NOW " button but can see the "BACK" button; however, if the user registers/logs in, they can see the "ORDER NOW" button if they are viewing a recipe that was not created by them.  

   - **Modal** - A modal appears on some pages for the user to perform the delete functionality.

### **FEATURES OF EACH PAGE**     

   - **Home Page**

      The hero image is located beneath the responsive navigation bar and serves to draw the user's attention. The header text has a zoom in effect that welcomes the user to the site, as well as a static tag line text that is visually appealing. 

      Under the header is a festive container with a brief summary of Ayo Recipes and three recipe containers with the highest star-rated recipes.

      The recipe containers allow the user to view the various categories of recipes available on the site. The user can view each recipe by clicking on any of the category names. 

      Following the categories section, the user can scroll down to see where they can buy cheaper kitchen decors that make cooking much easier. 
      <br/>

   - **Recipes Page**   
     * **Search Bar** : There is a search bar in the centre of the hero image header. The search bar allows the user to look up any recipe name or category.   
     * **Search Icon** : The search icon button allows the user to query their search, which leads to the results of the user's query 
     * **Clear Button** : The clear button resets the search query, allowing the user to return to the database's list of recipes rather than a search.  
     * **Recipe Cards** : In alphabetical order, the recipe cards display all of the recipes created by our registered users. The user can view more information about any of the recipes by clicking on them.  
     * **Back Button** : A back button is present at the bottom of the recipes page. This is placed before the footer to allow the user to return to the home page if they want to interact with another page.   
  
   <br/>

   - **Create Recipe/Login Page**
      - This displays a card form container with the following information: 
         * **Input Fields**: This enables the user to enter the information required to log into their account, such as (username and password). 
         * **Login Button** : To login to their profile, the user must complete all required fields, and once completed, it logs the user into their profile.
         * **Register Here Link** : If the user does not have an account with Ayo Recipes, there is a link under the card form container that redirects the user to the register page.
   
   <br/>

   - **Register Page**
      * A card container is also included, as are some mandatory input fields. The following inputs would be required from the user:
         - Full Name  
         - Username
         - Password 
         - Confirm Password
         - Phone Number 
         - Email
         - About yourself
      * **Sign Up Button** : All of the above fields must be filled out in order for the button to take the user to their profile once registered . 
      * **Log In Link** :If the user already has an account, there is a "LOGIN" link under the card container that takes them to the login page. 

   <br/>  

   - **Profile Page**
   
      * When a user logs in or registers with Ayo Recipes, they are taken to their profile page and greeted. 
      * **Header Image** : A header image containing the user's username is present in a card container at the top of the page.
      A profile container with the user's personal information is located beneath the header image. The information displayed on the profile is the information provided by the user when they registered.
      * **Buttons** :To perform any of their desired functions, the user can click on any of the buttons under the profile details: "CREATE A RECIPE" or "UPDATE A PROFILE."
      The user can view all of the recipes that have been created by clicking on the buttons. If no recipes are present, the user will see the message "No recipes added yet“.

   <br/>
 
   - **Edit Profile Page**
      * When a user logs in to their profile, they can access this page. When the user clicks on the "UPDATE PROFILE LINK," they will see the following pre-populated input fields.The input fields can be edited and must be filled out in order for the user profile to be updated. The fields are as follows:
         - Username
         - Phone Number
         - About me 
         - Email
     * **Buttons** : There are two buttons under the edit profile form that either update the profile or redirect the user back to the profile page.  

   <br/>

   - **Create A Recipe Page**  
     * When the user clicks the "CREATE A RECIPE" button, the user is taken to an add recipe form, which the user must complete. The following fields must be completed: 
       - Recipe Name 
       - Recipe Description 
       - Insert Ingredients
       - Recipe Directions
       - Recipe time
       - Recipe category 
       - Is vegetarian 
       - Recipe image_url : If the user has a link to the recipe image, they can enter it in the provided space.
       -	Recipe rating 

     * **Buttons** : The form includes two buttons under the input fields: "SUBMIT" and "CANCEL." When the submit button is pressed, the user's profile is updated with a new recipe, whereas when the cancel button is pressed, the user is redirected back to their profile page.  
     
   <br/>

   - **Single Recipe Page**  

      When a user clicks on one of the recipe cards, they are taken to a single recipe page that contains all of the information for the individual recipes. 

      When a guest user views this page, they will notice a "BACK" button in the middle of the page content, which will take them to the login page.

      When registered users view single recipes that were not created by them, they will notice the "ORDER NOW" button in the middle of the page, which will take them to another site where they can conveniently order the meal if they do not feel like preparing the recipe being viewed.

      For registered users  viewing recipes created by them they can see two action buttons at the middle of the page. The two buttons are “EDIT RECIPE” & “DELETE RECIPE” .When the user clicks on the delete recipe button a modal appears to ask the user if they are sure of their action. If yes , the user can delete the recipe and if no, the user can click cancel and return back to the single-recipe page .  

      The admin user has access to all of the buttons that are available to registered users who have created recipes. The admin user has the ability to edit and delete recipes created by registered users as well as create new recipes.

      * **Back Button** : Under the single recipe content, there is a back button that allows the user to return to the recipes page.
   
   <br/>

   - **Edit Recipe Page** 

      * When a user clicks the "EDIT RECIPE" button, they are taken to the edit recipe page, which contains pre-populated input fields for the previously created recipes. Some of the pre-populated input fields, such as the following , can be edited.
         - Recipe Name 
         - Recipe Description 
         - Insert Ingredients
         - Recipe Directions
         - Recipe time
         - Recipe category 
         - Is vegetarian 
         - Recipe image_url : The user can update their recipe image

      * **Button** : Once the fields have been correctly filled out, the user can click on either the "EDIT RECIPE" or "CANCEL" buttons. When the "EDIT RECIPE" button is clicked, the recipe information is updated, and when the "CANCEL" button is clicked, the user is returned to the single recipe page.
    
   <br/> 

   - **Tips & Tricks Page**
      Tips & Tricks Page This page provides the user with everyday kitchen hacks that can be used to make the cooking process as simple as possible. The tips aspect has been divided into three sections, each with a brief summary of how the user can deal with the situation. Providing users with discount codes that can be used to purchase a variety of kitchenware hack items.
    
<br/>

   - **View Category Page**(Admin)  
     When a guest or registered user visits Ayo Recipes and navigates to the 'Browse our categories' section, they can click on the images or category names to view all of the recipes in that category.

      When a user visits the page, a header image with the Category name and a brief description of the category appears.

      If there are recipes in the category clicked, the user can see the recipe cards below the header image, but if there are none, the user sees the message "No category results found."

     * **Button** : There is a back button at the bottom of the recipe card that, when clicked, takes the user back to the home page.  
   
   <br/>

   - **Manage Categories** (only available to admin)  
     This page is only accessible to the site's Admin user. When an administrator logs in, they will notice the "MANAGE CATEGORY" option among the menu line items. 

      When the user clicks, they can see all of the categories that are currently available in our recipe database, which is represented by a card container. The category name and two buttons are included in the card container. The admin user can either "EDIT" or "DELETE" the category using the buttons. 

   <br/>

   - **Add Category Page** (only available to admin)  
     There is a 'ADD CATEGORY " button at the bottom of the manage category page that allows the admin to add new categories for the users. This takes the admin user to a new page where they must enter the following information:
       - A category Name
       -	Category description
   
      Before the admin user can add the category, these fields must be correctly filled out. If the admin user fills out the form correctly, he or she can click the "ADD CATEGORY" button, and the category will be added and the admin user will be redirected back to the manage category page.

      If the admin user does not want to add a new category, they can simply click the "BACK" button to return to the manage category page.

   <br/>

   - **Edit Category Page** (only available to admin)  
     The admin can change the category by clicking the "EDIT" button on the manage category page. When the button is pressed, the user is taken to the edit -category page, which contains a pre-populated form with the category name and description. 

      The admin user can update the pre-populated data, and once the fields are properly filled, the user can click the "Update category" button to update the data and return to the manage category page. If the user changes their mind after editing the category information, they can return to the manage category page by clicking the other button "CANCEL.

   <br/>

   - **Delete Category Page** (only available to admin)  
     To delete a category, the user can simply click the "DELETE" button on the manage category page. When the admin user clicks this button, a modal appears asking the user to confirm their action.  The user can delete the category name and description from the manage - category dashboard by clicking the delete button. If the answer is no, the user can cancel and return to the manage-category page.

   <br/>  

### **FEATURES TO IMPLEMENT IN FUTURE**  

1. Forgot password functionality: This would allow users to change their passwords if they forgot them without having to create a new account each time they forgot their password. 

2. Pagination : As the number of recipes in the database grows, pagination should be added to the recipes and view category pages for a better user experience. 

3. A save recipe function that allows registered users to save recipes created by other members to their profile would be ideal. The saved recipes would appear on the registered user's profile alongside recipes created by them.

4. Profile picture: When a user creates an account, there should be a dropdown of images from which the user can choose an Ayo Recipes profile image. When the image is selected and the user is logged in, the profile image and the user's name should appear at the top of the profile page.

5.  The admin user should be given more powers, such as the ability to manage user information by editing or deleting it.

6. A public profile page where registered users can view information about other members as well as recipes they've created. Users should be able to leave reviews on each other's profile pages if any of the recipes they created have been attempted.

7. An e-cart that allows users to order recipes directly from the page rather than through a third-party link. On their profile page, registered users can post recipes and sell food items.

<br/>   
  
# **Technology Used**
### **LANGUAGE USED** 
   * [HTML5](https://en.wikipedia.org/wiki/HTML5)   
   * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)   
   * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)   
   * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))   

### **FRAMEWORKS,LIBRARIES AND PROGRAM USED**   
   * [Materialize CSS](https://materializecss.com/): This was used to aid in the structure, style, and responsiveness of the website across all devices.

   * [jQuery 3.6.0](https://jquery.com/) : This is a JavaScript library that is used to help us write less JavaScript code.

   * [Fontawesome](https://fontawesome.com/) : This was used to convey information through the use of icons and to improve the site's appearance.

   * [Flask](https://flask.palletsprojects.com) : This is the python web application framework that is used.

   * [FIGMA](https://www.figma.com/) : This was used to create wireframes for Ayo Recipes (mobile and desktop devices).

   * [Google Fonts](https://fonts.google.com/) : For this project's design, the fonts Dancing Scripts and Poppins have been imported into the stylesheet.

   * [GIT](https://git-scm.com/) : This was the preferred version control method. We used the gitpod to commit and publish our project to GitHub.

   * [GITHUB](https://github.com/) : This was where the project's code was store.

   * [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/) : This serves as a communication link between Flask and PyMongo.

   * [Jinja](https://jinja.palletsprojects.com) : This is a Python templating language that is used to display backend data in the frontend.

   * [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security) : Werkzeug was used for password hashing and authentication. 

   * [Favicon.io](https://favicon.io/favicon-converter/) : This is a Favicon generator that was used to create our Ayo Recipes favicon.  

   * [JSHint](https://jshint.com/) : This was used to analyse the JavaScript code and ensure that all errors were reduced to a minimum. 

   * [PEP8](http://pep8online.com/) : This was used to run our Python code to ensure it was error-free.

   * [CHROME DEV TOOLS]() : This was used to test the responsiveness of our website across various screen devices.

   * [Heroku](https://en.wikipedia.org/wiki/Heroku) : This was the preferred cloud platform for deploying our project, which hosts our Python project Ayo Recipes.

   * [MongoDB](https://www.mongodb.com/) : This is a document-based database where we keep our Recipe database.

   * [Werkzeug](https://pypi.org/project/Werkzeug/) : This was used to hash passwords and authenticate users.

   * [TinyPNG](https://tinypng.com/) : This is an image compressor that is used to compress all images


# **Testing**  
The testing documentation can be found [here](https://github.com/dissyulina/cookle-cookbook/blob/main/TESTING.md#cookle---testing). 

<br/>   
  
# **Deployment**   
This project was created with Gitpod as the IDE and is hosted on Github because Github Pages cannot host a Python project. This project was deployed using a free hosting service (Heroku).  

## **Deployment to Heroku**   
There are two ways to deploy to Heroku either by:   
- Pushing our code to the Git URL  that Heroku provides or 
- Linking our GitHub repository to Heroku.   
The second method was applied to deploy this project.   

1. **Create a new Heroku App**   
   * Sign in or create an account with Heroku. Select "Create new app" in the top right corner of your dashboard after logging in   
   * Provide a unique app name and use a hyphen between words.   
   * Choose a region that is close to you and then click Create App.  

2. **Create the following important files**   
   * Return to your project's Gitpod IDE and create a gitignore and an env.py file.
   * The env.py file would contain all of the environment variables required to connect our MongoDB database to our Heroku App.
   * To hide the sensitive information it contains, such as the secret key and our unique mongo DB URI, the env.py file must be added to the gitignore file.
   * Make a file called **"requirements.txt"** that contains a list of all the Python dependencies for our project. This tells Heroku what language is being used. To make this file, type the following into the terminal.   
      ```pipi3 freeze --local > requirements.txt```   
   * Next, in the terminal, type the following to create a "Procfile" that instructs Heroku on how to run our project:   
      ```echo web: python run.py > Procfile```
   * This tells Heroku that our application will be a web process, and the command to run it is **"python app.py."**  

3. **Link our Git repository to Heroku**   
   * Return to our Heroku Dashboard and choose "deploy" from the top options. 
   * Select "GitHub" from the deployment method from section.   
   * This gives you an input field where you can search for your GitHub repository by name. When the correct repository, in our case "Ayo Recipes," is found, click "Connect."   
   * After that, we need to set up the necessary environment variables in our Heroku App's env.py file.
   * Click "Settings" on the Heroku Dashboard and then the "Reveal Config Vars" button.
   * The following key value pairs should be  added:   
      |Key|Value|
      |----|----|
      |IP|0.0.0.0|
      |PORT|5000|
      |SECRET_KEY|```<your_secret_key>```|
      |MONGO_URI|```mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority```|
      |MONGO_DBNAME|```<database_name>```|
      
4. **Enable Automatic Deployment**   
   * Return to the dashboard and click "Deploy" once we've configured our environment variables. Scroll down to "Automatic Deployments" and click "Enable Automatic Deployment."  
   * We have the "Manual deploy" section under "Automatic deploys." From our main branch, click the "Deploy Branch" button.   
   * Once this is completed, Heroku will build our app with all of the necessary packages. To view the website, go to the top right corner and select "Open App". 


### **STEPS TO USE THIS PROJECT** 
The MongoDb atlas was used to store the data in this project. The steps below were taken to create our database and connect it to our Heroku App.

### **1. Create database on MongoDB**  
1. **Set Up MongoDB**   
   * To begin visit the mongoDB website and creating an account/login.
   * Create a cluster by selecting a shared cluster once you've logged in.
   * Choose a cloud provider. AWS was chosen for this project and is ideal for its requirements.
   * When that option is selected. Choose a "Cluster Tier" and the M0 Tier (Free forever tier).
   * Once you've completed all of the preceding steps, click the "Create Cluster" button.
   * To create our database user credentials, navigate to 'Database Access' under the Security section on our mongoDB dashboard.
     - Create a username and password using the default SCRAM authentication method by clicking 'Add New Database User.' (It is recommended that you use a combination of letters and numbers to avoid any problems.  
     - The username and password that we specify here will be used in our MONGO URI environment variable  
     - Finally, configure the "Database User Privileges" to allow read and write access to any database, and then click "Add User."  
   
   * After we've added the user, Go to the dashboard's Security menu and select "Network Access" to whitelist our IP address and ensure that it has access to our database.    
   *  Select "Allow Access from Anywhere" after clicking "Add IP Address." Normally, you would enter your website's IP address, but we chose this option because the database will be accessed via our gitpod workspace and Heroku
   * Then press the "Confirm" button.

We can now create our database after we have set up MongoDB. The database was built using the Ayo Recipes [Data Scheme](static/images/readme/database-schema.png "Database schema").    

2. **Create database**    
   * Select the Cluster tab, then select the "Collections" button.  
   * Since we aren’t uploading an existing dataset, select "Create Database."  
   * Provide the name of your database and one initial collection that will be used for your project. 
   * After we've done that, we can add more collections to our database by clicking the "Create Collection" button.
   * We can manually create a document by selecting one of the collections and clicking the "insert document" button in the upper right corner. 

### **2. Fork or Clone The Github Repository**   

#### **Forking The GitHub Repository**  
By forking the GitHub repository, we create a clone of our original repository (AYO RECIPES) in our GitHub account. By cloning our project we can make  modifications and experiments on the cloned repository without affecting the original repository.   

1. Sign In to GitHub account .  
2. Decide from the list of repositories which you would want to be duplicated. For this project it's AYO RECIPES .  
3. Locate the "fork" option at the top right corner of the AYO RECIPES and click it. Once clicked it creates another copy of the AYO RECIPES repository to accommodate modifications.  

#### **Making A Local Clone**     
1. Log in to your GitHub account.
2. Locate the desired repository to clone which in this case is “AYO RECIPES” .
3. At the top of AYO RECIPES repository page,  Locate the “Code” button at the top  and click it. Copy the HTTPS link that appears.
4. Activate your local IDE terminal.
5. In the terminal, type “git clone” and then paste the link copied from HTTPS.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
6. Press “Enter” and your local clone has been created.


# **Credits**  
### **CONTENT**  
1. The site's design was inspired by extensive research conducted on recipe sharing websites such as [yummly](https://www.yummly.co.uk/), [bbcgoodfood](https://www.bbcgoodfood.com/) , [epicurious](https://www.epicurious.com/) and other MS3 peer's project(slack channel).  

2. Photoshop was used to create the Ayo Recipes brand logo.
      
3.	The animation effect used on the hero image header text was obtained from the [CSS tricks](https://css-tricks.com/almanac/properties/a/animation/)  website. 

4. Abdul Basit's [Youtube](https://www.youtube.com/watch?v=MLBLsxcB3Dc) assistance was used to create the dynamic form fields in the add-recipe page code.

5. The code from Code Institute's mini project lesson on Task Manager Application was primarily used as a reference and guide for developing the basic CRUD (Create, Read, Update, and Delete) functionalities for this project. 

6. Another peer's [project](https://github.com/dissyulina/cookle-cookbook/blob/main/app.py#L433) here at code institute provided code assistance for the creation of the edit profile and add recipe functions.

7. Research on StackOverflow and Jinja documentation aided in the creation of some  Python functions and the application of the Jinja template. 

8. [Code pen](https://codepen.io/t_afif/pen/eYWJNBd) was used to generate the html and CSS code for the star rating applied on the add recipe page.  

9. The code for the star rating on the single page was also obtained from another peer's project here at [code institute](https://github.com/mosull20/dark-side-ms3/blob/main/templates/profile.html) which aided in the design.

10. The code used to force resize some images while maintaining the same aspect ratio was obtained from [stackoverflow](https://stackoverflow.com/questions/12991351/css-force-image-resize-and-keep-aspect-ratio). 

11. The external links relating to kitchenware discounts included in the tips & tricks page were obtained [Countryliving](https://www.countryliving.com/food-drinks/g32869067/chef-pantry-staples/?slide=1), [Delish](https://www.delish.com/food/a52476/kitchen-pantry-organization-ideas/) , [Buzzfeed](https://www.buzzfeed.com/michelleno/cooking-tips-for-beginners) and [Bbcgoodfood](http://www.bbcgoodfood.com/). 

12. Majority of the recipes added to the AYO Recipes database come from recipe sharing websites like [yummly](https://www.yummly.co.uk/), [delicious](delicious.com.au), [bbcgoodfood](https://www.bbcgoodfood.com/) as do the recipe images.

13. This readme was based on research on several readme documents, including the Code Institute's readme [sample](https://github.com/Code-Institute-Solutions/SampleREADME), the dark side's readme [sample](https://github.com/mosull20/dark-side-ms3#deployment),  Cookle's readMe's [sample](https://github.com/dissyulina/cookle-cookbook#deployment-to-heroku), FLYBOY's readMe [file](https://github.com/Didisimmons/LILELI-QUIZ-GAME/blob/main/test.md) and LILELI's readME's [file](https://github.com/Didisimmons/LILELI-QUIZ-GAME/blob/main/readME.md).

 
### **MEDIA**   
* The majority of the images on the website were obtained from image free providers such as [unsplash](https://unsplash.com/), with the exception of the food recipe images, which were obtained from [Bbcgoodfood](http://www.bbcgoodfood.com/) and [delicious](delicious.com.au).

* The homepage's hero image is a photo by Brooke Lark from [unsplash](https://unsplash.com/photos/of0pMsWApZE).

* Ryan Christodoulou from [unsplash](https://unsplash.com/photos/68CDDj03rks) provided the kitchen decor image used at the bottom of the homepage to depict the proper kitchen décor.

* The homepage's "Browse our categories" section is divided into four categories, and the images used were obtained from the following people: 
   - Breakfast Recipes – Photo by Brooke Lark  from [unsplash](https://unsplash.com/photos/W9OKrxBqiZA).

   - Snack Recipes  – Photo by Honey Fangs from [unsplash](https://unsplash.com/photos/-JU0sqGjeC0).

   - Soup Recipes  –Photo by Ella Olsson from [unsplash](https://unsplash.com/photos/fxJTl_gDh28).

   - Main Dish Recipes – Photo from Amna Akram from [unsplash](https://unsplash.com/photos/KIL9suHFp6s).

   - Default category image – Photo from Toa Heftiba from [unsplash](https://unsplash.com/photos/tE9Ovti1gRI).

* Some pages, such as the register page, profile header, and add recipe container, now have a background photo that was created in Photoshop

* The following people provided photos for the tips and tricks page:
   - Pantry Essentials – Photo by Jason Leung from [unsplash](https://unsplash.com/photos/jWU9FpLW7fI)

   - Essential Kitchen Gadgets – Photo by Kevin McCutcheon from [unsplash](https://unsplash.com/photos/APDMfLHZiRA).

   - Cleaning Pots & Pans – Photo by  Precious Plastic Melbourne from [unsplash](https://unsplash.com/photos/n5qirFAe6rQ).

*	The images for the recipes were sourced from [yummly](https://www.yummly.co.uk/recipe/Eggs-Benedict-2635676) ,[delicious](delicious.com.au) and [bbcgoodfood](http://goodfood.com/recipes/blackened-roast-salmon-avocado-mango-salsa). 

<br/>  

# **Acknowledgements**   
   * I'd like to thank my mentor, Sammy Dartnall, for her constant encouragement and constructive feedback on this project.  
   * The tutor support team for answering all of my questions and providing helpful problem-solving guidelines.  
   * Code institutes the Slack community as a valuable resource where students can interact and help one another, as well as Stack Overflow for guidance and constant support.

<br/> 