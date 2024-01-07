class App {
    constructor() {
        const date = new Date()
        document.querySelector('.year').innerHTML = date.getFullYear()
    }
}
export default new App()