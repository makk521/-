
fetch('/api/endpoint', {
    method: 'POST',
    headers: {
        'Content-Type': 'http://43.153.21.199:5000/'
    },
    body: JSON.stringify({data: 'hello world'})
})
.then(response => {
    if (response.ok) {
        console.log('Request succeeded!');
    } else {
        console.log('Request failed.');
    }
})
.catch(error => {
    console.log('Request failed:', error);
});