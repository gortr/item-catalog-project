# Movie Trailer Project
**Author:** Rigoberto Gort
**Date:** 05/01/2017

## Project Info
**Filename** 

README.md

**Main Project File:** `application.py`

**Connected Module Files** 

`database_setup.py`
`client_secrets.json`

**Connected HTML Files** 

`home.html`
`base.html`
`deleteCategory.html`
`deleteItem.html`
`editCategory.html`
`editItem.html`
`header.html`
`login.html`
`newCategory.html`
`newItem.html`
`publiccategories.html`
`publicCategoryItems.html`
`publichome.html`
`publicitems.html`
`showCategoryItems.html`
`showItem.html`
`showUser.html`
`deleteImage.html`
`editImage.html`

**Connected CSS Files** 

`bootstrap.min.css`
`style.css`

### Configuration Instructions
`application.py`

This is the primary file required in order to run the item catalog application.

This file imports the data that was setup in the itemcatalog.db file from database_setup.py.

### Operating Instructions
Please confirm that you have the following installed on your machine:

- Vagrant
- Virtual Box
- Python
- SQLite
- SQLalchemy
- OAuth2Client

For example, if you are using the standard Python IDLE  (GUI) then you would open the file in that environment. 

You would need to,

1. Verify that you have the required files installed in a directory of your choosing.
2. Verify that you are in that directory and run `vagrant up` in the CMD or Terminal.
3. Enter `vagrant ssh`.
4. Changes directories until you reach the iteam-catalog-project directory.
5. Once there make sure to run the `python database_setup.py` file. (Make sure itemcatalog.db does not exist first)
6. Afterwards make sure to run the feed the database information to test including a valid email and username which would tie into your Google Account.
7. Run `python application.py`
8. Open a browser and enter `localhost:8000`
9. Test the database to your hearts content!