# -*- coding: utf-8 -*-
"""

@author: 437team

This file is a prototypescratch file that describes all the needed functions fpr the app 

"""

#concerning the login page
'''
parameters: user_id
-check if this user_id exists, if no  alert an error
-if yes: check if the password_input matches the saved_password
-if no: alert an error/ if yes proceed to the home page
'''
def user_login(user_id, password): 
    return 

'''
parameters: admin_id
-check if this admin_id exists, if no  alert an error
-if yes: check if the password_input matches the saved_password
-if no: alert an error/ if yes proceed to the home page
'''
def admin_login(admin_id, password): 
    return 

#concerning the profile page as a user
'''
parameters: user_id 
-retrieve the user_name and the balance from the user table according to the logged in user_id
-send this info to the front-end side
'''
def personal_info(user_id):
    return 

'''
parameters: user_id
-retrieve the items from the transaction table where user_id is the logged in id and status is “sold”
-send this info to the front-end side
'''
def sold_items(user_id):
    return

'''
parameters: user_id
-retrieve the items from the transaction table where user_id is the logged in id and status is “bought”
-send this info to the front-end side
'''
def bought_items(user_id):
    return

#concerning the home page
'''
-retrieve all the shop_name from the shops table and display on a clickable button
'''
def getshops():
    return

'''
parameters: shop_id
-retrieve all the items with all their information of the selected shop and send them
to the front end of the home page
'''
def shop_items(shop_id):
    return 

'''
parameters: item_id
-retrieve the information (item_id, item_name, image, description, price, quantity) of an item
after pressing on it in the home page (according to the item_id)
-an add_to_cart button will be available 
-pressing on this button will add the item to the user cart
'''
def getitemby(item_id):
    return

'''
parameters: sender_id, receiver_id, amount
-a user can trade money to other users through:
        specifying the id of the other user and the amount of coins
'''
def trading(sender_id, receiver_id, amount):
    return


#concerning the cart page
'''
parameters: item_id, user_id, shop_id
-pressing on the add_to_cart button will add the item with its data to the user cart
'''
def add_to_cart(item_id, user_id, shop_id):
    return

'''
parameters: array of ids of the added items
-the cart page will contain all the needed added items with two buttons: confirm and cancel
-if cancel is pressed: all the process will be cancelled  
-if confirm is pressed: 
    -directs the user to a page link confirming the payment
    -updates the transaction table 
    -shows the updated cart with the new item added
'''
def checkout(item_ids):
    return

'''
parameters: item_id
-in each cart and for each item a delete button will be available 
-pressing this button will delete the item from the cart
'''
def remove_from_cart(item_id):
    return

#concerning the manager functions
'''
parameters: shop_id, item_name, image, price, description, quantity 
-the manager can have 2 options: 
    -option 1: adding each item alone and specifying the details 
    -option 2: adding a json file containing all the items with their details
'''
def add_data(items):
    return 

'''
parameters: item_id
-the manager will enter the item_id of the item he/she wants to update
-a page containing all the item detaills will be displayed with the ability to change every detail 
(shop_id, item_name, image, price, description, quantity)
'''
def update_data(item_id):
    return

'''
-the manager can have 2 options: 
    -option 1: deleting each item alone 
    -option 2: adding a json file containing all the item ids he/she wants to delete
'''
def delete_data(items):
    return

'''
-the manager will be able to get all the transactions made for the shop and on the frontend
they can filter by date
'''
def get_shop_transactions(shop_id):
    return


#concerning the administration functions
'''
-the admin can add aubitcoins for a user
'''
def add_aubitcoin(user_id):
    return


'''
-the admin will be able to get all transaction made on the aubitcoin platform and on the frontend they can filter by date, shop
'''
def get_transactions():
    return


