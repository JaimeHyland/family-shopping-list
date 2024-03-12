family-shopper
A bespoke shopping list management app developed using django and a variety of other technologies especially for the Hyland family.

Code Institute - Fourth Milestone Project: Build a Full-Stack site based on the business logic used to control a centrally-owned dataset (in this case, the data used by the Hyland family to organise their household grocery shopping). Set up an authentication mechanism (for one superuser, an "adult" and a "child" role) and provide appropriate access to the site's data, allowing each role to do activities appropriate to that role, based on the dataset.

Image of a H. x intermedia 'Arnold Promise' in mid-October

A very common cultivar of H. x intermedia ('Arnold Promise') giving a spectacular show of leaf colour in mid-October

## The user story

The Hyland family is a four-headed monster that consumes a shocking lot of groceries (especially chocolate) every week. The main shopper in the family (the father of the household ... me) does his best but often finds it difficult to keep track of what's in stock and what's not.  The other three family members (the mother of the household, Annett and the two children, Lily and Jim) often tell him what from their point of view is missing and what new purchases might be appreciated.  They also occasionally do a bit of shopping too!

Since I'm currently learning full-stack programming with Code Institute and am required by my course to complete a Full-Stack Web application for my fourth portfolio project, I thought this requirement would provide a good opportunity to develop a basic prototype (or minimally viable product - MVP) of a shopping list app designed specifically for our family needs, for further development at a later date. The objective of this project is therefore to create just such a MVP.


System design

Some flow charts portraying a selection of important witch-hazel worklflows

Accordingly, I prepared a series of outline flow charts in consultation with Laura and Donal on the basis of the needs they described to me. Once they'd approved the charts, I began thinking about actually programming the various functionalities.

For simplicity's sake, and because I thought the data was not enormously complex, I decided to store it all on a single google spreadsheet, which I simply named 'hamamelis'. It contains three worksheets.

rootstock
grafts-year-zero
plants
The data should be read as follows.

The 'rootstock' worksheet
The first column (A) is a label to tell the witch-hazel program what year the figures in the corresponding row refer to. The current year is at the top.
The top figure in the second column (B) shows the number of cuttings that the couple plan to take in the autumn of the current year minus one. The figures below that represent the number of cuttings that the couple planned to take in each relevant year minus one in the past.
The third column (C) shows the number of cuttings that they actually took in the relevant year.
The fourth column (D) shows the number of cuttings that rooted successfully and were potted up during the spring. It is a representation of work done, and does not increase when immature rootstocks are acquired from an outside source, nor does it reduce when such rootstocks are lost through disease or damage, or when they are used up to in the grafting process. Notice the change in nomenclature: successfully rooted cuttings begin to be referred to as rootstocks as soon as they've planted in pots (potted up).
The fifth column (E) contains at most two non-zero values: one in E1, which represents the figure for rootstocks in stock this year to become available for use as next year as rootstocks. It is equivalent to the value in D1 minus any losses and plus any acquisitions. The value in E2 represents the total number of rootstocks now available for use in this year's grafting. Every time a grafting session is recorded, this value goes down by the number of grafts made. Any rootstocks left over after the year's grafting campaign is finished remain in the system until they are set to zero upon creation of a new year. The reason for this is that two-year-old rootstocks will rarely be suitable for grafting when the time comes around again in the new year. They are generally physically disposed of (recycling the pots and compost) when the opportunity arises during the course of the new year. The rootstock worksheet the end of a year
The rootstock worksheet as it might look towards the end of a growing year

The 'grafts-year-zero' worksheet
The grafts-year-zero worksheet contains two more columns than the number of cultivars of Hamamelis currently cultivated by the Witch Hazel nursery.

The first column identifies the year to which the data in the corresponding row refers.
The second column tells any human or machine reader whether the figures in the corresponding row refer to numbers of grafted plants that the couple originally planned ('planned'), that they actually made ('grafted') and that they currently have in stock ('stock'). The 'stock' figure for the current year refers to the number of plants of the given category currently in stock (i.e., the number of grafts originally made of the relevant cultivar in the current year minus any losses recorded since then, plus any gains since then). When a new year is created, the relevant numbers are passed into the 'plants' worksheet, three new rows are created for the current year and the figures for 'planned' and 'grafted' for previous years can no longer be edited.
Each subsequent column gives the figures described above for the cultivar labelled in the topmost cell. The grafts-year-zero worksheet the end of a year
The grafts-year-zero worksheet as it might look towards the end of a growing year

The 'plants' worksheet
The plants worksheet is a little simpler. It shows the current stocks of each cultivar of each age group – i.e.: the total number of grafts of that age currently in stock, adjusted according to the losses and gains subsequently recorded by the couple in the witch-hazel program using the record_loss, record_gain, hold_back and bring_forward functions (see below). The plants worksheet towards the end of a year

The plants worksheet as it might look towards the end of a growing year

