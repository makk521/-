// const fun = async function() {
//     let res = await  fetch('http://43.153.21.199:5000/',{
//         method: "POST",

//         body: '你好'
//     });
//     let data = await res.json();
//     console.log(data)
    
// }
// fun()

// fetch('http://43.153.21.199:5000/', {
//     method: 'POST',

//     body: JSON.stringify({
//       key1: 111,
//       key2: '111',
//       key3: 111
//     })
//   })

// const fun = async function() {
//     let res = await  fetch('http://43.153.21.199:5000/',{
//         method: "POST",
//         headers: {
//             "X-APISpace-Token":"23rtlq8nj6ctlbd7gdnb6mko5lshcjgr",
//             "Authorization-Type":"apikey",
//             "Content-Type":"application/json"
//         },
//         body: '{"cpCode":"YUNDA",     "mailNo":"4329504801266xxxx",     "tel":"0000",      "orderType":"asc"}'
//     });
//     let data = await res.json();
//     console.log(data)
    
// }
// fun()

fetch('http://43.153.21.199:5000/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
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