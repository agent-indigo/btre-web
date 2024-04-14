const logout = document.querySelector('a#logout')
if(logout) logout.addEventListener('click', () => {
    document.querySelector('form#logout').submit()
})
document.querySelector('span#year').innerHTML = new Date().getFullYear()
setTimeout(() => {
    $('#message').fadeOut('slow')
}, 3000)