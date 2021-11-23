# Daniela's Art Shop - by Daniela Kronvall

<img src="https://res.cloudinary.com/frank2021/image/upload/v1637611261/Danielas%20art%20shop/Art-shop_lmlgrl.jpg">

## Project Goals

- Hi there! Welcome to Daniela's Art Shop.
  I have put together an ecommerce webpage that intends to satisfy the requirements of the project milestone 5 of the Code
  Institute.
  In this page you will find a fully functional ecommerce website. The main goal with this project is to create a small
  size ecommerce store that sells original paintings and prints, created by the artist.
  Generally speaking I believe the project to bring the feeling of a small art store, with personal touch, going away
  from the usual conventions in some cases. There are few implementations that I would like to do in the future, but due
  to time constraints they will have to be implemented later on.

## Deployed Application

- The Application is accessible by clicking on the link below. If you wish to create a test account click on the sign in
  dropdown menu and click register, to be transferred to the allauth default account creation links.

[View the live project here](https://danielasartshop.herokuapp.com/)

## UX

- Given this application is for an art ecommerce website, the design is product centered. It has been
  designed to enable a customer to add items to their basket, and checkout and pay as seamlessly as possible. All
  pertinent product information is highlighted upfront, for example, price, size and product uniqueness to keep customers
  informed.

### User Stories

- As an User I would like to purchase a product directly from the artist website.
- As an User I wish to find relevant information about a product, such as price, size, and description.
- As and User my experience has to be seamless and simple. With easy access to my personal information dashboard.
- As an User I want to be able communicate with the page owner without hassle in order to give feedback on a particular
  product or collaborations.

### Visitors can

- Explore the page information without having to create an account.
- Create an account if they decide to do so.
- Access their personal information dashboard once they have created an account.
- Add an address, that will be available on their profile page.
- Find links to social media accounts related to the artist.

### First Time Visitor Goals

- As a first time visitor, I want to see information about the artist, in order to consider making a purchase.
- As a first time visitor, I wish to see the product list before having to create an account.
- As a first time visitor, I would like to have access to account creation links.

### Returning Visitor Goals

- As a returning visitor, I want to use my sign-in credentials to access my profile page.
- As a returning visitor, I would like to see updated products list.
- As a returning customer, I would like to easily find links to social media and contact.

### Store Owner Goals

- As a store owner, I want to quickly modify product availability.
- As a store owner, I would like to categorize products, and exhibit information about a certain product.
- As a store owner, I would like to find information about orders and customer information under the same menu context
  on my admin panel.
- As a store owner, I expect to store customer information for future communications about events and promotions.

## Existing Features

- This application has been designed to be used used as an ecommerce page, allowing users to interact with application
  in numerous ways:

#### PROFILES

- In this app, all customer information is stored.
  Django-allauth is used as the default account management tool giving the user the ability to verify email addresses and
  reset passwords.
  Within this app I have used a number of default forms provided by allauth to integrate with the UserProfile model.
  To produce responsive forms I have used the django-crispy-forms that allows me to control the behavior of forms in a
  elegant and DRY way, without creating custom form templates.
  This app is also responsible for displaying order history, in combination with the checkout and products app.

#### PRODUCTS

- The Products app provides the majority of the application's functionality. It delivers this through two models,
  Product and Category.
  Products are displayed either in list form, for multiple views, or in detail form, for a specific
  product, both views displaying information about the items for sale (product name, price, category, if product is unique,
  dimensions and availability).
  In addition, products can be sorted by price, category or name.
  The product details view, allows users to add items to basket, if available, as well as display a product description.

#### CART

- Cart functionality has been added, allowing users to create a new cart using the session data, stored in the browsers
  session.
  This application has been made available through out the entire website, using a context processor file that allows cart access
  from anywhere on the website.
  The Cart app also provide the user with two views: one for when the cart is empty and another for there are cart items present,
  allowing users to update and remove items from their cart.

#### CHECKOUT

- The Checkout app is used to process orders, and can be accessed without the need to an user to be logged in. With that
  said users must have items in their cart to be able to move forward to the checkout section. This process captures the
  user's address (pre-populated if user is logged in) which is modifiable. Prior to processing payment, users can review
  and confirm their order, with payment processing handled by Stripe.

### Test Payments with Stripe

- As a simple example of the functionality of the application, users can add products to their shopping cart, and make
  test purchases.
- The card numbers below are provided by a third party software called Stripe to allow testing while implementing the
  payment functionality:

|       Event Type:        |   Card Number:   |
| :----------------------: | :--------------: |
|   Successful payment:    | 4242424242424242 |
| Requires authentication: | 4000002500003155 |
|     Failed payment:      | 4000000000009995 |

### Features Left to Implement

1. Automatic Stock Update

- In a near future before the application becomes available for actual commercial use. I´d like to implement an inventory
  management that automatically deducts sold items out of the available stock. Considering the goal of the page is to sell
  unique items in most cases.

2. Self Account Deletion by User

- When it comes to user management I would like to implement a custom model that allows users to delete their account if they
  wish to do so.

## Design

- The page design was inspired by the Boutique Ado, template provided by the Code Institute. The design is simplistic and minimalist.
  The focus of the design is to direct the user to the product page, and provide a simple but effective solution for the user all the way through out completing the purchase.

#### Colour Scheme

- The colour scheme of the entire page was chosen by the artist and seeks to inspire, users in a calming manner.
  The navbar and footer have a different colour scheme to bring together the contrast with the dark accent colours provided by the bootstrap
  framework.

  Navbar and Page Headers:
  [Pale Green: #d7f5e5](https://www.color-name.com/pale-mint-green.color#:~:text=Pale%20Mint%20Green%20color%20hex%20code%20is%20%23C2E5D3)

  Footer:
  [Light Pink: #FFB6C1](https://www.color-name.com/light-pink.color)

#### Imagery

- The images used in this project are created by the artist and are protected by copyright.
  They are not free for reproduction or use without the artist´s consent.

#### Typography

- As my logo font I have chosen 'Caveat', cursive. An elegant and easy to read font that brings together the feeling of the page.
  The fallback font is sans-serif.

- For the body elements I have chosen 'Lato', which is easy to read and flows with the rest of the project, Sans-serif is also the fallback.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)
- [Python](https://en.wikipedia.org/wiki/javascript)

### Frameworks, Libraries & Programs Used

[Django - 3.2.9](https://www.djangoproject.com/)

- Django was used as the main framework for this project

[Bootstrap 4 :](https://getbootstrap.com/)

- Bootstrap was used to assist with the responsiveness and styling of the website.

[Hover.css:](https://ianlunn.github.io/Hover/)

- Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.

[JQuery](https://jqueryui.com/)

- This is a JavaScript framework which enables easy manipulation of the Document Object Model (DOM) using JQuery syntax.

[Google Fonts:](https://fonts.google.com/)

- Google fonts was used to import the fonts into the main.css file which is used on the project.

[Font Awesome:](https://fontawesome.com/)

- Font Awesome was used as the icon provider for this project.

[Cloudinary:](https://cloudinary.com/)

- Cloudinary was used to store all media and static files for the project.

[Mailchimp](https://mailchimp.com/)

- Mailchimp was used as the third party newsletter service for this project following the directions os the Code Institute,
  to collect emails in accordance with GDPR rules.

[Stripe](https://stripe.com/)

- This is used to securely process customer payment details. No payment data is handled or stored by the application, it is all handled by Stripe. This makes for easy and secure integration and verification of payments.

[GitHub:](https://github.com/)

- GitHub is used for version control and to store the project's code after being pushed to the repository.

## Testing

- The application has been tested on most popular browsers, including mobile versions. Also the html code has been validated.

### Different Browsers

- The Page does not support Internet Explorer, but has been tested in the browsers listed below using
  [Broswerstack](https://www.browserstack.com/live) tool:

|    Browser    |      Result       |
| :-----------: | :---------------: |
|    Safari     | No Problems Found |
| Safari-Iphone | No Problems Found |
|    Chrome     | No Problems Found |
|    Firefox    | No Problems Found |
|     Edge      | No Problems Found |
|     Opera     | No Problems Found |

### Further Testing

- Tests were also performed on samsung mobiles and tablets, no significant issues were found.

### Validating

- No errors were found on this page, according to the [HTML - Checker](https://validator.w3.org/nu/) validator.

<img src="https://res.cloudinary.com/frank2021/image/upload/v1637589191/Danielas%20art%20shop/Screenshot_2021-11-22_145256_niuias.jpg">

## Forking from GitHub

- When forking this project from GitHub you will need a to set up a few things of your own:

1. Clone the Repository, or download the files manually from the repository;
2. Open the files in your development environment;
3. Set a Virtual Environment (On Windows - Using VScode)

| --- | ------------------------------- |
| 1 | py -m venv venv |
| 2 | venv\Scripts\activate |
| 3 | pip install -r requirements.txt |

- Complete the steps below

|           Name           | Environment Variable |
| :----------------------: | :------------------: |
|    Django Secret Key     |      SECRET_KEY      |
|    Stripe Secret Key     |  STRIPE_SECRET_KEY   |
|  Stripe Publishable Key  |  STRIPE_PUBLIC_KEY   |
| Heroku Postgres Database |  STRIPE_PUBLIC_KEY   |
|   Static Files Storage   |    CLOUDINARY_URL    |
|     Email Host User      |   EMAIL_HOST_USER    |
|    Default From Email    |  DEFAULT_FROM_EMAIL  |
|   App Password(Google)   |   EMAIL_HOST_PASS    |

- Create a file called env.py, in your root directory and add the following variables listed above to your file.
  Once you have downloaded the Code to you machine you can follow the steps below on deployment to heroku which include
  instructions on how to set up the environment variables

## Deployment to Heroku

- This application has been deployed to Heroku, from a github repository. I have stored some important information
  (config vars) such as Stripe keys, email information, django secret key, database secret key on the heroku admin panel
  under config vars.

* (IMPORTANT - Don't forget to set DEBUG to False in settings.py)

1. Create the Heroku app

| #   | Step                  | Action                                                                          |
| --- | --------------------- | ------------------------------------------------------------------------------- |
| 1.1 | Create new Heroku App | APP_NAME, Location = Europe                                                     |
| 1.2 | Add Database to App   | Located in the Resources Tab, Add-ons, search and<br>add e.g. ‘Heroku Postgres’ |
| 1.3 | Copy DATABASE_URL     | Located in the Settings Tab, in Config Vars, Copy<br>Text                       |

2. Attach the Database (In your editor)

| #   | Step                                             | Action      |
| --- | ------------------------------------------------ | ----------- |
| 2.1 | Create new env.py file on top<br>level directory | E.g. env.py |

3. In env.py

| #   | Step                      | Action                                                              |
| --- | ------------------------- | ------------------------------------------------------------------- |
| 3.1 | Import os library         | import os                                                           |
| 3.2 | Set environment variables | os.environ["DATABASE_URL"] = "Paste in Heroku<br>DATABASE_URL Link" |
| 3.3 | Add in secret key         | os.environ["SECRET_KEY"] = "Make up a<br>randomSecretKey"           |

4. In heroku

| #   | Step                          | Action                        |
| --- | ----------------------------- | ----------------------------- |
| 4.1 | Add Secret Key to Config Vars | SECRET_KEY, “randomSecretKey” |

5. In settings.py

| #   | Step                                                                                                                          | Action                                                                                                        |
| --- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 5.1 | Reference env.py                                                                                                              | from pathlib import Path<br>import os<br>import dj_database_url<br>if os.path.isfile("env.py"):<br>import env |
| 5.2 | Remove the insecure secret<br>key and replace - links to the<br>secret key variable on Heroku                                 | SECRET_KEY = os.environ.get('SECRET_KEY')                                                                     |
| 5.3 | Replace DATABASES Section<br>(Comment out the old<br>DataBases Section)<br>- links to the DATATBASE_URL<br>variable on Heroku | DATABASES = {<br>'default':<br>dj*database_url.parse(os.environ.get("DATABASE*<br>URL"))<br>}                 |

6. In the terminal

| #   | Step            | Code                            |
| --- | --------------- | ------------------------------- |
| 6.1 | Make Migrations | python manage.py makemigrations |

7. In Cloudinary.com

| #   | Step                                                      | Code                      |
| --- | --------------------------------------------------------- | ------------------------- |
| 7.1 | Copy your CLOUDINARY_URL<br>e.g. API Environment Variable | From Cloudinary Dashboard |

8. In env.py

| #   | Step                                                                                     | Code                                                                 |
| --- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 8.1 | Add Cloudinary URL to env.py -<br>be sure to paste in the correct<br>section of the link | os.environ["CLOUDINARY_URL"] =<br>"cloudinary://9444:SUZi@dbhyuj5mc" |

9. In Heroku

| #   | Step                                                                                                 | Code                                                                                          |
| --- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 9.1 | Add Cloudinary URL to Heroku<br>Config Vars - be sure to paste<br>in the correct section of the link | Add to Settings tab in Config Vars e.g.<br>COUDINARY_URL,<br>cloudinary://9444:SUZi@dbhyuj5mc |

10. In settings.py

| #    | Step                                                                                                     | Action                                                                                                                                                                                                                                                                                                                                          |
| ---- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10.1 | Add Cloudinary Libraries to<br>installed apps                                                            | ...<br>'cloudinary_storage',<br>'django.contrib.staticfiles',<br>'cloudinary',<br>...<br>(note: order is important)                                                                                                                                                                                                                             |
| 10.2 | Tell Django to use Cloudinary<br>to store media and static files<br>Place under the Static files<br>Note | STATIC_URL = '/static/'<br>STATICFILES_STORAGE =<br>'cloudinary_storage.storage.StaticHashedCloudinaryS<br>torage'<br>STATICFILES_DIRS = [os.path.join(BASE_DIR,<br>'static')]<br>STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')<br>MEDIA_URL = '/media/'<br>DEFAULT_FILE_STORAGE =<br>'cloudinary_storage.storage.MediaCloudinaryStorage' |
| 10.3 | Link file to the templates<br>directory in Heroku<br>Place under the BASE_DIR<br>line                    | TEMPLATES_DIR = os.path.join(BASE_DIR,<br>'templates')                                                                                                                                                                                                                                                                                          |
| 10.3 | Change the templates<br>directory to TEMPLATES_DIR<br>Place within the TEMPLATES<br>array                | 'DIRS': [TEMPLATES_DIR]                                                                                                                                                                                                                                                                                                                         |
| 10.4 | Add Heroku Hostname to<br>ALLOWED_HOSTS                                                                  | ALLOWED_HOSTS =<br>["PROJ_NAME.herokuapp.com", "localhost"]                                                                                                                                                                                                                                                                                     |

11. In your editor

| #    | Step                                                  | Action                   |
| ---- | ----------------------------------------------------- | ------------------------ |
| 11.1 | Make sure to have 3 folders on top<br>level directory | media, static, templates |
| 11.2 | Create procfile on the top level<br>directory         | Procfile                 |

12. In Procfile

| #    | Step     | Action                       |
| ---- | -------- | ---------------------------- |
| 12.1 | Add code | web: gunicorn PROJ_NAME.wsgi |

13. In the terminal

| #    | Step                 | Action                                                     |
| ---- | -------------------- | ---------------------------------------------------------- |
| 13.1 | Add, commit and push | git add .<br>git commit -m “Deployment Commit”<br>git push |

14. In Heroku

| #    | Step                                       | Action                                          |
| ---- | ------------------------------------------ | ----------------------------------------------- |
| 14.1 | Deploy Content manually<br>through heroku/ | E.g Github as deployment method, on main branch |

## Credits

- Code Institute: this page was built upon the boutique ado template, with some modifications to models, views and template structure.

### Special Thanks

1. Daniela kronvall

- Big thanks for the time and effort put on this project. Appreciate the all the help.

2. Spencer Barriball

- Thanks for the great mentoring skills and experience shared with me along this journey.

## For the accessors

- Following the instructions of the exercises from the modules, below we have a screen shot of the facebook pages for my business.

<img src="https://res.cloudinary.com/frank2021/image/upload/v1637629201/Danielas%20art%20shop/facebook_nuvd0t.jpg">
