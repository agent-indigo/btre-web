const App = (() => {
    document.querySelector('.year').innerHTML = new Date().getFullYear()
    setTimeout(() => {
        $('#message').fadeOut('slow')
    }, 3000)
})()
export default App