# **Testing and Bugs**

## **1. Testing**

This project was tested manually. Here follows a list of the tests that were carried out.  

No. | Action | Result
-- | -- | --
1 | Display homepage | ✔︎
2 | Navbar links are properly connected and lead to their related page | ✔︎
3 | Navbar displays general links for unregistered/unauthenticated users | ✔︎
4 | Shop Now button on homepage successfully opens products main page | ✔︎
5 | Search bar returns items with entered keywords | ✔︎
6 | Product detail page open upon click | ✔︎
7 | Quantity +/- buttons allow the user to select the quantity to purchase | ✔︎
8 | Keep Shopping button redirects the user to the main products page | ✔︎
9 | Add To Cart button correctly adds items to the cart | ✔︎
10 | Checkout link from success message toast links to updated cart | ✔︎
11 | Checkout page shows empty checkout form if no info is present | ✔︎
12 | Checkout page shows saved info if present | ✔︎
13 | Adjust Cart button leads back to cart | ✔︎
14 | Complete Order button successfully completes the order | ✔︎
15 | Stripe payment process is completed after clicking Complete Orded Button | ✔︎
16 | My Account navbar link correctly displays option for non/authenticated users | ✔︎
17 | If user is superuser, My Account link provides option to Add Food | ✔︎
18 | If user is superuser, My Account link provides option to Add Experience | ✔︎
19 | Add Food link correctly opens 'Add a Food Item' form | ✔︎
20 | Add Experience link correctly opens 'Add an Experience' form | ✔︎
21 | Cancel button on Add Food page leads back to Products main page | ✔︎
22 | Cancel button on Add Experience page leads back to Experiences main page | ✔︎
23 | Add Item button on Add Food/Add Experience pages correctly adds new item to the database | ✔︎
24 | Forms cannot be submitted without key information (indicated by an asterisk) | ✔︎
25 | If user is superuser, Product and Experience cards show edit and delete buttons | ✔︎
26 | Edit button correctly allows for item update | ✔︎
27 | Delete button correctly allows for item deletion | ✔︎
28 | Messages show constantly to notify the user of their actions (e.g. sign in and sign up, product editing, etc.) | ✔︎
29 | Accounts can be created successfully through Sign Up link | ✔︎
30 | Confirmation for Account creation is required through provided e-mail link | ✔︎
31 | Confirmation of Account creation is provided to the user via toast message | ✔︎
32 | Order History shows correctly for the right user | ✔︎
33 | Update Information button on My Profile page correctly updates profile info | ✔︎
34 | Forgot Password button on Sign In page triggers sending of email to recover it | ✔︎
35 | Password can be successfully reset through link received in e-mail | ✔︎

## **2. Known Bugs**

No. | Description 
-- | --
1 | Remove button on cart page does not work