const request = require('request')

const geocode = (address, callback) => {
    const url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + address + '.json?access_token=pk.eyJ1Ijoic3VucG9jaGluIiwiYSI6ImNrYTJkNWpjaTBiZzkzZW81aWJrbTljd2UifQ.ZUmvwFva-Peg8A9TfKtddA&limit=1'

//    const url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/Los%20Angeles.json?access_token=pk.eyJ1Ijoic3VucG9jaGluIiwiYSI6ImNrYTJkNWpjaTBiZzkzZW81aWJrbTljd2UifQ.ZUmvwFva-Peg8A9TfKtddA'
    console.log('geocode url:', url)

    request({ url, json: true }, (error, { body }) => {
        console.log('body.features:', body.features.length)
        if (error) {
            console.log('error 1' )
            callback('Unable to connect to location services!', undefined)
        } else if (body.features.length === 0) {
            console.log('error 2' )
            callback('Unable to find location. Try another search.', undefined)
        } else {
            console.log('ELSE!' )
            callback(undefined, {
                latitude: body.features[0].center[1],
                longitude: body.features[0].center[0],
                location: body.features[0].place_name
            })
        }
    })
}

module.exports = geocode