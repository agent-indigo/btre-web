const logout = document.querySelector('a#logout')
if (logout) logout.addEventListener(
  'click',
  () => document.querySelector('form#logout').submit()
)
setTimeout(
  () => $('#message').fadeOut('slow'),
  3000
)