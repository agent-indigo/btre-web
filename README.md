# BT Real Estate

## Description

This is the BT Real Estate project from Brad Traversy's 2019 Python Django Dev to Deployment course on O'Reilly.

I made the following modifications:

- Moved uploaded image storage to Cloudinary

- Added a setting to enable/disable sending emails

- Set up `dotenv` and added a template

- Staff get redirected to the admin area after logging in through the user-facing login page

- Added a link in the `nav` to the admin area that only appears when a staff member is logged in

- Moved the following into partials:

  - Breadcrumb

  - Listings

  - Search

  - Inner Showcase

  - Realtor card

- Added a favicon

- Added dynamic page titles

- Moved JavaScript that was embedded in the `nav` to `btre/static/app.js`

- Copyright year in footer retrieved using jinja instead of JS

- Added a `noscript` tag

- Added `tel` and `mailto` links

- Third party resources are retrieved from CDNs instead of locally bundled

- Added Docker files

- Bug fixes

- Other minor modifications
