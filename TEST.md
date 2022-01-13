# AYO RECIPES 

[Back To Main README File](README.md)

[View The Deloyed Site](http://ayo-recipes.herokuapp.com/)

## TESTING
<br/>

**Table of Contents** 
1. [Validator Testing](#validator-testing)  
   - [HTML](#html)   
   - [CSS](#css)
   - [JAVASCRIPT](#javascript)
   - [PYTHON](#python)

2. [User Stories Testing](#user-stories-testing)  
   - [UNREGISTERED USER GOALS](#unregistered-user-goals)   
   - [REGISTERED USER GOALS](#registered-user-goals)  
   - [ADMI USER GOALS](#admin-user-goals)  
    
3. [Manual Testing](#manual-testing)   
   - [HOMEPAGE AS A GUEST](#homepage-as-a-guest-user)   
   - [RECIPES PAGE](#recipes-page)   
   - [LOGIN](#login-page)   
   - [REGISTER](#register-page)  
   - [SIDE NAVIGATION BAR](#side-navigation-bar)
   - [TIPS & TRICKS](#tip-tricks-page)  
   - [REGISTER](#register-page)     
   - [PROFILE](#profile-page)
   - [ALL ADD FORMS](#all-add-forms)
   - [ALL EDIT FORMS](#all-edit-forms)
   - [ALL DELETE FORMS](#all-delete-forms)

4. [Defensive Programming](#defensive-programming)

5. [Lighthouse Testing](#lighthouse-test)

6. [Further Testing](#further-testing)

7. [Solved Bugs](#solved-bugs)

   
<br/>

### **VALIDATOR TESTING**
#### **HTML**
* [W3C Markup Validation](https://validator.w3.org/): This is also used to validate the HTML code for all newly created webpages. Our code was discovered to have some errors as a result of the jinja template used when you paste the direct html code. However, this was resolved by obtaining the source code by right-clicking on our page and selecting "View page source." The errors are removed when checked again. 
* [Homepage](static/images/readme/html/homepage.png) 
* [Profile](static/images/readme/html/profile.png) 
* [Recipes](static/images/readme/html/recipes.png)  
* [Tips & Trick](static/images/readme/html/tips&tricks.png)  
* [Manage Categories](static/images/readme/html/manage-categories.png)  
* [Add Category](static/images/readme/html/addcategory.png)  
* [Edit Category](static/images/readme/html/edit-category.png) 
* [Single-recipe](static/images/readme/html/single-recipe.png)  
* [Login page](static/images/readme/html/login.png)
* [Edit profile](static/images/readme/html/edit-profile.png)
* [View_category](static/images/readme/html/view_category.png)
* [Register](static/images/readme/html/register.png)
* [Add Recipe](static/images/readme/html/addrecipe.png)
* [Edit Recipe](static/images/readme/html/edit-recipe.png)

<br/>

#### **CSS**
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/): This is used to validate the CSS code used on all webpages created. Our code is found to be error-free by the validator.

![css_validation](static/images/readme/test/css-validation.png)

<br/>

#### **JAVASCRIPT**
* [JSHint validation ](https://jigsaw.w3.org/https://jshint.com/): This was used to validate the JavaScript and Jquery code used on Ayo Recipes to ensure that it was error-free. The script.js file was added to all pages, and the addscript.js file was added to the recipe add/edit page. It was discovered that some semi-colons were missing when this was first run. This was fixed by inserting the necessary semicolons.

![JSHint validation for script.js](static/images/readme/test/jshint-validation.png "JSHint validation for script.js")
![JSHint validation for addscript.js](static/images/readme/test/jshint-validation2.png "JSHint validation for addscript.js")

<br/>

#### **PYTHON**
* [Pep8 Online validator](http://pep8online.com/): This was used to run our Python code in the app.py file to ensure that all errors were removed, such as whitespace, trailing whitespace, and so on. When this was run through the validator, it was discovered that there were some whitespaces that were removed. 

![Pep8 Online validation](static/images/readme/test/pep8-validation.png "Pep8 Online validation")

<br/>

### **USER STORIES**
#### **Unregistered User Goals**   
As a new/ unregistered user, I want to:
1. Easily understand the purpose of the site and how it works.

When a user arrives at the home page, the header image welcomes them to the site, capturing their attention and keeping them interested in the site. The user can easily scroll down to see a summary of Ayo Recipes, what it entails, and what to expect when visiting the site.  
   ![Home page](static/images/readme/test/fig1.png "landing page")

There is a fully responsive navigation bar that the user can hover over. A white box shadow appears over the menu line items when the user hovers over the menu.
    ![Home page menu navigation bar](static/images/readme/test/fig2.png "Home page menu navigation bar")

The website has been designed to be extremely user-friendly. When a user clicks on one of the links, he or she is taken to the desired page. When a user performs any of the basic CRUD functions, such as registering with Ayo Recipes, a flash message appears informing them of their action.
    ![flash message from register page](static/images/readme/test/fig3.png "user account ")

2. View all the recipes available with directions on how to prepare and cook the recipe.

When the user hovers over and clicks the recipe menu option. The user is directed to the recipes page, which displays all of the Ayo database's recipes.

![recipes page](static/images/readme/test/fig4.png "recipes page ")

The user can view more information about the recipes individually by clicking on any of the recipe cards. When the user clicks, he or she is taken to a single recipe page that displays all of the information about a specific recipe (cooking ingredients and directions).

![single-recipes page](static/images/readme/test/fig5.png "single recipes page ")

When a user clicks the "Back button" in the middle of the page, they are directed to the Login page, where they can log into their profile, create a new recipe, and order any of the recipes created by other registered users.

![single-recipes page](static/images/readme/test/fig6.png "single recipes page ")
    

3. Easily search for recipes and be able to view the full details of the recipe interested in.

The user is presented with a search bar on the recipes Page, which is located in the middle of the header image. The search bar contains the search icon, which allows the user to query their search, and the clear button, which allows the user to cancel the search. 
The user can search for recipe or category names, which will return results if the recipe/category name is found.

![search for recipe](static/images/readme/test/fig7.png "search for recipe on recipe page ")

![recipe found](static/images/readme/test/fig8.png "recipe found ")

The user can reset the search query by clicking the "CLEAR" button, or they can return to the home page by clicking the "BACK" button at the bottom of the page.

4. Easily locate the call to action buttons on the site to allow the user either register or Sign up 

When a user visits the homepage, the register and Login buttons appear on the navigation bar and, when clicked, direct the user to either the register or Login page. 

The "Create Menu" option in the navbar also takes the user to the login page, because in order to create a new recipe, the user must first register with Ayo Recipes.

![menu bar for get user](static/images/readme/test/fig9.png "menu bar foor guest user ")


#### **Registered User Goals** 
As a returning/ registered user, I want to:
1.	Easily Log  into my profile dashboard to explore recipes made by me.

When a user arrives at the home page, he or she can either register to create a profile or log in by clicking on any of the menu options shown in the image above. When a user logs in, they are taken to their profile, where they are greeted, as shown below. When the user is a guest, the menu bar looks different.

![proifle greeting user](static/images/readme/test/fig10.png "proifle greeting user ")

If the user hasn't created any recipes yet, the text "No recipes added Yet" will appear under the user's personal information, as shown in the image above. If the user clicks the "Create Recipe" button, they will be taken to the add recipe page, where they can add a new recipe. Once this has been added, the user can view the recipes that have been added by them on their profile in the form of a card. See the list below.

![add recipe in profile](static/images/readme/test/fig11.png "recipe in profile page ")

2.	Easily search for recipes either by recipe name or the recipe category.

When a user is logged in, they can view all of the recipes at Ayo Recipes by going to the homepage or the recipes page. 
If the user wants to search for recipes by category names, they can easily do so by clicking on the images or category names on the index.html page.

![browse categories](static/images/readme/test/fig12.png "browse categories in profile ")

This takes the user to the "view category.html" page, where they can see all of the recipes in that category.

![view categories page](static/images/readme/test/fig13.png "view categories page ")

The user can also view all of the recipes on the website by selecting the "recipes" menu option. The present search bar can be used to query the user's searches. The user can conduct a search using either the recipe name or the category name. The user is notified if no results are found. See the following:

![No results found in the search engine](static/images/readme/test/fig14.png "No results found in the search engine")


3. Be able to create my own recipe and share on the site. Edit it’s content and delete if the case need be. 

When the user logs into their profile, two buttons appear under their personal information. These two buttons allow the user to "Create Recipe" or "Update Profile." When a user clicks the "Create Recipe" button, they are taken to the add recipe page, where they can add a new recipe. If the user clicks the submit button, the recipe is saved to their profile; if the user clicks the "Cancel" button, they are returned to their profile page. 

![add recipe](static/images/readme/test/fig15.png "add recipe")

Once the recipe is added, the user's profile will be updated with all of their recipes, as shown in the images above.

![add recipe to profile](static/images/readme/test/fig16.png "add recipe to profile")

To learn more about the recipe, the user can click on the recipe card, which takes them to the single-recipe.html page.

![view single recipe created by user](static/images/readme/test/fig17.png "view single recipe created by user ")

When the user views the recipe they created, they will notice the "EDIT" and "DELETE" recipe buttons, allowing them to perform either function. When a user clicks the "EDIT" button, they are taken to the "edit-recipe.html" page, which displays a form field with prepopulated data containing the recipe details. When finished, the user can update the fields of their choice by clicking the "Update Recipe" button. If they want to cancel the update, they can do so by clicking the "CANCEL" button and then being diverted back to the single -recipe page.

![edit recipe created by user](static/images/readme/test/fig18.png "edit recipe created by user ")

If the user changes the fields and then clicks the "Update Recipe" button, a flash message appears and the user is redirected back to their profile page, with a feedback at the top.

![flash message for update ](static/images/readme/test/fig19.png "flash message for update")

If a user wants to delete a recipe, they can do so by clicking the "DELETE" button on the single-recipe page. When the button is clicked, a modal appears asking the user to confirm their action.

![modal for delete ](static/images/readme/test/fig20.png "modal for delete")

The user can confirm their decision to delete the recipe by clicking the "DELETE" button, or they can return to the single recipe page by clicking "CANCEL." If the delete button is pressed, the recipe is deleted, and the user is notified that their action was successful.

![recipe deleted feedback ](static/images/readme/test/fig21.png "recipe deleted feedback ")


4. Easily edit my personal profile in case changes are needed.

The user can update their personal information in their profile by clicking on the "UPDATE PROFILE" button, which takes them to the edit-profile page. The edit-profile page contains the user's prepopulated data, allowing the user to easily make changes to any fields.

![edit profile](static/images/readme/test/fig22.png "edit profile ")

After updating the fields, the user can either click "UPDATE PROFILE" or "CANCEL." If the user clicks the "UPDATE PROFILE" button, they will receive confirmation that their action was successful.

![profile updated ](static/images/readme/test/fig23.png "profile updated ")

If the user does not want to update their profile information, they can click the "CANCEL" button and be taken back to their profile page, which displays all of the recipes they have created.


5. Be able to order recipes online

If the user is registered or has an account with Ayo Recipes, they can order recipes online. After logging into their profile and visiting the home page, the user can see the "ORDER NOW" button by clicking on any of the recipes created by other users. This takes the user to a third-party site where they can order the recipe takeaway directly. 

![view single recipe created by other users](static/images/readme/test/fig24.png "view single recipe created by other users")

If the user is viewing a page that they created, the buttons that appear on the single-recipe page are different, with the "edit" and "delete" buttons present due to some defensive back end programming.


#### **Admin User Goals**
As an Admin User, I want to:

1.	Be able to do all the functionalities assigned to a registered user.

When an administrator logs into Ayo recipes, they see the same menu navigation bar as a registered user. The admin user has access to all recipes and can search for them. Like a registered user, the admin user can create a recipe and edit their profile.

![admin profile ](static/images/readme/test/fig25.png " admin profile")

The buttons that appear for a user who created a recipe appear on the single -recipe page when the admin user wants to view each recipe card to see more information about each recipe. All recipes created by users can be edited and deleted by the admin user. The recipe below, for example, was created by a user named "Heidi," and the admin user has access to all functions as Heidi.

![admin user viewing single recipe page ](static/images/readme/test/fig26.png " admin user viewing single recipe page")

2. Restrict access for certain features that can only be accessed by the admin. 

When the admin user logs in to Ayo Recipes, they can see all of the menu items that the registered user can see, but there is an additional menu item "MANAGE CATEGORIES" that is only available to the admin user. 

![menu bar for admin user ](static/images/readme/test/fig27.png " menu bar for admin user")

The admin user also has access to all recipes created by users, allowing the admin user to edit or delete each recipe's information.


3. Add, Edit, or Delete the category of recipes present.

When an administrator logs into Ayo Recipes, the menu item "MANAGE CATEGORIES" allows the administrator to add a new category, edit existing categories, and delete any unwanted categories.

![manage category page ](static/images/readme/test/fig28.png " manage category page")

When the admin clicks the "ADD CATEGORY" button, the user is taken to the add-category page, where the admin can enter the category name and description.
 
![add new category page ](static/images/readme/test/fig29.png " add new category page")

The category would be added to the manage-category page if the user clicked the "ADD CATEGORY" button.

![new category added displaying flash message ](static/images/readme/test/fig30.png "new category added displaying flash message")

If the admin user wants to delete the newly added category, they must click the "DELETE" button, which will open a modal asking the admin user to confirm their action. 

![delete category ](static/images/readme/test/fig31.png "delete category")

The new category would be removed once the admin user confirms their action and clicks the delete button.

![ category deleted with feedback ](static/images/readme/test/fig32.png "category deleted with feedback")


4. Be able to edit , delete and update any recipes listed on the site.

When an admin user logs into their profile, they can see the same buttons that a registered user sees, which are "create recipe" and "edit profile." 
The admin user has the ability to create new recipes as well as edit existing recipes on the website that were created by other users. The admin user has the ability to delete all of the recipes created by different users.

![ single recipe page ](static/images/readme/test/fig33.png "single recipe page")


### **MANUAL TESTING**

#### TESTING ALL FEATURES ON EACH PAGE 

#### **HOMEPAGE AS A GUEST USER** 

 1. Navigation bar 

     1. Navigate to the Index page (Home) on a desktop by clicking the Ayo Recipes brand logo in the upper left corner. 

     2. Change the desktop's screen size to that of a tablet device to ensure that the navigation bar is responsive and changes to a hamburger icon as the screen width decreases to that of a tablet or mobile device. The navigation bar should be fixed, and menu items should be hidden in the side navigation bar that appears on medium to small devices.

         When testing responsiveness across different devices, there was no overflow of the navbar. On a tablet and a mobile device, the navigation bar menu changed to a hamburger icon, and the menu items were displayed in the side navigation as expected. The menu items are in place, and the navigation bar is fixed, with the brand logo image in the centre.

    3. Hover your mouse over the navbar menu items and click on each link to ensure that you are taken to the correct page.

          When tested on all devices, the menu links work as expected. The user is directed to the appropriate sites, which are recipes, login and the registration page for a guest user.

    4. Hover over the menu items to ensure that a white background overlay appears with a box shadow on the white background when the mouse is hovered.

         When testing the effect on a desktop device by hovering the mouse over the menu item in the navigation bar, the white backdrop appears with a box shadow when the mouse is hovered over the menu item.

    5. When you click on the Ayo Recipes logo, make sure it takes you to the home page. 

         When tested on all devices by adjusting the screen width, the brand logo for Ayo Recipes actually takes the user to the home page when clicked.

    6. On a tablet or mobile device, ensure that the Ayo Recipes Brand Logo is centred on the navigation bar.

         When the device's screen width is reduced to that of a tablet or mobile device, the Ayo Recipes Brand Logo is centred on the navigation bar, as expected.

    7. Change the screen size to that of a tablet or mobile device and verify that the side navigation appears when the user clicks the hamburger icon. The menu items should be displayed in the side navigation. Additionally, ensure that the menu links from the hamburger icon have a background overlay when hovered over and that they all lead to the appropriate pages.

         When the width of the navigation bar is changed to that of a tablet device, the hamburger icon appears as expected. When you click the hamburger icon, a side navigation bar menu appears, displaying the menu links. When hovered, the menu links have a white background overlay and link to the appropriate pages when clicked. The menu items have been centred to improve the appearance of the navigation bar on a tablet and mobile device. When the image brand logo is also clicked, the user is taken to the homepage. 

         ![ side navigation ](static/images/readme/test/fig34.png "side navigation")


2. Hero image  

    1.	Navigate to the Index page (Home) on a desktop by clicking the Ayo Recipes brand logo in the upper left corner. 

    2. Check that the hero image is visible and occupies the entire width of the screen on all devices.

         On a desktop, the hero image fills the entire screen width with no overflow issues. When the screen size is changed to a tablet or mobile device, the same effect occurs; the hero image takes up the entire screen width.

    3. Confirm that when the home page (index page) loads on all devices, the hero image text header has an animation effect and that the tagline text is hidden on all small devices such as mobile.

         The hero image text header has a stretch animation effect when tested on a desktop device. The same thing happens on a tablet and a mobile device. However, certain text in the hero image, such as the tagline text, is hidden on a mobile device to keep the mobile screen clean and visually appealing.

         ![ mobile view of hero image ](static/images/readme/test/fig35.png "mobile view of hero image")

3. Explore Festive section    

    1. Navigate to the Home page, which is the Index page on a desktop.
     
    2. Confirm that the brief summary of Ayo Recipes and the three recipe cards below the summary adjust responsively as the screen width changes .From a medium breakpoint point upwards, the recipe cards should occupy three columns per row, whereas on a smaller device, such as a mobile, the recipe cards should only occupy one column per row. 

         When tested on a desktop device, the festive container adjusts to fit the width of the screen. On a tablet device, the recipe cards appear as expected.
         
         ![ festive recipes with high ratings ](static/images/readme/test/fig36.png "festive recipes with high ratings")
         
         When viewing the recipe cards on a mobile device, they appear on top of each other, one card per row, as expected. The font size and images adjust as needed, and are responsive on all devices.

         ![ festive recipes with high ratings on mobile view ](static/images/readme/test/fig37.png "festive recipes with high ratings on mobile view ")

    3. Confirm that the recipe card container design includes a picture, a title, and some engaging text. When the screen width is changed, the recipe cards should change to fit the size of the screen, with the fonts also changing to fit the size of the screen. On a mobile device, each container should take up the entire width of the screen, yielding one recipe card per row.

        When tested on a desktop device, the recipe card container contains an image, title, and engaging text that is responsive to the screen as it is changed in the dev tools. The font size is also screen-responsive. The same effect occurs on a tablet device, where the recipe cards adjust responsively to the screen width, fitting well on the screen. When viewed on a mobile device, the three recipe cards appear on top of each other, occupying the entire screen width, creating a clean and visually appealing appearance.


    4. Hover your mouse over the image of the recipe cards and confirm if the alt text appears.

         When the mouse is hovered over the images, the alt text appears as expected.

    5.	Confirm that the recipe cards displayed on the index page in the “Explore festive section ” are sorted by recipes with high ratings.. 
    
        Clicking on each of the recipe cards demonstrates that the recipes displayed in the festive container have high ratings. The recipes with the highest ratings appear first.



4. Browse our Categories Section 
   
    1. Navigate to the Home page, which is the Index page on a desktop.

    2. Confirm that the categories have been divided into four distinct image pills, each with its own heading text. The image pills should adjust to the screen size so that they look good on all devices. 

         When tested on a desktop device, the categories occupy two rows, with one row containing two images and two heading text of the category names. When the screen width is changed to a tablet device, the image pills retain their structure, but the images and font size adjust to fit the size of the screen, making it visually appealing to the user.

         ![ category section  ](static/images/readme/test/fig38.png "category section ")

         ![ category section mobile view](static/images/readme/test/fig39.png "category section  mobile view ")

    3. Hover your mouse over the image pills in the category to see the alt text.

         When tested, the alt text is visible when the mouse is hovered over the image.

    4. Confirm that when the category image pill is clicked or the header text beside the image pill  is clicked the user is directed to the correct page. 

         Confirm that the user is directed to the correct page when the category image pill or the header text beside the image pill is clicked.

         ![ view category page tablet view](static/images/readme/test/fig40.png "view category page tablet view ") 
    
5. Kitchen Décor 

    1. Go to the Home page (the Index page on a desktop) and scroll down to the page. 
       
    2. Ensure that the image is responsive on all devices and that the font size adjusts to fit the width of the screen.

        When tested on a desktop device, the image is responsive. As the screen width is reduced, the image, as well as the font used on the text, shrinks. On a mobile device, the text appears above the image to fit the size of the screen and appear clean and organized and less clustered.

         ![mobile view oof kitchen decor image](static/images/readme/test/fig41.png "mobile view oof kitchen decor image ")   


    3. Confirm that the button under the kitchen décor text enlarges when hovered over and directs the user to the correct page when clicked.

        When this is tested, it can be seen that when the button is hovered over, a light box shadow appears on the button. When the button is pressed, a new page appears, which directs the user to the third-party site as expected.

        ![kitchen decor buy now button](static/images/readme/test/fig42.png "kitchen decor buy now button")

6. Footer 

    1. Navigate to the Home page, also known as the Index page on a desktop, and scroll down to the footer.

    2. Adjust the screen width of the device to see if the footer content is responsive. Check that the image in the desktop footer is hidden on a mobile device.

         When tested on a desktop device, the footer content is displayed in three columns, with the text in each column visible as expected. The second column contains the brand image logo, which, when clicked, takes the user to the website's homepage. As the width of the screen changes, the footer content adjusts to fit. The text and icons have been shrunk in size. However, on a mobile device, the second column with the brand logo is hidden, making the footer appear cleaner and less crowded.


    3. Hover your mouse over the social media icons in the third column of the footer section to see if they have a background overlay. 

        When testing this on all devices and hovering over the social network icons, each icon has a background overlay with a box shadow when hovered. This informs the user of which icon is currently selected. The outcome is as expected.

        ![hover effect on social media icons](static/images/readme/test/fig43.png "hover effect on social media icons")

    4.	Ensure that clicking on the social media icons takes you to the correct page.

         When tested by clicking on the social media links in the footer, it is clear that all of the social media icons, as expected, lead to Ayo Recipes social accounts.

    5.	Confirm that the links in the first column of the footer take the user to the correct page and that when hovered over, a box shadow appears. 

         Hovering the mouse over the links on a desktop or tablet device reveals that the box shadow appears as expected. When the user clicks on any of the links, he or she is taken to the homepage, as expected.  

         ![hover effect on footer links](static/images/readme/test/fig44.png "hover effect on footer links")

 
    6. Confirm that the brand logo in the footer has an  alt text when hovered and links to the home page when clicked.

         When tested on a desktop device, the alt text appears when the mouse is hovered over the image, and when the user clicks the brand image, they are directed to the homepage as expected.

<br/>

#### **RECIPES PAGE** 
1. Navigation bar 

    1. Navigate to the Recipes page on a desktop computer.
        
    2. Confirm that the guest users menu item corresponds to the guest user's home page navigation bar.
 
        When tested on all devices, the menu item for the recipe page is the same as the home page for the guest user.

    3. Confirm that the menu item for the recipe page when the user is logged in differs from the menu item for the homepage when the user is a guest.

        By logging into Ayo Recipes, it is possible to see that the navigation menu items are different. When logged in, the user has access to the following menu items (Recipes , Profile, Tips & Tricks & Logout).

        ![menu bar for a logged in user ](static/images/readme/test/fig45.png "menu bar for a logged in user")


2. Hero image
    1. Navigate to the Recipes page on a desktop computer.

    2.  Ensure that the hero image is visible and occupies the entire width of the screen on all devices, with a search bar in the centre of the image.

         On a desktop, the hero image fills the entire screen width with no overflow issues. When the screen size is changed to a tablet or mobile device, the same effect occurs; the hero image takes up the entire screen width. As the screen width is changed, the search bar appears in the middle of the page. The search icon and the clear button are present as expected, adjusting to the size of the screen to accommodate all devices.

    3. Confirm that when a user queries the search with a recipe or category name, the results are displayed and that if no results are found, a message informing the user is displayed.

         When tested across all devices, the search bar does query the user's search after the user enters a recipe name/category name, displaying results. If no results are found, the user will receive a message.

        ![no results found in recipe page ](static/images/readme/test/fig46.png "no results found in recipe page ")


3. Recipe card containers

    1. Go to the Recipes page on a desktop/ mobile device.

    2. Confirm that the recipe cards present under the header image are divided into three equal columns with card container designs. The design of the recipe cards  should include a picture, a title  and the time for preparation. On a mobile device the recipe cards  should collapse and  each recipe card should occupy the full screen width . The user should also  be a able to click the image and be directed to the single -recipe page. 

         Ascertain that the recipe cards displayed beneath the header image are divided into three equal columns with card container designs. The recipe cards should be designed with a picture, a title, and the time required for preparation. On a mobile device, the recipe cards should collapse and each recipe card should take up the entire width of the screen. The user should be able to click the image and be directed to the single-recipe page as well.

         ![recipe cards in a tablet view](static/images/readme/test/fig47.png "recipe cards in a tablet view")

        When viewed on a mobile device, the recipe cards collapse to one per row, as expected.

        ![recipe cards in a mobile view](static/images/readme/test/fig48.png "recipe cards in a mobile view")

    3. Confirm that when the "BACK" button under the recipe cards is clicked, it takes the user to the appropriate site and that the button expands when the mouse is hovered over the item.

          During testing, when the mouse is hovered over the button, it expands and a box shadow appears. As expected, the button is placed at the bottom of the recipe cards, adjusting to the screen width as it is increased and decreased. When the user clicks, he or she is returned to the homepage.

<br/>

#### **LOGIN PAGE**

1. On a desktop, navigate to the Login page. 

2. Confirm that the card container containing the login form has a background image and that the card adjusts to the screen responsively.

    When tested on a desktop device, the background image is visible, and the card container adjusts to fit the screen width.

    ![login page](static/images/readme/test/fig49.png "login page")

3. Confirm that the form validation on the login page works when the required attribute is present.
 
    Testing this on all devices reveals that the user cannot "LOGIN" to their profile unless they provide the correct details in the correct format or fill out all of the fields.

    ![login page with feedback](static/images/readme/test/fig50.png "login page with feedback")

    When the user enters the correct information in the correct format and enters his or her username and password, they will be logged into their profile and will be able to create a recipe.

4. Confirm that when the "Login" button is hovered, it expands with a box shadow and directs the user to the profile page.

    Performing this test reveals that the Login button expands as expected, with a box shadow present to make it visually appealing. When the button is pressed, the user is taken to their profile page, where they are greeted with a flash message.

    ![button on login page](static/images/readme/test/fig51.png "button on login page")

    ![profile created](static/images/readme/test/fig52.png "profile created")

5. Confirm that when a user enters the wrong password or username, a feedback message is displayed informing them that the details were incorrect.
        
    When this test is run on all devices, it can be seen that when a user enters a wrong username/password and clicks the "LOGIN" page, they are presented with feedback informing them that the details they have entered are incorrect. 
    It does not specify which input field is incorrect in order to keep hackers from gaining access to the user's account.

    ![provide wrong login details](static/images/readme/test/fig53.png "provide wrong login details")

6.	Confirm that clicking the "REGISTER HERE" link below the form leads to the sign-up page.
        
    By clicking on the "REGISTER HERE" link at the bottom of the form, the user is directed to the registration page, as expected, to sign up for Ayo Recipes.

<br/>

#### **REGISTER PAGE**

1. On a desktop, navigate to the Register page. 

2. Confirm that the register page has a background image and that the register form is in a card container.

    When tested on a tablet device, the background image is present on the site, and the register form is indeed in a card container with its contents evenly spaced.

3. Confirm that the form validation for the register page is enabled in the card container. If the field is not filled correctly, the user should be prompted, and if it is filled correctly and the "SIGN UP" button is clicked, the user should be directed to the correct site.

    Testing this on all devices reveals that the user cannot "LOGIN" to their profile unless they provide the correct details in the correct format or fill out all of the fields. The user will not be able to submit the registration form unless all fields are correctly filled out.

    ![register page validation](static/images/readme/test/fig54.png "register page validation")

    There are currently placeholders on the register page to help users with the information that is expected of them. This improves the user experience.

    ![register page with placeholders](static/images/readme/test/fig55.png "register page with placeholders")

    When the user correctly fills out all of the fields and clicks the "SIGN UP" button, he or she will be directed to their profile page.

4. Confirm that clicking the "LOGIN" link takes the user to the Login page where they can sign up. 

    By clicking on the "LOGIN" link located under the register form card container, the user is directed to the Login page, where they can login to their profile.


#### **SIDE NAVIGATION**

1. Navigate to the Home page on a desktop and reduce the screen width to that of a tablet/mobile device.

2. Confirm that when the hamburger icon is clicked, the side navigation appears from the left side, and that the user can easily hide the side navigation by dragging/swiping the mouse to the left.

    When tested on a tablet device, the hamburger icon appears when the screen width is reduced. When the hamburger icon is clicked, the side navigation appears; to hide it, the user simply swipes left or drags the pointer left as expected.

    ![side navigation bar](static/images/readme/test/fig56.png "side navigation bar")

3. Confirm that the menu items on the side navigation bar, when clicked, take the user to the correct page, and that a white background overlay appears when the mouse is hovered over the menu items.

    When tested on all devices, the white background does appear on the menu items when the mouse is hovered over them.

    ![hover effect on menu items in sidenav](static/images/readme/test/fig57.png "hover effect on menu items in sidenav")


4. Confirm that when the page is opened, the brand image logo appears in the side navigation bar.

    During testing, it was discovered that when the hamburger icon is clicked and the side navigation bar opens, the user can see the brand image logo at the top of the menu recipes. When the brand image logo is clicked, the user is returned to the home page.

5. Confirm that when a user clicks the "Ayo Recipes" heading under the logo, they are directed to the homepage, just like the brand logo. 

    When tested on a mobile device, it can be seen that when the hamburger icon is clicked, the sidenavigation bar opens and the user can click the heading for "Ayo Recipes," which directs them back to the homepage as the brand logo, as expected.

<br/>

#### **TIPS & TRICKS**

1. If you're a logged in user on a desktop, go to the Tips & Tricks page.  

2. Confirm that the images and brief summary of each section are responsive as the screen width is changed.

    As the screen width is adjusted to that of a tablet device, it is clear that the images and summary text, including the header text, of each section are responsive as expected.

    ![tips & tricks on a tablet view](static/images/readme/test/fig58.png "tips & tricks on a tablet view")

3. Confirm that when a button on the page is hovered over, it expands in size and that clicking the button takes the user to the appropriate site on a new page.

    When the mouse is hovered over the buttons, the button expands with a box shadow present on all devices. When the user clicks the button, he or she is directed to the desired site on a new page, as expected.

<br/>

#### **PROFILE PAGE**
1. When you login or register, you are taken to your profile page.

2. Confirm that the user's personal information appears correctly when he or she signs in. On all devices, the user details and icons should be responsive.

    Testing this on a desktop device it can be seen than the user details match that of the database. On a tablet device it can be seen that the user details as well as the icons adjust to fit the size of the screen without looking squashed. The details are evenly spaced, on a mobile device the same effect takes place . The details are evenly spaced and collapse to one input field per column. 

     ![profile user details](static/images/readme/test/fig59.png "profile user details")

3.	Confirm that when the mouse is hovered over the buttons, they expand and the user is directed to the correct page when the buttons are clicked.

    When tested on a mobile device, the desired effect is seen when the mouse is hovered over the buttons: a box shadow appears on the button as it expands. 

<br/>

#### **ALL ADD FORMS**
**( Create Recipe, Add Category)**

1. Confirm that the user must fill out all mandatory fields before submitting any of the forms. If the fields are not properly filled out, the user should receive a validation message.

    When the two forms are tested, it is clear that the user is unable to submit any of them without entering the correct information. When the user clicks the submit button, they are notified if any fields were left blank. If the user enters incorrect information or enters fewer characters than required, they are also prompted on the form with a validation message stating what is expected. 

    However, the select category validation did not work on the create recipe form, allowing the user to submit the form without selecting a category. This was solved by incorporating the select validation function from the task manager project of Code Institute. This caused the select category option to function as expected, notifying the user when no options were selected.


2.	Confirm that a flash message appears at the top of the screen providing feedback on the user's action.

    When the user clicks the submit button, he or she is given feedback on the action that was just completed. 

<br/>

#### **ALL EDIT FORMS**
**( Edit Recipe, Edit Profile, Edit Category)**

1.	Confirm that all edit forms populate the correct information in all input fields. Before submitting, the user must complete all mandatory fields. 

    When testing the three pages forms, the desired effect occurs: the pre-populated information is presented in the input fields, and the user is informed about mandatory fields that cannot be left blank if they want to submit the form without filling out all of the fields. 

    However, on the edit profile page, the "required" attribute was not added to the input type "email," allowing the user to submit the form without filling out the mandatory field. 

    This was fixed by adding the "required" attribute to the "email" input type on the edit page. 

2.	Confirm that a flash message appears at the top of the screen in response to the user's action. 

    When the user clicks the Update button, he or she receives feedback on the action that was just completed.

<br/>

#### **ALL DELETE FORMS**
**( Delete Recipe, Delete Category)**

1.	Confirm that when the "delete" button is clicked, a modal appears asking the user to confirm their action. If the user selects Delete, the appropriate recipe/category is removed.

    When tested on a desktop device, the modal does appear when the user clicks the "delete" button. A dialogue box appears, asking the user to confirm that they want to perform the desired function. When you click the delete button, the recipe/category is removed from the website and database.

2.	Confirm that a flash message appears at the top of the screen in response to the user's action.

    When the user clicks the Update button, he or she receives feedback on the action that was just completed..

3.	Confirm that the "Cancel" link, when clicked, returns the user to the appropriate page.

    When tested on a mobile device, the cancel button directs the user back to the manage categories page, and the dialogue box disappears.
 

4. Confirm that when you hover the mouse over the two buttons, they expand and a box shadow appears.

    When tested on a mobile device, the desired effect can be seen when the mouse is hovered over the buttons. As the button expands, a box shadow appears on it, and when clicked, it performs the desired function.

<br/>

### **DEFENSIVE PROGRAMMING**

Some defensive back end programming has been put in place to limit users' access to certain functions.

1.	Only the admin user has the ability to add a category to the website. The admin user's menu includes a new menu item called "Manage Categories." Any category can be added, edited, or deleted by the admin user from this page. 

2.	When a guest user views the single recipe page, they do not have the option to order the recipe; instead, they only see the "back" button. When the button is pressed, the user is taken to the login page, where he or she can register and either create or order a recipe.


3.	When a user registers/logs in, they can view all recipes created by other users and, if desired, order the recipe via an external link. The user would only be able to edit or delete their own recipes, not those of other users. When viewing another user's recipe versus recipes created by them, the registered / logged in user will notice that the buttons on the single recipe page are different. 

4.	If the user is unable to provide an image url for the recipe on the add-recipe page, a default image will appear in the recipe card when the recipe is added to the user's profile. If the user wants to learn more about the recipe, they can click on the recipe card to be taken to the single recipe page, which includes a recipe image even if the user did not enter an image url in the add recipe form.

5.	 The admin user has the same functions as the registered user. When viewing each recipe individually, the admin user has the ability to edit and delete all recipes. On the website, he or she can also add, edit, or delete a recipe category.

6.	Only the registered user and the admin user have access to the profile menu item and can create a recipe. To perform the basic CRUD functions, the guest user would need to register/login with Ayo Recipes.

</br>

### **LIGHTHOUSE TEST**
The lighthouse test was used to evaluate our website's performance, accessibility, best web practises, and SEO. The lighthouse test results for Ayo Recipes are listed in the table below.

Page Name | Performance | Accessbility | Best Practices | SEO | See link   
--- | --- | --- | ---  | --- | ---    
index.html |  96 | 94 | 80 | 90 | [see here](static/images/readme/lighthouse/index.png)   
recipes.html | 78 | 88 | 87 | 90 | [see here](static/images/readme/lighthouse/recipes.png)   
profile.html | 80 | 93 | 87 | 90 | [see here](static/images/readme/lighthouse/profile.png)   
single-recipe.html | 99 | 95 | 80 | 90 | [see here](static/images/readme/lighthouse/single-recipe.png)  
edit-recipe.html | 91 | 82| 100 | 90 | [see here](static/images/readme/lighthouse/edit-recipe.png)  
edit-profile.html | 94 | 96 | 87 | 90 | [see here](static/images/readme/lighthouse/edit-profile.png)   
view-category.html | 90 | 94 | 87 | 90 | [see here](static/images/readme/lighthouse/view-category.png)
add-recipe.html | 90 | 89 | 87 | 90 | [see here](static/images/readme/lighthouse/addrecipe.png)
tips&trick.html | 100 | 94 | 80 | 80 | [see here](static/images/readme/lighthouse/tips&tricks.png)
login.html | 92 | 95 | 87 | 90 | [see here](static/images/readme/lighthouse/login.png)
register.html | 92 | 95 | 87 | 90 | [see here](static/images/readme/lighthouse/register.png) 
manage-category.html | 94 | 94 | 87 | 90 | [see here](static/images/readme/lighthouse/manage-categories.png) 
add-category.html | 94 | 96 | 87 | 90 | [see here](static/images/readme/lighthouse/add-category.png) 

<br/>

### **FURTHER TESTING** 

1.	The site was tested on a desktop device (Mac OS and Windows), iPad, iPadPro, iPhone(6,7,8 and SE) and Pixel2 to ensure that it was error-free and responsive. Some feedbacks were provided. 

    * One of the feedbacks was that the register form was not accepting their phone number format even if they followed the pattern shown. This was fixed by changing the pattern in the input field to one that accepted the users input as well as the placeholder in order for the user to understand easily.  

    * Another issue was that they couldn't select a category from the drop down menu. If they wanted to select "Soup Recipe," for example, the form would select "Snack Recipe," which they found annoying and frustrating. This was fixed by adding the "multiple " attribute to the select element; for more information, see "SOLVED BUGS, no.13."


3. The website [AM I Responsive](http://ami.responsivedesign.is/) was used to capture Ayo Recipes aesthetic look and responsiveness across all devices. Screenshot below.

    ![overview of AYO RECIPES on all devices](static/images/readme/general-overview.png)

<br/>

### **SOLVED BUGS**

1. To display the correct category name that the user selected on the edit recipe page, the if/else statement provided in the for loop had to be changed. Instead of ( % If category.category_name == recipe.category_name % ), this was changed to ( % If category.category name in recipe.category name % ) because the recipe category name is in an array and we need to use the "in" keyword to check for the value category name in order for the system to pick the correct item from the array. 

2. On a tablet device, the flash message at the top of the website had no padding on the left and right sides, making the text look squashed. This was resolved by adding padding to the flash message's left and right sides.

3. On the register page, it was discovered that the "about me" input field at the bottom of the page lacked a min-length or max-length attribute, allowing the user to enter any number of characters in the about me field. The text area element was fixed by adding the "min-length" and "max-length" attributes.


4. The placeholder text for Phone number and password on the register page has been updated to a more concise text that can direct the user of the necessary pattern /input expected. The previous text was a little puzzling for the user.

5. On the recipes page, an if/else statement is present for the recipe image incase the user does not input any link. If no link is added to the recipe image url , a default recipe image would appear on the recipes page in a recipe card. The image can also be seen on the single -recipe page and the users profile. 

 
6. The star rating on a tablet device was overflowing to another row on the add – recipe page. This was corrected by decreasing the font size of the star icon from a breakpoint of 1024px below.

    ![tablet view of add recipe page ](static/images/readme/test/fig59.png "tablet view of add recipe page ")

7. To create the dynamic input fields, stack overflow and [Youtube](https://www.youtube.com/watch?v=MLBLsxcB3Dc) were consulted. However, when the javascript code for the dynamic input fields was linked to the overall script.js file for the website, errors appeared in the chrome dev tools console tab. Except for the recipe and edit recipe pages, this error appeared on all pages. This was rectified by separating the JavaScript code for the dynamic input fields into a separate file called (addscript.js). 

    The new file (addscript.js) was added to the add recipe and edit recipe pages to validate the dynamic input fields, which worked and eliminated all errors on each page.

8.	When a user clicks on the category image pills or category name headings, they are taken to the view category page, which displays all of the recipes created by users in that category. If there are no recipes, the user should see the message "no category results found." 

    This was not the case during testing, as the "no category results found" message was not visible. To resolve the issue, the steps used to create the search function for Ayo Recipes were used to create the if /else statement for the view _category page, allowing the user to see the message "no category results found."

    This was fixed by adding an if/else statement above the for loop that said  (%if allrecipe|length > 0 %). The recipes' for loop should be nested inside the if else statement. When the test is run again with this fix, the message "no category results found" now appears as expected.


9. The placeholder for the user to enter their phone number on the register page was still confusing to the user and did not accept the user's mobile phone number format. This was changed to a more clear understanding placeholder, with the font size increased to make it more visible. The pattern for the input field has been updated as well. This fix enabled the user to enter their phone number without issue.
    pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}”

10. Some extra padding is added to the footer content to remove the bottom space on the webpage. The footer currently has only a top padding, but to address the issue, a bottom padding is added to the footer container, removing the space at the bottom of the footer. When the user views the webpage, he or she will notice that the space at the bottom of the page has been removed.

     ![no padding at the bottom of home page ](static/images/readme/test/fig60.png "no padding at the home page")

     ![ padding at the bottom of home page ](static/images/readme/test/fig61.png "padding at the home page")

11.	On the single recipe page, further testing on an iPad device revealed that there was almost no top padding for the recipe image, making the menu bar and recipe content look squashed. This was fixed by adding some top padding to the recipe-image class. This change improved the visual appeal of the recipes page.
    ![no top padding on single recipe page ](static/images/readme/test/fig63.png "no top padding on single recipe page")

    ![ top padding on single recipe page ](static/images/readme/test/fig64.png "top padding on single recipe page")
 
12.	Initially, the delete modal did not work because the system read the same id for the various categories on Ayo Recipes. This was resolved by conducting research on [stackoverflow](https://stackoverflow.com/questions/44606429/modal-window-in-jinja2-template-flask), which suggested creating a dynamic modal that would target each category id, which worked. If an administrator wanted to delete a category, the correct category id is now targeted.

13. During additional testing, one of my colleagues complained about having difficulty creating a recipe due to the select category. The select category was not working properly for her while she was using her phone and iPad to access the webpage, whereas it was working properly for me, the developer. I tested this on a desktop device with Chrome Dev Tools, adjusting the screen size, but the issue that affected her was not visible. 

    When this test was performed on an iPad, it was discovered that the aforementioned problem exists. The user was unable to select a preferred category without the system changing it.

    ![ Old category dropdown on addrecipe page and edit page](static/images/readme/test/olddropdown.png " Old category dropdown on addrecipe page and edit page")

    This was escalated to tutor support, who suggested a workaround involving the multiple attribute. The user can now select multiple categories by adding the "multiple" attribute to the select element. However, for this project, the user is only permitted to select one of the categories listed on the placeholder. This new fix allows users to select a category of their choice and edit it to their liking.

    ![ Old category dropdown on addrecipe page](static/images/readme/test/new-dropdown.png " new category dropdown on addrecipe page and edit page")


14. When testing the admin user goals, it was discovered that when the admin user adds a new category, the categories are arranged alphabetically and take up two rows and two columns. 

    ![ old category section on home page](static/images/readme/test/oldcategory.png " old category section on home page")

    However, for some newly added categories, the html structure is distorted; the first fix was to add breakpoints for different screen devices, but this did not resolve the issue.

    ![ distorted category section showing categories on home page](static/images/readme/test/distortedcategory.png " distorted category section showing categories on home page")

    The design of the category section, as well as the html code, were changed to allow the admin to add new categories to the webpage without distorting the structure of the categories section. Instead of two rows of categories, one row with a category heading is occupied by one category. The images and fonts have been created to be mobile-friendly on all devices. As the user adjusts the screen width, the images and heading text shrink to fit the screen without looking squashed or tacky.

     ![ desktop view of new category section on home page](static/images/readme/test/list-category.png " desktop view of new category section on home page")

     ![ mobile view of new category section on home page](static/images/readme/test/mobile-view-category.png " mobile view of new category section on home page")



<br/>


