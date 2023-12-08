# FilmFlux

### Welcome to Filmflux! Your go-to destination for films.

## For a live preview of FilmFlux click this link.
* https://filmfluxx-394da2dec566.herokuapp.com/


# UX Design

### Design Thinking
When I started this project, my goal was to create a film blog website that was modern and user friendly where people can review, add, delete film blogs and meet new people of the same genre/film.
* Easy access to film reviews
* A navbar to navigate through pages
* Being able to create an account and login
* A film card able to edit and delete reviews
* Add a film page

# User Stories

* Create a film review
  - As a site user I want to add my favourite films and add my personal review on the film so that I can view all the films I have watched and reviewed.
* View a film review
  - As a site user I want view films and the reviews so that I can watch them in my free time.
* Edit a film
  - As a site user I want to edit films so that I can give it my own personal opinion.
* Delete a film
  - As a site user I want to delete my review so that I can delete it if I change my decision.
* Navigation Bar
  - As a site user I want to navigate through the navbar so that I can easily navigate through the website.
* Footer Social Links
  - As a site user I can click on social links that I can follow the restaurant on various social media pages.


 ### Database Chart

 I created a chart for my CRUD functionality so I am able to use this image and chart to visualize the model I want in my project.


 # Design

## Home Page
  
* Laying out all the cards (Films) across the page so the user can easily see which films are rated and liked by other people.
*  Navbar that includes, register, login, films and add your own film.
  
## Log In Page
* In this page I want the user to be able to login to their existing account

## Register Page
* In this page I want the user to be able to create a account.

## Add a Film
* In this page I want the logged in user to be able to view, create, delete and update their films.

## Logout Page
* Here I want the user to be able to logout of their account.

## Fonts
* I decided to go simple and go with Times New Roman for the text.

## Colors
I decided to go with quite a few colors:
* Black: #3f006a0f;
* Blue: #0d6efd;
* Black: #000;
* White: #f6f6f6;
* White: #fff;
* Orange: #ffbf50;

# Features

## Existing Features

### Navbar
* The Navigation bar includes films, add a film, login, register and sign in
* It is visible on all pages and includes all the navigation links
* The navbar is the most crucial part as it simplifies the navigation of the website

  <img width="1440" alt="Screenshot 2023-12-07 at 17 11 57" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/e94e3448-09ee-414c-b978-52c30eebde9a">

### Registration Page 
* Registration allows users to add films

  <img width="732" alt="Screenshot 2023-12-07 at 17 18 54" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/006701ec-4a06-45bb-9ee6-e0a66ae1c188">

### Sign In 
* Sign In feature allows users to sign in and add in reviews or remove them.

  <img width="720" alt="Screenshot 2023-12-07 at 17 22 48" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/3c9c3b96-e0f5-4e16-8256-35d39966be2e">
### Add a film form

* Allows user to create a film review
* Users can add image, add their own review about the film alongside a rating out 10
* User can see who posted the app with time and date
  <img width="758" alt="Screenshot 2023-12-07 at 18 09 52" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/c4a22c78-c1c5-4df9-8c96-7dc3c618d30e">

### User Review
* Provides user when it was edited and uploaded
* The user can easily see the review, description and the film type about the page.

  <img width="1247" alt="Screenshot 2023-12-07 at 18 19 15" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/a4a1094f-98db-4af8-964c-71e014b74b6b">
### Update Film 
* If decision is changed you can simply edit the review
* Allows users to change review, image, rating, description and the film type
* Saves users time and effort instead of adding a new one

<img width="1108" alt="Screenshot 2023-12-07 at 18 25 50" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/4a2dc6cd-74b3-4cb3-b082-91f44dd797c0">

### Delete Film

* If user is not happy with review they can delete it
* Confirm button is available for the user if user is undecisive

  <img width="327" alt="Screenshot 2023-12-07 at 18 30 16" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/ad84d7ec-7862-49f6-acf8-7ac7a95843fe">
### Footer Social Links 
* Users can use these links to connect with the sites social accounts (Does not actually take you to the sites pages)
* Allows users to stay connected with the sites on social media platforms, keeping them informed about the latest dishes and events.

  ## Future Features

  ### Leave a comment
  The ability to leave a comment on other users reviews. This ability I want to add allows users to connect with eachother and get eachothers opinion.

  ## Favourites
  I want to add this feature so users can favourite their films or films they would like watch. This feature would allow users to find films they would like or interested in for them to watch it later on.

  ## Search Bar
This feature will be going on for more easy accessibility for the user. 

# Tools and Technologies used
## Frameworks, libraries and programs used
* Django Django served as the foundation of this project, used for the creation of models, forms, and views of the app.

* Cloudinary Cloudinary was used as free cloud store CSS staticfiles.

* Bootstrap 5.1 Bootstrap 5.1 enhanced the project's user interface, enabling responsive and visually appealing design.

* ElephantSQL was chosen for its reliable PostgreSQL database hosting, ensuring efficient data management for the project.

* Google Fonts was used to import the 'Prompt' font in the style.css file which is used on all text on the website. 

* Git Git was employed for version control by utilizing the GitPod terminal to commit changes and push them to GitHub.

* GitHub was used to store the project code after being pushed from gitpod.

* Heroku was used to host the project.

