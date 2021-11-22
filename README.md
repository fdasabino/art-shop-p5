# Daniela's Art Shop - by Daniela Kronvall

<img src="#">

## Project Goals

- Hi there! Welcome to Daniela's Art Shop.
  I have put together an ecommerce webpage that intends to satisfy the requirements of the project milestone 5 of the Code
  Institute.
  In this page you will find a fully functional ecommerce website. The main goal with this project is to create a small
  size ecommerce store that sells original paintings and prints, created by the artist.

- Generally speaking I believe the project to bring the feeling of a small art store, with personal touch, going away
  from the usual conventions in some cases. There are few implementations that I would like to do in the future, but due
  to time constraints they will have to be implemented later on.

## Deployed Application

- The Application is accessible by clicking on the link below. If you wish to create a test account click on the sign in
  dropdown menu and click register, to be transferred to the allauth default account creation links.

[View the live project here](https://danielasartshop.herokuapp.com/)

## UX

- Given this application is for an art ecommerce website, the design is very product centered. It has been
  designed to enable a customer to add items to their basket, and checkout and pay as seamlessly as possible. All
  pertinent product information is highlighted upfront, for example, price, size and product uniqueness to keep customers
  informed.

### User Stories

- As an User I would like to be able to purchase a product directly from the artist website.
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

- This application has been designed to be used used as an e-commerce page, allowing users to interact with application
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

- In a near future before the application becomes available for actual commercial use. I´d like to implement an inventory
  management that automatically deducts sold items out of the available stock. Considering the goal of the page is to sell
  unique items in most cases.

- When it comes to user management I would like to implement a custom model that allows users to delete their account if they
  wish to do so.

## Design

- The page design was inspired by the Boutique Ado, template provided by the Code Institute. The design is simplistic and minimalist.
  The focus of the design is to direct the user to the product page, and provide a simple but effective solution for the user all the way through out completing the purchase.

### Colour Scheme, Imagery and Typography

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

[Google Fonts:](https://fonts.google.com/)

- Google fonts was used to import the fonts into the main.css file which is used on the project.

[Font Awesome:](https://fontawesome.com/)

- Font Awesome was used as the icon provider for this project.

[Stripe:](https://stripe.com/en-se)

- Stripe is implemented as the default payment tool in this project.

[GitHub:](https://github.com/)

- GitHub is used for version control and to store the project's code after being pushed to the repository.

## Testing

### Validating

- No errors were found on this page, according to the [HTML - Checker](https://validator.w3.org/nu/) validator.

<img src="https://res.cloudinary.com/frank2021/image/upload/v1637589191/Danielas%20art%20shop/Screenshot_2021-11-22_145256_niuias.jpg">

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

## Deployment

### Heroku

### Forking the GitHub Repository

- By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make
  changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork"
   Button.
3. You should now have a copy of the original repository in your GitHub account.

- Click
  [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
  to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Special Thanks

### Code

### Media

## Latest Updates
