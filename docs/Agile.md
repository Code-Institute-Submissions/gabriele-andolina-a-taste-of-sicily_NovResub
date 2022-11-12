# **User Stories & Agile Development**

## **1. Wireframes**

The detailed wireframes and database schema for this project can be found here: [Wireframes & Database](/docs/wireframes.md).

## **2. Epics & User Stories**

![Epics no. 1-2](/docs/images/1-epics-one-two.png).
![Epics no. 3-4](/docs/images/2-epics-three-four.png).
![Epic no. 5](/docs/images/3-epic-five.png).

## **3. Epics & User Stories - Description and Testing**
### **3.1 Epics & User Stories - Description** 

No. | User Story
--- | ----------
1   | As an admin, I want to present a clear landing page so that users can quickly understand the site's goals and feel drawn to become a member. 
2   |As a registered user, I can write new posts so I can actively contribute to the community with my experience and learn from other contributors'.
3   | As a registered user, I can create, read, update and delete my own posts so that I am always free to modulate my participation in the community.
4   | As a registered user, I can like or unlike a post so I can interact with the content.
5   | As a registered user I can comment on a post so I can be involved in the conversation.
6   | As an admin I can view comments on each post so I can moderate the conversation as necessary.
7   | As an unregistered/registered user I can view the number of likes on a post so I can start reading from the most popular ones.
8   | As a user, I can create a personal account so I can become part of the community, contribute to its blog and have my personal diver's profile.
9   | As a site user (both registered and unregistered) I can open a post so I can read it in its entirety.
10  | As an unregistered/registered user I can view a paginated list of posts so I can get an instant and clear glance at the available posts.
11  | As an unregistered/registered user I can view a list of posts so I can easily select one to read.
12  | As an admin/registered user, I can create draft posts so I can finish writing the content later.
13  | As an admin, I can approve comments so that inappropriate and/or offensive content can be left out of the community.
14  | As an admin, I can manage all blog posts so that the community may be a place which offers true value and correct information to all its users.
15  | As a registered user, I can log a new dive so I can keep track of my progress and experiences underwater.
16  | As a registered user, I can always view a list of previous dives on my profile's page so I can easily access them at any time.
17  | As a registered user, I can create, read, update and delete my dives so I can keep my personal logbook updated and relevant.
18  | As a registered user, I can store all posts together so I can easily return to previous conversations.
19  | As a registered user, I can see all posts of the same user so I can benefit from all of their contributions if I have enjoyed previous posts by them.
20  | As a registered user, I can add other divers as friends so I can keep in touch with them and their ongoing diving adventures.
21  | As a registered user, I can log a dive shared with another user so I can keep track of shared underwater adventures.

### **2.2 Testing User Stories** 

#### **2.2.1 Successful User Stories**
No. | User Story | Result
--- | ---------- | ------
1   | As an admin, I want to present a clear landing page so that users can quickly understand the site's goals and feel drawn to become a member. | Pass
2   |As a registered user, I can write new posts so I can actively contribute to the community with my experience and learn from other contributors'. | Pass
3   | As a registered user, I can create, read, update and delete my own posts so that I am always free to modulate my participation in the community. | Pass
4   | As a registered user, I can like or unlike a post so I can interact with the content. | Pass
5   | As a registered user I can comment on a post so I can be involved in the conversation. | Pass
6   | As an admin I can view comments on each post so I can moderate the conversation as necessary. | Pass
8   | As a user, I can create a personal account so I can become part of the community, contribute to its blog and have my personal diver's profile. | Pass
9   | As a site user (both registered and unregistered) I can open a post so I can read it in its entirety. | Pass
10  | As an unregistered/registered user I can view a paginated list of posts so I can get an instant and clear glance at the available posts. | Pass
11  | As an unregistered/registered user I can view a list of posts so I can easily select one to read. | Pass
13  | As an admin, I can approve comments so that inappropriate and/or offensive content can be left out of the community. | Pass
14  | As an admin, I can manage all blog posts so that the community may be a place which offers true value and correct information to all its users. | Pass
15  | As a registered user, I can log a new dive so I can keep track of my progress and experiences underwater. | Pass
16  | As a registered user, I can always view a list of previous dives on my profile's page so I can easily access them at any time. | Pass
17  | As a registered user, I can create, read, update and delete my dives so I can keep my personal logbook updated and relevant.  | Pass

## **3. Agile Development**

The tool I chose to keep track of my work is Asana, due to its popularity and to some sort of acquaintance due to my previous project.
On Asana, I organized my work in Epics and User Stories (see the above section for all the Epics and User Stories), finding Asana a practical tool to organize smaller subtasks such as the User Stories from the same card.

Below is a detail sample of an Epic and its organization as it showed on the kanban board:
![Kanban board detail](/docs/images/4-kanban-board-detail.png)

### **3.1 The project's kanban board at the final stage of development**

![Kanban board in progress](/docs/images/5-kanban-board-progress.png)


### **3.2 Logbook App Implementation:**

The first version of the project did not have the logbook app, the user stories of which (15 through 17) do not appear in the kanban board shown above. The bulk of these (to complete all CRUD functions) were implemented in the course of one sprint that lasted from September 27 to October 4, 2022, as observable in the commits history.

### **3.3 Things to note/improve:**
- *Poor formatting:* After removing the Summernote Widget, the content portion of the blog post and the description portion of the dive details are not formatted in an aesthetically appealing way. This is something that can be improved in future versions of the project.