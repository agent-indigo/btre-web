# BT Real Estate

## Description

This is the BT Real Estate project from Brad Traversy's 2019 Python Django Dev to Deployment course on O'Reilly.

I made the following modifications:

- Third party resources retrieved from CDNs instead of locally bundled

- Redirect staff to admin area after logging in through user-facing login page

- Added a link in the `nav` to the admin area that only appears when a staff member is logged in

- Moved JavaScript embedded in the `nav` to `btre/static/app.js`

- Moved the following into partials:

  - Breadcrumb

  - Listings

  - Search

  - Inner Showcase

- Added a favicon

- Added a setting to enable/disable sending emails

- Set up `dotenv` and added a template

- Bug fixes

- Other minor modifications
