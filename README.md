family-shopper
A bespoke shopping list management app developed using django and a variety of other technologies especially for the Hyland family.

Code Institute - Fourth Milestone Project: Build a Full-Stack site based on the business logic used to control a centrally-owned dataset (in this case, the data used by the Hyland family to organise their household grocery shopping). Set up an authentication mechanism (for one superuser, an "adult" and a "child" role) and provide appropriate access to the site's data, allowing each role to do activities appropriate to that role, based on the dataset.

Image of a H. x intermedia 'Arnold Promise' in mid-October

A very common cultivar of H. x intermedia ('Arnold Promise') giving a spectacular show of leaf colour in mid-October

## The user story

The Hyland family is a four-headed monster that consumes a shocking lot of groceries (especially chocolate) every week. The main shopper in the family (the father of the household ... me) does his best but often finds it difficult to keep track of what's in stock and what's not.  The other three family members (the mother of the household, Annett, and the two children, Lily and Jim) often tell him what from their point of view is missing and what new purchases might be appreciated.  They also occasionally do a bit of shopping!

Since I'm currently learning full-stack programming with Code Institute and am required by my course to complete a Full-Stack Web application for my fourth portfolio project, I thought this requirement would provide a good opportunity to develop a basic prototype (or minimally viable product - MVP) of a shopping list app designed specifically for our family needs, for further development at a later date. The objective of this project is therefore to create just such a MVP.

We decided that the MVP should include the following features:
- The adults (i.e. Annett and myself) should be able to govern which products should be included in shopping lists and which sources (shops, supermarkets, etc.) should be allowed.
- The children should be able to suggest new products and sources to include in the system, subject to the approval of us two adults.
- It should be possible to add a description to each suggested and/or approved product.
- The children should be able to add a description only to a suggested product and should be unable to edit an approved product.
- It should be possible to add only approved products to the shopping list.
- Products should be divided into categories and default sources and that the shopping list should be filterable using those categories and defaults.
- The children should not be able to cancel items from the shopping list but should be able to mark items as bought. The adults should be able to do both.
- There should be some simple mechanism to control which edits should take priority when more than one person at a time is editing the data.
- There should be no mechanism for outsiders to register to use the app. The superuser should the only person(s) able to add or delete a user from the app.
- Anyone not logged in or stumbling on the site accidentally (or maliciously!!) should see a page asking them to log in. If they can't log in, then the simply don't get to see the shopping list.

## System design

Some flow charts portraying a selection of important Hyland family shopping list workflows.

I prepared a series of outline flow charts in consultation with Nette on the basis of our family needs and habits. Once we'd agreed the basic processes, I began thinking about how to actually program the various functionalities the family needs in the short term.

My reasons for choosing a django-based system on a Postgresql database at the back end, with some important appearances from Bootstrap on the front end, were basically twofold:
- Django offers a seamless way of creating a simple full-stack website quickly and corresponding to the family's needs and habits.
- The most obvious way of satisfying the requirements of my fourth portfolio project on my Code Institute Full-Stack Programming course was to use Django along with Bootstrap.

### The database structure

I decided that the simplest way implementing the above requirements at the back end was to base the system on two main tables:
- a Product table, listing all the articles approved for inclusion in the shopping list
- a List Item table, in which a new record is created every time a new item is added to the shopping list by picking a product to be bought
I decided not to ordinarily delete List Item or Product records, but simply to remove LIst Items from the visible shopping list as they're bought or cancelled. In the case of records on the Product table, they are not shown on the Product list if the value of their 'Current' variable is set to False.

The other bespoke tables of the database are as follows:
- Shop
- Category

For the moment, the purpose of both these tables is simply to allow the user to appropriately filter results for the Product and List Item tables, depending on where they are and what category of shopping they want to buy.

Their purpose has the potential to expand to provide more information to the family members in the future.

There are also two tables generic to Django:
- User
- Group

The purpose of the first of these from our point of view is to manage users and maintain security (so that nobody but family members can access the website), the second (again, from our point of view) is simply to maintain the functional distinction between an adult user and a child.


The website's workflow:
The first thing a user sees on navigating to the website is an login page. Nobody can get any further without logging in. Once logged in, any user in either group should be able to see the full current shopping list in order of entry (oldest first). They should also see several buttons:
- a button inviting the user to add an item to the shopping list
- a button inviting the user to filter by category
- a button inviting the user to filter by shop



There should be two checkboxes attached to each item on the shopping list, though only one of them will be enabled for child users:
- a Cancel Item checkbox on the left, which should only be enabled for adults
- an Item Bought checkbox on the right, which everyone should be able to check