* Font Awesome was used for fonts on the site.

* ChatGPT was used to improve copyright.

* LucidChart was used to create my diagram Booking Model.

  ## Languages used
  * CSS3
  * HTML5
  * Python
 
## Bugs 
Currently the images are down which will be fixed as soon as possible.
The sign out page isnt showing due to some error in the urls.
The cards on the homepage is not showing for some error between the home app and films app
The responsiveness is not tested yet due to cards not showing

## Solved Bugs 
* Could not get the edit button to display the form 
 - I fixed this by linking the edit button by giving it a film.id

   # Validation

I used https://jigsaw.w3.org/css-validator/validator to validate my CSS3 

| File | Screenshot | Notes |
| :---         |     :---:      |          ---: |
| base.css |   <img width="1420" alt="Screenshot 2023-12-07 at 20 53 07" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/1f71baf2-2d02-4b89-9f77-5edba91a3c49"> | Pass |

I used https://validator.w3.org/nu/ to validate my HTML

| File | Screenshot | Notes |
| :---         |     :---:      |          ---: |
| Sign up | <img width="1406" alt="Screenshot 2023-12-07 at 21 30 21" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/7bd5a945-fc67-4793-b00f-4b871cfc7122">| Heading error |
| Log in | <img width="1424" alt="Screenshot 2023-12-07 at 21 31 59" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/1b55f37f-e476-46d6-9b85-3cd63f55aa6e">| Heading error |
| Add a film | <img width="1424" alt="Screenshot 2023-12-07 at 21 36 26" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/fe63f065-7255-4778-bfdb-1091d4196ff5">| Heading error and attribute |

I used Python Linter to validate my python code.
| File | Screenshot | Notes |
| :---         |     :---:      |          ---: |
| URLS | <img width="1347" alt="Screenshot 2023-12-08 at 08 36 56" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/abb56900-5b04-40b2-9ad4-df42218f9b16">| Passed |
| Film Views | <img width="1339" alt="Screenshot 2023-12-08 at 08 40 34" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/6d6a2f70-feab-4aa9-921d-a2e55b838520">| Lines too long |
| Film Models | <img width="1325" alt="Screenshot 2023-12-08 at 08 41 30" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/c4c7c413-2f6c-4963-9f0f-b84a9fd6556f">| Lines too long |
| Film Form | <img width="1359" alt="Screenshot 2023-12-08 at 08 42 34" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/f68a1d55-3ff9-4830-b01d-56cf4dae6d75">| Lines too long |
| Admin | <img width="1282" alt="Screenshot 2023-12-08 at 08 43 00" src="https://github.com/Ennie0906/Film-Flux/assets/141347750/61895fdc-4b05-4db1-94f4-c3374833c821">| Passed |

# Manuel Testing 

| Test | Action | Notes | Notes |
| :---         |     :---:      |          ---: |          ---: |
| #1 Clicking on logo name redirect user to homepage | Click the logo name | N/A | Pass |
| #2 Clicking on the Home in the navbar will redirect user to homepage | Click Home tab | N/A | Pass |
| #3 Clicking on the Films in the navbar will redirect user to Films page | Click Film tab | N/A | Pass |
| #4 Clicking on the Register in the navbar will redirect user to the Sign up page | Click Register tab | N/A | Pass |
| #5 Clicking on the Sign In in the navbar will redirect user to the Sign In page | Click Sign In tab | N/A | Pass |
| #6 WHEN LOGGED IN clicking on the add a film tab will open a form to add a film | Click Add a film tab | N/A | Pass |
| #7 WHEN LOGGED IN clicking on the Logout | Click Logout tab | N/A | Pass |
| #8 WHEN LOGGED IN clicking on the add a film button and adds users film with review | Click Add a film | N/A | Pass |
| #9 WHEN LOGGED IN clicking on the edit button and users can edit their reviews | Click Edit | N/A | Pass |
| #10 WHEN LOGGED IN clicking on the delete and users can delete their reviews | Click Delete | N/A | Pass |
| #11 Clicking on the Click on the homepage and users can see the films | Click Click me | In production | Fail |
| #12 Clicking on the Learn me on the homepage and users can see details about the film | Click Learn more | N/A | Pass |
| #13 Clicking on the Links in the Social Links footer takes users to designated sites | Click icons on the footer | N/A | Pass |


# Browser Testing
### Firefox 
Works perfectly no errors

### Safari
Works perfectly no errors

My websites performance by lighthouse.
![lighthouse-filmflux](https://github.com/Ennie0906/Film-Flux/assets/141347750/a335f6c7-e0ef-4d8c-a146-d147ab5c3cf2)

# Deployment: 

Deployment
To deploy the project to Heroku, I followed these steps:

* Creating Heroku App:
* Logged into Heroku.
* Selected 'Create New App' from the dashboard.
* Chose a unique app name.
* Selected region based on the location.
* Clicked 'Create App'.
* Connecting to GitHub:

From the Heroku dashboard, navigated to the 'Deploy' tab.
* Under 'Deployment Method', chose 'GitHub'.
* Searched and selected the repository by name.
* Clicked 'Connect'.
* Setting Environment Variables:
* Went to the 'Settings' tab.
* Located 'Config Vars' and clicked 'Reveal Config Vars'.
* Added the necessary variables.
