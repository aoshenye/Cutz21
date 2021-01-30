# CutZ

This primary goal of CutZ is to provide users with a place to submit, create, read and delete their own reviews of barbers they have seen. User's can compare  the best and the worst barbers in their areas and make conscious decisions about where to get their hair cuts. 

## UX

This website is geared towards men and women who want to describe their experiences with their barbers, but also find out about other customer's experiences. The website is a perfect way for people to get a better understanding on the best barber that fits their needs and location requirements as well. The reviews overall provide the much needed information for prospective clients to know more about their barber prior to having anything done on their hair. We all hate wondering how good our barber is or whether they know how to do a fade. This website covers that for prospective clients before you have even left your home.

### Strategy

The main goal of this project is to provide users with a sleek and simple user experience of reviews and a chance for them to provide their reviews. I have done research and below user stories describe the user needs for my webpage.

User Stories:

-   As a user type, I want to be able to upload my review and share it with the community that are registered users( good that people have to register as it makes me more comfortable to read and make other reviews which are trustworthy, ensuring its regular reviewers). and I want to be able to edit it freely and possibly delete it if I do not feel fully comfortable with it. I want people to use my reviews as a basis for how good or bad a barber is so I know if they are good for just me or for other people. 

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features
-   Navigation bar: Simple and swift and initiated with materialize
- CRUD functionality
	- The Form - add_review.html - simple form that allows user to name the barber and provide their comments and date of their experience. 
	- reviews page - get_reviews.html - provides users to read all reviews. 
	- Edit and Delete function provided on the user's profile page. 

- Flash messages provided to warn people when logging in or trying to register. 
- Buttons: initialized from Materialize 

- In the future, it would be good to add a "forgotten password" section. 

## Technologies Used

-   
    -   For **HTML**  for the outline of the website and all it pages 
    - For **CSS** for styling support rather than full styling of website. 
    - For **Python** for background logic of website. 
    - For **Flask** - displaying python logic on web browser
	- For **MongoDB** - python extension for manipulation mongoDB database & storage of collections for reviews and user information/fields. 
	- For **Materialize** - creating the layout of the pages, navigation bar and footer.
	- 

## Testing
1.  review form:
    1.  Go to the "Your review" page
    2.  Try to submit the empty form and verify that an error message about the required fields appears
    3.  Try to submit the form with an invalid email address and verify that a relevant error message appears
    4.  Try to submit the form with all inputs valid and verify that the flash success message appears.
    5. Try to submit the form as a registered user and verify takes you to the Profile.html page for that user
2. Log in page
	1. Try to login as an unregistered user and verify error message appears. 
	2. Submit as a registered user, and verify can log in and renders profile.html page with user's username being displayed. 
3. Ensure when logged in, a user can see their profiles
	1. log in as a registered user
	2. add a review in Your reviews page and submit it
	3. ensure a successful submission message is displayed.
	4. go to profile page and ensure user can see user individual  reviews. 
4. Nav bar - ensure Navigation bar renders when screen size altered. 
		1. open page and altered screen size to make it smaller. Nav bar was missing. Altered the page size and nav bar size and background image size to render navigation bar effectively.  
5. The website was tested on the following browsers using a Microsoft Surface Laptop on Windows 10.

- Google Chrome - Version 86.0.4240.183 (Official Build) (64-bit)

- Microsoft Edge - Version 86.0.622.63 (Official build) (64-bit)

- Firefox - 75.0 (64 bit)

- The website worked efficiently on all browsers and mobile phones above. All navigation links, required elements, APIs’ all functioned correctly. The hovering animations still worked on all browsers.

- The site was also tested on the following Devices:

	- Google pixel 3a using Google Chrome on Android 10 iphone xr using Safari on IOS 13.4.1 
## Deployment
1.  login to heroku
2.  Create heroku app
3.  Add heroku with repository by typing in terminal: heroku git: remote -a cdins-msp3-recipe-book
4.  Create requirements.txt file by typing in terminal 'pip3 freeze > requirements.txt'
5.  Create Procfile by typing in terminal: 'web: python3 app. py > Procfile'
6.  Add and push created files to repository by commands: 'git add', 'git commit', 'git push' for github and 'git push heroku master' for heroku.
### For Deployment 
	1. Link git hub repository to Heroku
			-click Deploy
			- got to App connected to GitHub
			- find my github page
			- click connect and ensure connection  made. 
			- scroll down to Automatic Deploys
			- In the choose a branch to deploy section, click Master
			- scroll down to Manual deploy and click Deploy Branch.
			- Wait a few seconds for deployment.   

## Credits

### Content

- Photos were taken from my own library of photos.   
- Materialize used for layout and design of website Particularly the home page is inspired by example themes by [Materialize](https://materializecss.com/Z)
- Wireframes were created with [lucid.app](lucid.appZ])

### Media

-   The photos used in this site were obtained from ...

### Acknowledgements

-   I received inspiration for this project from code institutes Task manager mini project for inspiration from the CRUD functionality. [Task Manager - Mini Project](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/course/#block-v1:CodeInstitute+DCP101+2017_T3+type@chapter+block@196c000dd670458cafc7b2dc9d4a8245Z)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzOTgzODU5MV19
-->
