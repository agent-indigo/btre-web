# BT Real Estate Database Schema

Database name: btre

## Tables

## Listings

- id: INT
- realtor: INT (FK [realtors])
- title: STR
- address: STR
- city: STR
- state: STR
- zipcode: STR
- description: TEXT
- price: FLOAT
- bedrooms: INT
- bathrooms: FLOAT
- garage: INT [0]
- sqft: FLOAT
- lot_size: FLOAT
- is_published: BOOL [true]
- list_date: DATE
- photo_main: STR
- photo_1: STR
- photo_2: STR
- photo_3: STR
- photo_4: STR
- photo_5: STR
- photo_6: STR

## Realtors

- id: INT
- first: STR
- last: STR
- photo: STR
- description: TEXT
- email: STR
- phone: STR
- is_mvp: BOOL [false]
- hire_date: DATE

## Contacts

- id: INT
- user_id: INT
- listing: INT
- listing_id: INT
- first: STR
- last: STR
- email: STR
- phone: STR
- message: TEXT
- contact_date: DATE
