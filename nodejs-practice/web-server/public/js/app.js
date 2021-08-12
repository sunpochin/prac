console.log('Client side javascript file is loaded!')


const weatherForm = document.querySelector('form')
const search = document.querySelector('input')
const message1 = document.querySelector('#message-1')
const message2 = document.querySelector('#message-2')
const historydiv = document.getElementById('history')

//const historydiv = document.createElement('p')

message1.textContent = 'LOADING!!!'
message2.textContent = '.............'

weatherForm.addEventListener('submit', (e) => {
    e.preventDefault()

    const location = search.value
    console.log('testing! :', location)

    const loc = document.createTextNode('location')
    const br = document.createElement('br')
    historydiv.appendChild(loc)
    historydiv.appendChild(br)
    console.log('loc: ', loc)

    let url = '/weather?address=' + location
    fetch(url).then(
        (response) => {response.json().then( (data) => {
            if (data.error) {
                console.log('data.error: ',data.error)
                message1.textContent = data.error
            } else {
                console.log('data.location: ', data.location)
                console.log('data.forecast: ', data.forecast)
                message1.textContent = data.location
                message2.textContent = data.forecast
            }
        })
    })
    

})