When an adult checks the "Cancel Item" checkbox, the text for the item is shown in grey and the Item Bought checkbox is disabled.
When anyone checks the "Item Bought" checkbox, the text for the item is shown in strikethrough font and the Cancel Item checkbox is disabled (if it's not already disabled).

Anyone who double clicks on an item text will be brought to an Item Details screen, where they can see further details on the Item. Adults can edit these details.


Once users are logged in, they are immediately shown the full list of current items on the shopping list. The page also contains buttons allowing them to do the following:
- filter the list by category and shop
-


cuttings taken vs total rootstocks
grafts taken vs total plants in stock (recorded for each cultivar separately)
ad-hoc tasks
Option 7 (Record plant losses) asks the user the cultivar and age of the plants they want to record as lost (including year-zero rooted cuttings), showing them the current figure for that cultivar and age. The user is prevented from entering a number greater than that figure. It gives a confirmation message before writing the data entered by the user to the spreadsheet.

Option 8 (Record plant gains) works similarly, adding instead of subtracting. It does not impose any restriction on the number added.

Option 9 (Hold over plants for one year) asks the user to identify the cultivar and age of the plants they want to hold back, shows the user the current number of those plants and subtracts the number given by the user from the current age category, adding the same number to the category one year younger. As with record_loss, the user can't move more plants than the recorded number for the relevant category in any direction. The system also prevents the user from entering a value less than two, as it is impossible to hold year-one plants over to year-zero. The year zero values are not recorded in the plants worksheet at all. They have ther own worksheet (grafts-year-zero)

Option 10 (Bring plants forward one year) does the same in the opposite direction. Again, the appropriate restriction on numbers moved applies. In contrast to the previous option, the user can choose the value 1 for year cohort, as the same problem doesn't apply here.

In exceptional cases where the user wishes to hold back or bring forward a number of plants by more than a year, they must run the relevant process twice.

Unfortunately, due to the time restraints, I was unable to implement option 11 (Add new cultivar). I have, however prepared much of the groundwork to introducing it in the future. For example, I have implemented a system by which the functions that involve cultivars identify those cultivars dynamically.

Reductions in plant stocks through sales are not recorded in this app. The couple tell me that this may be the next step once they have this work planning system bedded in.

The same can be said of a number of other parts of the nursery workflow.

Bug fixes and warning resolution
Bugs
Bugs were fixed as they arose during smoke testing.

As far as practicable, all Bugs are resolved separately and the Bug resolution is recorded in Git commits separately, prefixing the commit text with "Bug: ".

Warnings
pycodestyle issues (all warnings) were closed shortly before submitting the app project.

Two warnings could not be resolved, but appear not affect the functioning, reading or comprehension of the program in any way! They were:

$ pip install pycodestyle
$ pycodestyle ...

  warnings.warn(
run.py:318:22: E231 missing whitespace after ':'
run.py:318:22: E701 multiple statements on one line (colon)
run.py:428:80: E501 line too long (82 > 79 characters)
In reality there are at least a dozen warnings relating to lines that are too long, but they do not affect the Heroku pseudo-terminal and do not appear to affect the readability of the code. I corrected them, saw that the caused bugs in the presentation, and even in the running of the code itself, and reversed them (one by one).

App robustness
Numerical vs character/string entries
Aside from the restrictions on user entries mentioned above, the user must not enter either a negative number or an entry that cannot be rendered as an integer. Sadly, in most cases, I have not had the time to resolve all issues relating to the user entering characters and strings that cannot be converted into integers yet, but I have put the necessary software in place in some functions (notably the opening menu function and functions 6, 7, 8 and 9). I have told the users to be careful not to make non-numerical entries where numerical entries are expected.

Out of range numbers
The app has been designed so that integers entered outside the valid range of values are handled elegantly without the program havin to shut down. Users are shown an appropriate message repeatedly until they make a valid entry.

Yes or no responses
The app is designed so that the user can respond to yes or know answers by entering 'y' or 'Y' for yes; entering any other value than 'y' or 'Y' is interpreted as a no.

Programming philosophy
Being an app generally modelling a procedural series of steps, little use was made of the concepts of OOP in its design. Few custom classes were specifically designed for the app. This was deliberate and should not be taken for any absence of understanding of the basic concepts of OOP. It may, however, be useful to look at other programs created for a similar purpose when the time comes to refactor this code, and to use the advantages of OOD/OOP to make the code more efficient and more comprehensible.

Sharing the hamamelis google spreadsheet
This section is work in progress.

Registering for Heroku and using it
This section is work in progress.

Lessons learned
This section is work in progress.

Other unresolved issues and future development
This section is work in progress.

Credits
This section is work in progress.