The program's original workflow and the technical issues with the technology used
At the outset of programming, I wanted the app to call a run.py file in the usual way but to attach an argument after a blank space on the command line, depending on the task that the user wished to do at that time. Unfortunately, the Heroku pseudo terminal on which the app is destined to run does not allow the use of command-line arguments (or at least I have been unable to find a way of implementing such a command-line-argument-based design). Due to some issues with my implementation of the Heroku architecture, I discovered this limitation rather late in the day. As a result I was forced redesign the app at the last-minuteto follow a different (and in my opinion much less elegant) logic. Originally, the user would have typed the run.py file name on the terminal, followed by a space and then a short string indicating what they wanted the app to do.

For example, they would have typed run.py plan_cuttings to plan their campaign of taking and preparing cuttings. But the Heroku pseudo-terminal automatically runs the run.py file without any arguments immediately upon opening, so everything must be based on an argument-free initial call. The description of the workflow below is based on my last-minute changes due to this difficulty. It should be understood, however, that workflow described below was not my first choice.

The time used dealing with this problem at the last minute may have affected some of the finishing work on the program. For example, it was my original intention to connect each task to the next in their logical order, asking the user if they wished to go on to the next task. Sadly, the user now needs to restart the program every time they wish to complete a new task.

The program's workflow:
Seasonal tasks in order
Typically towards the autumn of every year, the owners will want to close out the figures they have entered over the previous year, begin a new year and start work on planning their campaign of taking H. Virginiana cuttings. They begin this task by running the app and choosing option 1 (Create new year/Close out current year). This function adds the required new lines for the new current year on each worksheet, and copies the data on graft stocks for the old current year to date from the grafts-year-zero worksheet to the plants worksheet. This has the effect of putting the data for the previous year out of reach of the seasonal tasks.

Also within the Create new year/Close out current year function, users can choose either to enter the figure for cuttings that they anticipate taking this year or opt to leave that job for later.

The rootstock worksheet straight after the user executes the  function

The rootstock worksheet straight after the user executes the Create new year/Close out current year function. Note that the user has chosen to enter a value for planned cuttings of 2800. That value can be changed at any time during the year by running Option 2 Plan this year's cutting campaign.

The grafts-year-zero worksheet straight after the user executes the  function

The grafts-year-zero worksheet straight after the user executes the Create new year/Close out current year function.

The plants worksheet straight after the user executes the  function

The plants worksheet straight after the user executes the Create new year/Close out current year function.

Then, whether or not they have entered a figure for planned cuttings, they can run app option 2 Plan this year's cutting campaign to revise that figure. If they have already recorded a figure for cuttings actually made, they are given a warning to tell them that the cutting campaign has already started and asked to confirm whether they want to replace the planned figure with a new total. The new figure is not added to the old one; it simply replaced it. This is the case with all planning functions.

When they run app option 3 (Record cuttings taken), they are asked to enter a number of cuttings actually taken. They are given the already existing figure for cuttings taken and warned not to enter a number for cuttings unless that number has already been physically taken, prepared and inserted in the cuttings bed. It tells the user when the number of cuttings taken exceeds the number of cuttings planned.

The new figure entered by the user is added to the already existing number. In the nursery, the cuttings campaign takes several days, the owners typically entering the day's figure for cutting production in the evening of the relevant day. The user receives a message on the command line when the figure exceeds the planned figure. The logic behind the difference between planned figures (each of which simply replaces the previous one) and the actually taken figures is that the latter are usually totted up for each day in the cutting/grafting campaigns, and the user should expect the app to remember the numbers recorded from previous days.

Option 4 (Record rooted cuttings potted up) instructs the user to enter a figure for the number of successfully rooted cuttings actually potted up. As another figure indicating for work actually done (usually daily), it functions in a similar cumulative way to option 3 (Record cuttings taken, as do all functions designed to record work actually done). It informs the user when the total number of potted cuttings recorded has reached or exceeded the total number of cuttings taken.

Option 5 (Plan grafts for this year) displays the number of rootstocks (i.e. the figure for cuttings successfully potted up in the previous year, minus losses, plus gains) asks the user what cultivar they want to graft and how many grafts they want to make of that cultivar. The function keeps a running total of the rootstocks required and issues a notification/warning if and when the total number of planned cuttings exceeds the number of rootstocks available. As the function is about planning numbers, new numbers simply overwrite old ones the second and subsequent time the user runs the option for a particular cultivar.

Option 6 (Record grafts taken) argument asks the user which cultivar they want to record grafts for. The owners typically enter the day's figure for graft production separately for each cultivar in the evening of the relevant day. The user receives a message on the command line if and when any figure exceeds the associated planned figure. As for other options recording work actually done, new figures are added to old figures creating a new total. Each time a grafting session is recorded in this way, the current stock of rootstocks is reduced by the corresponding amount.

N.B.: In order to record total work done separately from current stocks (i.e., total work done minus losses plus gains) all the following numbers are recorded separately:

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