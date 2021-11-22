# Daniela's Art Shop - by Daniela Kronvall

<img src="#">

## Project Goals

- Hi there! Welcome to Daniela's Art Shop.
  I have put together an ecommerce webpage that intends to satisfy the requirements of the project milestone 5 of the Code
  Institute.
  In this page you will find a fully functional ecommerce website. The main goal with this project is to create a small
  size ecommerce store that sells original paintings and prints, created by the artist.

- Generally speaking I believe the project to bring the feeling of a small art store, with personal touch, going away
  from the usual conventions in some cases. there are few implementations that i would like to do in the future, but due
  to time constraints they will have to be implemented in a near future.

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

#### CHECKOUT

- The Checkout app is used to process orders, and can be accessed without the need to an user to be logged in. With that
  said users must have items in their cart to be able to move forward to the checkout section. This process captures the
  user's
  address (pre-populated if user is logged in) which is modifiable. Prior to processing payment, users can review
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

## Design

### Colour Scheme and Imagery

### Typography

- 'Caveat', cursive, sans-serif; hero text
- 'Lato', sans-serif; body

### Imagery

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/javascript)
- [Python](https://en.wikipedia.org/wiki/javascript)

### Frameworks, Libraries & Programs Used

[Django - 3.2.9](https://www.djangoproject.com/)

- Django was used as the main framework for this project

[Bootstrap 5 :](https://getbootstrap.com/)

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

### Different Browsers

### Further Testing

## Future changes to the Website

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
